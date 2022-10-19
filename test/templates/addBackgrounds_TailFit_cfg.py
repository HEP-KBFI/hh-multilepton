import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
#    fileNames = cms.vstring('/local/veelken/hhAnalysis/2017/2018Aug01v1/histograms/hh_2l_2tau/histograms_harvested_stage2_hh_2l_2tau_disabled_disabled_Tight_OS_with2016.root'),
    fileNames = cms.vstring('/local/veelken/hhAnalysis/2017/2018Aug01v1/histograms/hh_2l_2tau/addBackgroundLeptonFakes_hh_2l_2tau_disabled_disabled_OS.root'),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('out.root')
)


process.addBackgrounds_TailFit = cms.PSet(
    categories = cms.VPSet(
        cms.PSet(
            outputDir = cms.string("hh_2l_2tau_sumOS_Tight"),
            inputDir = cms.string("hh_2l_2tau_sumOS_Tight")
            ),
        ),
    processData = cms.string("data_fakes"),
    processToTailFit = cms.string("data_fakes"),
    processesToSubtract = cms.vstring(),
    sysShifts = cms.vstring(),
    apply_automatic_rebinning = cms.bool(True),
    minEvents_automatic_rebinning = cms.double(0.5),
    explicit_binning = cms.vdouble(),
    HistogramsToTailFit = cms.VPSet(
        cms.PSet(
            name = cms.string("dihiggsMass"),
            nominal_fit_func = cms.PSet(
                FitfuncName   = cms.string("Exponential"), 
                FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                  
                FitParameters = cms.vdouble(2.68, -0.0001), # norm, exponent                                                                                                                 
                ),  
            alternate_fit_funcs = cms.VPSet(
                #        cms.PSet(
                #            FitfuncName   = cms.string("LegendrePolynomial1"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax 
                #            FitParameters = cms.vdouble(2.2, 0.01), # par0, par1                                                                                             
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("LegendrePolynomial2"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax  
                #            FitParameters = cms.vdouble(2.2, 0.01, 0.0001), # par0, par1, par2                                                                                             
                #            ),
                cms.PSet(
                    FitfuncName   = cms.string("LegendrePolynomial3"), 
                    FitRange      = cms.vdouble(500., 1500.), # xmin, xmax    
                    FitParameters = cms.vdouble(2.2, 0.0001, 0.0001, 0.0001), # par0, par1, par2, par3                                                                                             
                    ),
                #        cms.PSet(## FIT SUCCEEDS BUT GIVES "Error in <GSLError>: Error 21 in qags.c at 553 : bad integrand behavior found in the integration interval"
                #            FitfuncName   = cms.string("ATLASFitFunc"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax  
                #            FitParameters = cms.vdouble(2.2, 0.1, 0.06), # par0, par1, par2                                                                                             
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("CrystalBall"), 
                #            FitRange      = cms.vdouble(90., 200.), # xmin, xmax                                                                                    
                #            FitParameters = cms.vdouble(1.0, 0.7, 5.0, 170.0, 20.0), # norm, alpha, n, mu, sigma                                                                                    
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("ExponentialErf"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                  
                #            FitParameters = cms.vdouble(2.2, 0.1, 600.0, 100.0), # norm, exponent, mean, sigma                                                                                     
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("Gaussian"),  
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                             
                #            FitParameters = cms.vdouble(2., 500.0, 200.0), # norm, mean, sigma                                                                                                       
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("DoubleGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                   
                #            FitParameters = cms.vdouble(5., 300.0, 50.0, 500.0, 100.0), # norm, mean0, sigma0, mean1, sigma1                                                                         
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("TripleGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                
                #            FitParameters = cms.vdouble(5., 300.0, 10.0, 2.0, 500.0, 50.0, 1000.0, 100.0), # norm, mean0, sigma0, norm1, mean1, sigma1, mean2, sigma2                               
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("ExponentialGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                 
                #            FitParameters = cms.vdouble(3., -0.001, 500.0, 10.0), # norm, exponent, mean, sigma                                                                                     
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("DoubleExponentialGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                      
                #            FitParameters = cms.vdouble(10.0, 6.0, -0.0001, 500.0, 50.0, 800.0, 100.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1                                     
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("ErfExponentialGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                  
                #            FitParameters = cms.vdouble(10., -0.001, 500.0, 50.0, 800.0, 100.0), # norm0, exponent, mean0, sigma0, mean1, sigma1                                                   
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("DoubleErfExponentialGaussian"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                 
                #            FitParameters = cms.vdouble(10., 6.0, -0.0001, 500.0, 50.0, 750.0, 100.0, 900.0, 150.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1, mean2, sigma2
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("Voigt"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax
                #            FitParameters = cms.vdouble(10., 500.0, 100.0), # norm, sigma, gamma       
                #            ),
                #        cms.PSet(
                #            FitfuncName   = cms.string("DoubleGaussianVoigt"), 
                #            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                            
                #            FitParameters = cms.vdouble(10., 6.0, 100.0, 10.0, 150.0, 20.0, 180.0, 50.0), # norm0, norm1, sigma, gamma, mean0, sigma0, mean1, sigma1  
                #            ),
                )
            ),
        cms.PSet(
            name = cms.string("dihiggsVisMass"),
            nominal_fit_func = cms.PSet(
                FitfuncName   = cms.string("Exponential"), 
                FitRange      = cms.vdouble(300., 1500.), # xmin, xmax                                                                                                                  
                FitParameters = cms.vdouble(0.8, -0.001), # norm, exponent                                                                                                                 
                ),  
            alternate_fit_funcs = cms.VPSet(
                cms.PSet(
                    FitfuncName   = cms.string("LegendrePolynomial1"), 
                    FitRange      = cms.vdouble(300., 1500.), # xmin, xmax    
                    FitParameters = cms.vdouble(0.01, -0.01), # par0, par1, par2, par3                                                                                             
                    ),
                )
            ),
        cms.PSet(
            name = cms.string("STMET"),
            nominal_fit_func = cms.PSet(
                FitfuncName   = cms.string("Exponential"), 
                FitRange      = cms.vdouble(350., 1500.), # xmin, xmax                                                                                                                  
                FitParameters = cms.vdouble(0.002, -0.01), # norm, exponent                                                                                                                 
                ),  
            alternate_fit_funcs = cms.VPSet(
                cms.PSet(
                    FitfuncName   = cms.string("LegendrePolynomial1"), 
                    FitRange      = cms.vdouble(350., 1500.), # xmin, xmax    
                    FitParameters = cms.vdouble(0.1, 0.01), # par0, par1, par2, par3                                                                                             
                    ),
                )
            ),
        cms.PSet(
            name = cms.string("HT"),
            nominal_fit_func = cms.PSet(
                FitfuncName   = cms.string("Exponential"), 
                FitRange      = cms.vdouble(300., 1500.), # xmin, xmax                                                                                                                  
                FitParameters = cms.vdouble(0.7, -0.0001), # norm, exponent                                                                                                                 
                ),  
            alternate_fit_funcs = cms.VPSet(
                cms.PSet(
                    FitfuncName   = cms.string("LegendrePolynomial1"), 
                    FitRange      = cms.vdouble(300., 1500.), # xmin, xmax    
                    FitParameters = cms.vdouble(0.05, 0.01), # par0, par1, par2, par3                                                                                             
                    ),
                )
            ),
        cms.PSet(
            name = cms.string("mTauTauVis"),
            nominal_fit_func = cms.PSet(
                FitfuncName   = cms.string("Exponential"), 
                FitRange      = cms.vdouble(90., 200.), # xmin, xmax                                                                                                                  
                FitParameters = cms.vdouble(1.0, -0.01), # norm, exponent                                                                                                                 
                ),  
            alternate_fit_funcs = cms.VPSet(
                cms.PSet(
                    FitfuncName   = cms.string("LegendrePolynomial3"), 
                    FitRange      = cms.vdouble(90., 200.), # xmin, xmax    
                    FitParameters = cms.vdouble(1.0, 0.1, 0.01, 0.001), # par0, par1, par2, par3                                                                                             
                    ),
                )
            ),
        )    
    )

'''
## OLD ---
    InputDir  = cms.string("hh_2l_2tau_sumOS_Tight"),
    processName = cms.string("data_fakes"),
    histogramName = cms.string("dihiggsMass"),


    apply_automatic_rebinning = cms.bool(True),
    minEvents_automatic_rebinning = cms.double(0.5),
    explicit_binning = cms.vdouble(),
    nominal_fit_func = cms.PSet(
        FitfuncName   = cms.string("Exponential"), 
        FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                  
        FitParameters = cms.vdouble(2.68, -0.0001), # norm, exponent                                                                                                                 
        ),
    alternate_fit_funcs = cms.VPSet(
#        cms.PSet(
#            FitfuncName   = cms.string("LegendrePolynomial1"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax 
#            FitParameters = cms.vdouble(2.2, 0.01), # par0, par1                                                                                             
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("LegendrePolynomial2"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax  
#            FitParameters = cms.vdouble(2.2, 0.01, 0.0001), # par0, par1, par2                                                                                             
#            ),
        cms.PSet(
             FitfuncName   = cms.string("LegendrePolynomial3"), 
             FitRange      = cms.vdouble(500., 1500.), # xmin, xmax    
             FitParameters = cms.vdouble(2.2, 0.0001, 0.0001, 0.0001), # par0, par1, par2, par3                                                                                             
            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ATLASFitFunc"), ## FIT SUCCEEDS BUT GIVES "Error in <GSLError>: Error 21 in qags.c at 553 : bad integrand behavior found in the integration interval"
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax  
#            FitParameters = cms.vdouble(2.2, 0.1, 0.06), # par0, par1, par2                                                                                             
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("CrystalBall"), 
#            FitRange      = cms.vdouble(90., 200.), # xmin, xmax                                                                                    
#            FitParameters = cms.vdouble(1.0, 0.7, 5.0, 170.0, 20.0), # norm, alpha, n, mu, sigma                                                                                           
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ExponentialErf"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(2.2, 0.1, 600.0, 100.0), # norm, exponent, mean, sigma                                                                                            
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("Gaussian"),  
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                             
#            FitParameters = cms.vdouble(2., 500.0, 200.0), # norm, mean, sigma                                                                                                                    
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(5., 300.0, 50.0, 500.0, 100.0), # norm, mean0, sigma0, mean1, sigma1                                                                                        
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("TripleGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                
#            FitParameters = cms.vdouble(5., 300.0, 10.0, 2.0, 500.0, 50.0, 1000.0, 100.0), # norm, mean0, sigma0, norm1, mean1, sigma1, mean2, sigma2                                              
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ExponentialGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(3., -0.001, 500.0, 10.0), # norm, exponent, mean, sigma                                                                                                     
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleExponentialGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                      
#            FitParameters = cms.vdouble(10.0, 6.0, -0.0001, 500.0, 50.0, 800.0, 100.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1                                             
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ErfExponentialGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(10., -0.001, 500.0, 50.0, 800.0, 100.0), # norm0, exponent, mean0, sigma0, mean1, sigma1                                                                    
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleErfExponentialGaussian"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                
#            FitParameters = cms.vdouble(10., 6.0, -0.0001, 500.0, 50.0, 750.0, 100.0, 900.0, 150.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1, mean2, sigma2
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("Voigt"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax
#            FitParameters = cms.vdouble(10., 500.0, 100.0), # norm, sigma, gamma       
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleGaussianVoigt"), 
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(10., 6.0, 100.0, 10.0, 150.0, 20.0, 180.0, 50.0), # norm0, norm1, sigma, gamma, mean0, sigma0, mean1, sigma1  
#            ),
     )
'''


