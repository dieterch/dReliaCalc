from reliability.ALT_probability_plotting import ALT_probability_plot_Weibull, ALT_probability_plot_Lognormal
from reliability.Datasets import ALT_temperature
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(121)
ALT_probability_plot_Weibull(failures=ALT_temperature().failures, failure_stress=ALT_temperature(
).failure_stresses, right_censored=ALT_temperature().right_censored, right_censored_stress=ALT_temperature().right_censored_stresses)
plt.subplot(122)
ALT_probability_plot_Lognormal(failures=ALT_temperature().failures, failure_stress=ALT_temperature(
).failure_stresses, right_censored=ALT_temperature().right_censored, right_censored_stress=ALT_temperature().right_censored_stresses)
plt.gcf().set_size_inches(15, 7)
plt.show()

'''
ALT Weibull probability plot results:
  stress  original alpha  original beta     new alpha  common beta beta change
      40    21671.954375       1.625115  21671.954523     1.519015      -6.53%
      60     6628.557163       1.315739   6628.557053     1.519015     +15.45%
      80     1708.487268       1.397979   1831.456045     1.519015      +8.66%
Total AICc: 686.2426265268432
Total BIC: 690.1470371150222

ALT Lognormal probability plot results:
  stress  original mu  original sigma    new mu  common sigma sigma change
      40     9.814749        1.008337  9.717867      0.939793        -6.8%
      60     8.644075        1.187552  8.507165      0.939793      -20.86%
      80     7.141321        0.770355  7.147846      0.939793      +21.99%
Total AICc: 683.8113391548707
Total BIC: 687.7157497430494
'''
