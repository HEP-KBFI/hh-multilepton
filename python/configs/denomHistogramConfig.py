from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists, run_cmd, get_log_version, record_software_state, check_submission_cmd
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, createFile, generateInputFileList
from tthAnalysis.HiggsToTauTau.analysisTools import createMakefile as tools_createMakefile
from tthAnalysis.HiggsToTauTau.sbatchManagerTools import createScript_sbatch as tools_createScript_sbatch
from tthAnalysis.HiggsToTauTau.sbatchManagerTools import createScript_sbatch_hadd as tools_createScript_sbatch_hadd
from tthAnalysis.HiggsToTauTau.sbatchManagerTools import is_file_ok as tools_is_file_ok
from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.common import logging, DEPENDENCIES

import os
import uuid
import re

DKEY_SCRIPTS    = "scripts"
DKEY_CFGS       = "cfgs"
DKEY_HISTO_TMP  = "tmp_histograms"
DKEY_HISTO      = "histograms"
DKEY_PLOTS      = "plots"
DKEY_LOGS       = "logs"
DKEY_HADD_RT    = "hadd_cfg_rt"
MAKEFILE_TARGET = "sbatch_nonResDenom"

def validate_denom(output_file, samples):
    error_code = 0
    if not os.path.isfile(output_file):
        logging.error('File {} does not exist'.format(output_file))
        return 1
    histogram_file = ROOT.TFile.Open(output_file, 'read')
    if not histogram_file:
        logging.error('Not a valid ROOT file: {}'.format(output_file))
        return 2
    category_sums = {}
    for sample_name, sample_info in samples.items():
        if not sample_info["use_it"]:
            continue
        process_name = sample_info["process_name_specific"]
        category_name = sample_info["sample_category"]
        expected_nof_events = sample_info["nof_tree_events"]
        if category_name not in category_sums:
            category_sums[category_name] = 0
        category_sums[category_name] += expected_nof_events
        logging.info('Validating {} (expecting {} events)'.format(process_name, expected_nof_events))
        histogram = histogram_file.Get(process_name)
        if not histogram:
            logging.error("Could not find histogram '{}' in file {}".format(process_name, output_file))
            error_code = 3
            continue
        nof_events = int(histogram.GetEntries())
        if nof_events != expected_nof_events:
            logging.error(
                'Histogram {} in file {} has {} events, but expected {} events'.format(
                    process_name, output_file, nof_events, expected_nof_events,
                )
            )
            error_code = 4
        else:
            logging.info('Validation successful for sample {}'.format(process_name))

    for category_name, expected_nof_events in category_sums.items():
        histogram = histogram_file.Get(category_name)
        if not histogram:
            logging.error("Could not find histogram '{}' in file {}".format(category_name, output_file))
            error_code = 3
        nof_events = int(histogram.GetEntries())
        if nof_events != expected_nof_events:
            logging.error(
                'Histogram {} in file {} has {} events, but expected {} events'.format(
                    category_name, output_file, nof_events, expected_nof_events,
                )
            )
            error_code = 4
        else:
            logging.info('Validation successful for category {}'.format(category_name))

    histogram_file.Close()
    if error_code == 0:
        logging.info("Validation successful!")
    else:
        logging.error("Validation failed!")
    return error_code

class denomHistogramConfig:
    """Configuration metadata needed to run PU profile production.

    Args:
        configDir:             The root config dir -- all configuration files are stored in its subdirectories
        outputDir:             The root output dir -- all log and output files are stored in its subdirectories
        executable:            Name of the executable that runs the PU profile production
        check_output_files:     if True, checks each input root file (Ntuple) before creating the python configuration files
        running_method:        either `sbatch` (uses SLURM) or `Makefile`
        num_parallel_jobs:     number of jobs that can be run in parallel on local machine
                               (does not limit number of PU profile production jobs running in parallel on batch system)

    """
    def __init__(self,
            configDir,
            localDir,
            outputDir,
            output_file,
            executable,
            samples,
            max_files_per_job,
            era,
            binning,
            use_gen_weight,
            check_output_files,
            running_method,
            num_parallel_jobs,
            pool_id  = '',
            verbose  = False,
            dry_run  = False,
            use_home = False,
            keep_logs = False,
            submission_cmd = None,
          ):

        self.configDir             = configDir
        self.localDir              = localDir
        self.outputDir             = outputDir
        self.executable            = executable
        self.max_num_jobs          = 200000
        self.samples               = samples
        self.max_files_per_job     = max_files_per_job
        self.era                   = era
        self.binning               = binning
        self.use_gen_weight        = use_gen_weight
        self.check_output_files    = check_output_files
        self.verbose               = verbose
        self.dry_run               = dry_run
        self.use_home              = use_home
        self.keep_logs             = keep_logs
        if running_method.lower() not in ["sbatch", "makefile"]:
          raise ValueError("Invalid running method: %s" % running_method)

        self.running_method    = running_method
        self.is_sbatch         = self.running_method.lower() == "sbatch"
        self.is_makefile       = not self.is_sbatch
        self.makefile          = os.path.join(self.localDir, "Makefile_nonResDenom")
        self.num_parallel_jobs = num_parallel_jobs
        self.pool_id           = pool_id if pool_id else uuid.uuid4()

        self.workingDir = os.getcwd()
        logging.info("Working directory is: %s" % self.workingDir)
        self.template_dir = os.path.join(
            os.getenv('CMSSW_BASE'), 'src', 'tthAnalysis', 'HiggsToTauTau', 'test', 'templates'
        )
        logging.info("Templates directory is: %s" % self.template_dir)

        create_if_not_exists(self.configDir)
        create_if_not_exists(self.localDir)
        create_if_not_exists(self.outputDir)
        self.output_file      = os.path.join(self.outputDir, output_file)
        self.stdout_file_path = os.path.join(self.localDir, "stdout_nonResDenom.log")
        self.stderr_file_path = os.path.join(self.localDir, "stderr_nonResDenom.log")
        self.sw_ver_file_cfg  = os.path.join(self.localDir, "VERSION_nonResDenom.log")
        self.sw_ver_file_out  = os.path.join(self.outputDir, "VERSION_nonResDenom.log")
        self.submission_out   = os.path.join(self.localDir, "SUBMISSION_nonResDenom.log")
        self.stdout_file_path, self.stderr_file_path, self.sw_ver_file_cfg, self.sw_ver_file_out, self.submission_out = get_log_version((
            self.stdout_file_path, self.stderr_file_path, self.sw_ver_file_cfg, self.sw_ver_file_out, self.submission_out
        ))
        check_submission_cmd(self.submission_out, submission_cmd)

        self.sbatchFile_nonResDenom = os.path.join(self.localDir, "sbatch_nonResDenom.py")
        self.cfgFiles_nonResDenom    = {}
        self.logFiles_nonResDenom    = {}
        self.scriptFiles_nonResDenom = {}
        self.jobOptions_sbatch     = {}

        self.inputFiles      = {}
        self.outputFiles_tmp = {}
        self.outputFiles     = {}

        self.phoniesToAdd = []
        self.filesToClean = [ self.configDir ]
        self.targets = []

        self.dirs = {}
        all_dirs = [ DKEY_CFGS, DKEY_HISTO_TMP, DKEY_HISTO, DKEY_PLOTS, DKEY_LOGS, DKEY_SCRIPTS, DKEY_HADD_RT ]
        cfg_dirs = [ DKEY_CFGS, DKEY_LOGS, DKEY_PLOTS, DKEY_SCRIPTS, DKEY_HADD_RT ]

        self.gen_weights = {}
        if self.use_gen_weight:
            ref_genweights = os.path.join(
                os.environ['CMSSW_BASE'], 'src', 'tthAnalysis', 'HiggsToTauTau', 'data', 'refGenWeight_{}.txt'.format(era)
            )
            with open(ref_genweights, 'r') as f:
                for line in f:
                    line_split = line.strip().split()
                    assert(len(line_split) == 2)
                    sample_name = line_split[0]
                    ref_genweight = float(line_split[1])
                    assert(sample_name not in self.gen_weights)
                    self.gen_weights[sample_name] = ref_genweight

        for sample_name, sample_info in self.samples.items():
            if not sample_info['use_it']:
                continue
            process_name = sample_info["process_name_specific"]
            if self.use_gen_weight:
                assert(re.sub('_duplicate$', '', process_name) in self.gen_weights)
            key_dir = getKey(process_name)
            for dir_type in all_dirs:
                if dir_type == DKEY_PLOTS:
                    continue
                initDict(self.dirs, [ key_dir, dir_type ])
                if dir_type in cfg_dirs:
                    dir_choice = self.configDir if dir_type == DKEY_CFGS else self.localDir
                    self.dirs[key_dir][dir_type] = os.path.join(dir_choice, dir_type, process_name)
                else:
                    self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, process_name)
        for dir_type in cfg_dirs:
            initDict(self.dirs, [ dir_type ])
            dir_choice = self.configDir if dir_type == DKEY_CFGS else self.localDir
            self.dirs[dir_type] = os.path.join(dir_choice, dir_type)
            if dir_choice != self.configDir:
                self.filesToClean.append(self.dirs[dir_type])

        self.cvmfs_error_log = {}
        self.num_jobs = {
            'hadd'        : 0,
            'nonResDenom' : 0,
            'plot'        : 0,
        }


    def createCfg_nonResDenom(self, jobOptions):
        """Create python configuration file for the denomHistogramProducer.sh script

        Args:
          inputFiles: list of input files (Ntuples)
          outputFile: output file of the job -- a ROOT file containing histogram
        """
        lines = jobOptions['inputFiles'] + \
                [ '', '%s %s %s %s %s' % (
                    jobOptions['processName'], jobOptions['categoryName'], jobOptions['outputFile'],
                    ('%.6e' % jobOptions['genWeight']) if self.use_gen_weight else '0', self.binning,
                ) ]
        assert(len(lines) >= 3)
        createFile(jobOptions['cfgFile_path'], lines, nofNewLines = 1)

    def createScript_sbatch(self,
                            executable,
                            sbatchFile,
                            jobOptions,
                            key_cfg_file    = 'cfgFile_path',
                            key_input_file  = 'inputFiles',
                            key_output_file = 'outputFile',
                            key_log_file    = 'logFile',
                            key_script_file = 'scriptFile',
                           ):
        num_jobs = tools_createScript_sbatch(
            sbatch_script_file_name = sbatchFile,
            executable              = executable,
            command_line_parameters = { key: value[key_cfg_file]    for key, value in jobOptions.items() },
            input_file_names        = { key: value[key_input_file]  for key, value in jobOptions.items() },
            output_file_names       = { key: value[key_output_file] for key, value in jobOptions.items() },
            script_file_names       = { key: value[key_script_file] for key, value in jobOptions.items() },
            log_file_names          = { key: value[key_log_file]    for key, value in jobOptions.items() },
            keep_logs               = self.keep_logs,
            working_dir             = self.workingDir,
            max_num_jobs            = self.max_num_jobs,
            cvmfs_error_log         = self.cvmfs_error_log,
            pool_id                 = uuid.uuid4(),
            verbose                 = self.verbose,
            dry_run                 = self.dry_run,
            job_template_file       = 'sbatch-node.produce.sh.template',
            validate_outputs        = self.check_output_files,
            min_file_size           = -1,
            use_home                = self.use_home,
        )
        return num_jobs

    def create_hadd_python_file(self, inputFiles, outputFile, hadd_stage_name, process_name = ''):
        sbatch_hadd_file = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_hadd_%s.py" % hadd_stage_name)
        sbatch_hadd_file = sbatch_hadd_file.replace(".root", "")

        scriptsDir = self.dirs[process_name][DKEY_SCRIPTS] if process_name else self.dirs[DKEY_SCRIPTS]
        logDir     = self.dirs[process_name][DKEY_LOGS]    if process_name else self.dirs[DKEY_LOGS]
        haddRtDir  = self.dirs[process_name][DKEY_HADD_RT] if process_name else self.dirs[DKEY_HADD_RT]

        scriptFile      = os.path.join(scriptsDir, os.path.basename(sbatch_hadd_file).replace(".py", ".sh"))
        logFile         = os.path.join(logDir,     os.path.basename(sbatch_hadd_file).replace(".py", ".log"))
        sbatch_hadd_dir = os.path.join(haddRtDir,  hadd_stage_name)

        self.num_jobs['hadd'] += tools_createScript_sbatch_hadd(
            sbatch_script_file_name = sbatch_hadd_file,
            input_file_names        = inputFiles,
            output_file_name        = outputFile,
            script_file_name        = scriptFile,
            log_file_name           = logFile,
            working_dir             = self.workingDir,
            auxDirName              = sbatch_hadd_dir,
            pool_id                 = uuid.uuid4(),
            verbose                 = self.verbose,
            dry_run                 = self.dry_run,
            use_home                = self.use_home,
            max_input_files_per_job = 20,
            min_file_size           = -1,
        )
        return sbatch_hadd_file

    def addToMakefile_nonResDenom(self, lines_makefile):
        """Adds the commands to Makefile that are necessary for running the denominator production code
        """
        if self.is_sbatch:
            lines_makefile.extend([
                "%s:" % MAKEFILE_TARGET,
                "\t%s %s" % ("python", self.sbatchFile_nonResDenom),
                "",
            ])
        for key_file, output_file in self.outputFiles_tmp.items():
            cfg_file = self.cfgFiles_nonResDenom[key_file]
            if self.is_makefile:
                log_file = self.logFiles_nonResDenom[key_file]
                lines_makefile.extend([
                    "%s:" % output_file,
                    "\t%s %s &> %s" % (self.executable, cfg_file, log_file),
                    "",
                ])
            elif self.is_sbatch:
                lines_makefile.extend([
                    "%s: %s" % (output_file, MAKEFILE_TARGET),
                    "\t%s" % ":",
                    "",
                ])
        self.phoniesToAdd.append(MAKEFILE_TARGET)

    def addToMakefile_hadd(self, lines_makefile):
        scriptFiles = {}
        jobOptions = {}
        for key, cfg in self.outputFiles.items():
            scriptFiles[key] = self.create_hadd_python_file(
                inputFiles      = cfg['inputFiles'],
                outputFile      = cfg['outputFile'],
                hadd_stage_name = "_".join([ key, "ClusterHistogramAggregator" ]),
                process_name    = key,
            )
            jobOptions[key] = {
                'inputFiles'   : cfg['inputFiles'],
                'cfgFile_path' : scriptFiles[key],
                'outputFile'   : cfg['outputFile'],
                'logFile'      : os.path.join(
                    self.dirs[DKEY_LOGS],
                    'hadd_%s' % os.path.basename(cfg['outputFile']).replace(".root", ".log"),
                ),
            }

        for key, cfg in self.outputFiles.items():
            lines_makefile.extend([
                "%s: %s" % (cfg['outputFile'], ' '.join(cfg['inputFiles'])),
                "\trm -f %s" % cfg['outputFile'],
                "\tpython %s" % scriptFiles[key],
                "",
            ])

    def addToMakefile_plot(self, lines_makefile):
        cmd_string = "plot_from_histogram.py -i %s -j %s -o %s -x 'm_{HH}' " \
                     "-y '\\cos\\theta*' -t '%s'"
        cmd_log_string = cmd_string + " -l"

        jobOptions = {}
        for key, cfg in self.outputFiles.items():
            plot_linear = os.path.join(self.dirs[DKEY_PLOTS], '%s.png'     % key)
            plot_log    = os.path.join(self.dirs[DKEY_PLOTS], '%s_log.png' % key)
            logFile_linear = os.path.join(self.dirs[DKEY_LOGS], 'plot_linear_%s.log' % key)
            logFile_log    = os.path.join(self.dirs[DKEY_LOGS], 'plot_log_%s.log' % key)
            logFile_linear, logFile_log = get_log_version((
                logFile_linear, logFile_log
            ))
            jobOptions[key] = {
                'inputFile' : cfg['outputFile'],
                'jobs' : {
                    'linear' : {
                        'outputFile' : plot_linear,
                        'cmd'        : cmd_string % (cfg['outputFile'], key, plot_linear, key),
                        'logFile'    : logFile_linear,
                    },
                    'log' : {
                        'outputFile' : plot_log,
                        'cmd'        : cmd_log_string % (cfg['outputFile'], key, plot_log, key),
                        'logFile'    : logFile_log,
                    }
                }
            }
            plot_files = [
                jobOptions[key]['jobs'][plot_type]['outputFile'] for plot_type in jobOptions[key]['jobs']
            ]
            self.targets.extend(plot_files)

        for cfg in jobOptions.values():
            for plot_cfg in cfg['jobs'].values():
                lines_makefile.extend([
                    "%s: %s" % (plot_cfg['outputFile'], cfg['inputFile']),
                    "\t%s &> %s" % (plot_cfg['cmd'], plot_cfg['logFile']),
                    "",
                ])
                self.num_jobs['plot'] += 1

    def addToMakefile_finalHadd(self, lines_makefile):
        outputFiles     = [
            self.outputFiles[key]['outputFile'] for key in \
            sorted(self.outputFiles.keys(), key = lambda k: k.lower())
        ]
        outputFiles_cat = ' '.join(outputFiles)
        if self.is_sbatch:
            scriptFile = self.create_hadd_python_file(
                inputFiles      = outputFiles,
                outputFile      = self.output_file,
                hadd_stage_name = "_".join([ 'final', "ClusterHistogramAggregator" ]),
            )
            lines_makefile.extend([
                "%s: %s"      % (self.output_file, outputFiles_cat),
                "\trm -f %s"  % self.output_file,
                "\tpython %s" % scriptFile,
            ])
        else:
            lines_makefile.extend([
                "%s: %s"       % (self.output_file, outputFiles_cat),
                "\trm -f %s"   % self.output_file,
                "\thadd %s %s" % (self.output_file, outputFiles_cat),
                "",
            ])
            self.num_jobs['hadd'] += 1
        self.targets.append(self.output_file)

    def createMakefile(self, lines_makefile):
        """Creates Makefile that runs the PU profile production.
        """
        tools_createMakefile(
            makefileName   = self.makefile,
            targets        = self.targets,
            lines_makefile = lines_makefile,
            filesToClean   = self.filesToClean,
            isSbatch       = self.is_sbatch,
            phoniesToAdd   = self.phoniesToAdd
        )
        logging.info("Run it with:\tmake -f %s -j %i " % (self.makefile, self.num_parallel_jobs))

    def create(self):
        """Creates all necessary config files and runs the denominator production -- either locally or on the batch system
        """

        for key in self.dirs.keys():
            if type(self.dirs[key]) == dict:
                for dir_type in self.dirs[key].keys():
                    create_if_not_exists(self.dirs[key][dir_type])
            else:
                create_if_not_exists(self.dirs[key])

        self.inputFileIds = {}
        for sample_name, sample_info in self.samples.items():
            if not sample_info['use_it']:
                continue

            process_name = sample_info["process_name_specific"]
            is_mc = (sample_info["type"] == "mc")

            if not is_mc:
              continue

            logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable, process_name))

            inputFileList = generateInputFileList(sample_info, self.max_files_per_job)
            key_dir = getKey(process_name)

            outputFile = os.path.join(
                self.dirs[key_dir][DKEY_HISTO], "%s.root" % process_name
            )
            self.outputFiles[process_name] = {
                'inputFiles' : [],
                'outputFile' : outputFile
            }
            if os.path.isfile(outputFile) and tools_is_file_ok(outputFile, min_file_size = 2000):
                logging.info('File {} already exists --> skipping job'.format(outputFile))
                continue

            for jobId in inputFileList.keys():

                key_file = getKey(sample_name, jobId)

                self.inputFiles[key_file] = inputFileList[jobId]
                if len(self.inputFiles[key_file]) == 0:
                    logging.warning(
                        "ntupleFiles['%s'] = %s --> skipping job !!" % (key_file, self.inputFiles[key_file])
                    )
                    continue

                self.cfgFiles_nonResDenom[key_file] = os.path.join(
                    self.dirs[key_dir][DKEY_CFGS], "nonResDenom_%s_%i_cfg.txt" % (process_name, jobId)
                )
                self.outputFiles_tmp[key_file] = os.path.join(
                    self.dirs[key_dir][DKEY_HISTO_TMP], "histogram_%i.root" % jobId
                )
                self.logFiles_nonResDenom[key_file] = os.path.join(
                    self.dirs[key_dir][DKEY_LOGS], "nonResDenom_%s_%i.log" % (process_name, jobId)
                )
                self.scriptFiles_nonResDenom[key_file] = os.path.join(
                    self.dirs[key_dir][DKEY_CFGS], "nonResDenom_%s_%i_cfg.sh" % (process_name, jobId)
                )
                process_name_wodupl = re.sub('_duplicate$', '', process_name)
                ref_genweight = self.gen_weights[process_name_wodupl] if self.use_gen_weight else 0.
                self.jobOptions_sbatch[key_file] = {
                    'processName'  : process_name,
                    'categoryName' : sample_info['sample_category_hh'],
                    'genWeight'    : ref_genweight,
                    'inputFiles'   : self.inputFiles[key_file],
                    'cfgFile_path' : self.cfgFiles_nonResDenom[key_file],
                    'outputFile'   : self.outputFiles_tmp[key_file],
                    'logFile'      : self.logFiles_nonResDenom[key_file],
                    'scriptFile'   : self.scriptFiles_nonResDenom[key_file],
                }
                self.createCfg_nonResDenom(self.jobOptions_sbatch[key_file])
                self.outputFiles[process_name]['inputFiles'].append(self.outputFiles_tmp[key_file])

        if self.is_sbatch:
          logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable)
          self.num_jobs['nonResDenom'] += self.createScript_sbatch(
              self.executable, self.sbatchFile_nonResDenom, self.jobOptions_sbatch
          )

        logging.info("Creating Makefile")
        lines_makefile = []
        self.addToMakefile_nonResDenom(lines_makefile)
        self.addToMakefile_hadd(lines_makefile)
        #self.addToMakefile_plot(lines_makefile)
        self.addToMakefile_finalHadd(lines_makefile)
        self.createMakefile(lines_makefile)
        logging.info("Done")

        return self.num_jobs

    def run(self):
        """Runs all denominator production jobs -- either locally or on the batch system.
        """
        record_software_state(self.sw_ver_file_cfg, self.sw_ver_file_out, DEPENDENCIES)
        run_cmd(
            "make -f %s -j %i 2>%s 1>%s" % \
            (self.makefile, self.num_parallel_jobs, self.stderr_file_path, self.stdout_file_path),
            False
        )
