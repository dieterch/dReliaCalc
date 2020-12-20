from reliability.Distributions import Weibull_Distribution

dist = Weibull_Distribution(alpha=50, beta=2)
sf = dist.SF(20)
# we are converting the decimal answer (0.8521...) to a percentage
print('The value of the SF at 20 is', round(sf * 100, 2), '%')

'''
The value of the SF at 20 is 85.21 %
'''
