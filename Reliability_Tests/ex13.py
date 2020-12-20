from reliability.Fitters import Fit_Everything
# created using Weibull_Distribution(alpha=5,beta=2), and rounded to nearest int
data = [4, 4, 2, 4, 7, 4, 1, 2, 7, 1, 4, 3, 6, 6,
        6, 3, 2, 3, 4, 3, 2, 3, 2, 4, 6, 5, 5, 2, 4, 3]
Fit_Everything(failures=data, show_histogram_plot=False,
               show_probability_plot=False, show_PP_plot=False)

'''
                   Alpha      Beta     Gamma       Mu     Sigma    Lambda        AICc         BIC        AD
Distribution
Weibull_2P       4.21932   2.43761                                         117.696224  120.054175  1.048046
Gamma_2P        0.816685   4.57132                                         118.404666  120.762616  1.065917
Normal_2P                                     3.73333   1.65193            119.697592  122.055543  1.185387
Lognormal_2P                                  1.20395  0.503621            120.662122  123.020072  1.198573
Lognormal_3P                               0  1.20395  0.503621            123.140754  123.020072  1.198573
Weibull_3P       3.61252   2.02388  0.530239                               119.766821  123.047337  1.049479
Loglogistic_2P   3.45096   3.48793                                         121.089046  123.446996  1.056100
Loglogistic_3P   3.45096   3.48793         0                               123.567678  126.848194  1.056100
Exponential_2P                         0.999                      0.36572  124.797704  127.155654  2.899050
Gamma_3P         3.49645  0.781773    0.9999                               125.942453  129.222968  3.798788
Exponential_1P                                                   0.267857  141.180947  142.439287  4.710926
'''
