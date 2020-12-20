from reliability.ALT_probability_plotting import ALT_probability_plot_Normal
from reliability.Datasets import ALT_temperature
import matplotlib.pyplot as plt
ALT_probability_plot_Normal(failures=ALT_temperature().failures, failure_stress=ALT_temperature(
).failure_stresses, right_censored=ALT_temperature().right_censored, right_censored_stress=ALT_temperature().right_censored_stresses)
plt.show()

'''
ALT Normal probability plot results:
  stress  original mu  original sigma       new mu  common sigma sigma change
      40  9098.952677     3203.855879  7764.809302    2258.04215      -29.52%
      60  5174.454788     3021.349445  4756.980035    2258.04215      -25.26%
      80  1600.177190     1169.695509  1638.730675    2258.04215      +93.05%
Total AICc: 709.5115334757447
Total BIC: 713.4159440639235
'''
