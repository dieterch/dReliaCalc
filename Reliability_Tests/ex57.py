from reliability.PoF import palmgren_miner_linear_damage
palmgren_miner_linear_damage(rated_life=[50000, 6500, 1000], time_at_stress=[
                             40/60, 15/60, 5/60], stress=[1, 2, 4])

'''
Palmgren-Miner Linear Damage Model results:
Each load cycle uses 0.01351 % of the components life.
The service life of the component is 7400.37951 load cycles.
The amount of damage caused at each stress level is:
Stress =  1 , Damage fraction = 9.86717 %.
Stress =  2 , Damage fraction = 28.463 %.
Stress =  4 , Damage fraction = 61.66983 %.
'''
