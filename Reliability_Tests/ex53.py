from reliability.PoF import fracture_mechanics_crack_initiation
fracture_mechanics_crack_initiation(P=0.15, A=5*80, Kt=2.41, q=0.9857, Sy=690, E=210000, K=1060,
                                    n=0.14, b=-0.081, c=-0.65, sigma_f=1160, epsilon_f=1.1, mean_stress_correction_method='SWT')

'''
A crack of 1 mm will be formed after: 2919.91 cycles ( 5839.82 reversals )
Stresses in the component: Min = -506.7291 MPa , Max = 506.7291 MPa , Mean = -5.684341886080802e-14 MPa.
Strains in the component: Min = -0.0075 , Max = 0.0075 , Mean = 8.673617379884035e-19
Mean stress correction method used: SWT
'''
