from reliability.PoF import stress_strain_diagram
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(121)
print('Tension first:')
stress_strain_diagram(E=210000, K=1200, n=0.2, max_stress=378,
                      min_stress=-321, initial_load_direction='tension')
plt.title('Cyclic loading - tension first')
plt.subplot(122)
print('Compression first:')
stress_strain_diagram(E=210000, K=1200, n=0.2, max_stress=378,
                      min_stress=-321, initial_load_direction='compression')
plt.title('Cyclic loading - compression first')
plt.gcf().set_size_inches(12, 7)
plt.show()

'''
Tension first:
Max stress: 378.0
Min stress: -328.8931121800317
Max strain: 0.004901364196875
Min strain: -0.0028982508530831477
Compression first:
Max stress: 385.8931121800323
Min stress: -320.99999999999943
Max strain: 0.004901364196875
Min strain: -0.0028982508530831477
'''
