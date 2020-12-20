from reliability.PoF import fracture_mechanics_crack_growth
import matplotlib.pyplot as plt
fracture_mechanics_crack_growth(
    Kc=66, C=6.91*10**-12, m=3, P=0.15, W=100, t=5, Kt=2.41, D=10)
plt.show()

'''
SIMPLIFIED METHOD (keeping f(g), S_max, and a_crit as constant):
Crack growth was found in two stages since the transition length ( 2.08 mm ) due to the notch, was greater than the initial crack length ( 1 mm ).
Stage 1 (a_initial to transition length): 6802 cycles
Stage 2 (transition length to a_final): 1133 cycles
Total cycles to failure: 7935 cycles.
Critical crack length to cause failure was found to be: 7.86 mm.

ITERATIVE METHOD (recalculating f(g), S_max, and a_crit for each cycle):
Crack growth was found in two stages since the transition length ( 2.45 mm ) due to the notch, was greater than the initial crack length ( 1 mm ).
Stage 1 (a_initial to transition length): 7576 cycles
Stage 2 (transition length to a_final): 671 cycles
Total cycles to failure: 8247 cycles.
Critical crack length to cause failure was found to be: 6.39 mm.
'''
