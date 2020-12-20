import matplotlib.pyplot as plt
from reliability.Other_functions import make_right_censored_data
from reliability.Nonparametric import KaplanMeier, NelsonAalen, RankAdjustment
from reliability.Distributions import Weibull_Distribution

dist = Weibull_Distribution(alpha=500, beta=2)

plt.figure(figsize=(12, 7))
samples = [10, 100, 1000]
for i, s in enumerate(samples):
    raw_data = dist.random_samples(number_of_samples=s, seed=42)
    # this will multiply-censor 50% of the data
    data = make_right_censored_data(
        data=raw_data, fraction_censored=0.5, seed=42)
    plt.subplot(131 + i)
    KaplanMeier(failures=data.failures, right_censored=data.right_censored,
                print_results=False, show_plot=True, label='Kaplan-Meier')
    NelsonAalen(failures=data.failures, right_censored=data.right_censored,
                print_results=False, show_plot=True, label='Nelson-Aalen')
    RankAdjustment(failures=data.failures, right_censored=data.right_censored,
                   print_results=False, show_plot=True, label='Rank Adjustment')
    dist.SF(label='Weibull Distribution', color='red')
    plt.title(str(str(s) + ' samples'))
    plt.legend()
plt.suptitle(
    'Comparison of Kaplan-Meier, Nelson-Aalen, and Rank Adjustment for varying sample sizes with 50% censoring')
plt.tight_layout()
plt.show()
