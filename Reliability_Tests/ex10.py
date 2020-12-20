from reliability.Distributions import Gamma_Distribution
from reliability.Fitters import Fit_Gamma_2P
from reliability.Other_functions import make_right_censored_data, histogram
import matplotlib.pyplot as plt

a = 30
b = 4
threshold = 180  # this is used when right censoring the data
trials = [10, 100, 1000, 10000]
subplot_id = 221
plt.figure(figsize=(9, 7))
for sample_size in trials:
    dist = Gamma_Distribution(alpha=a, beta=b)
    # create some data. Seeded for repeatability
    raw_data = dist.random_samples(sample_size, seed=2)
    data = make_right_censored_data(
        raw_data, threshold=threshold)  # right censor the data
    gf = Fit_Gamma_2P(failures=data.failures, right_censored=data.right_censored,
                      show_probability_plot=False, print_results=False)  # fit the Gamma_2P distribution
    print('\nFit_Gamma_2P parameters using', sample_size, 'samples:',
          '\nAlpha:', gf.alpha, '\nBeta:', gf.beta)  # print the results
    plt.subplot(subplot_id)
    # plots the histogram using optimal bin width and shades the right censored part white
    histogram(raw_data, white_above=threshold)
    dist.PDF(label='True')  # plots the true distribution
    # plots the fitted Gamma_2P distribution
    gf.distribution.PDF(label='Fitted', linestyle='--')
    plt.title(str(str(sample_size) + ' samples\n' + r'$\alpha$ error: ' + str(round(abs(gf.alpha - a) /
                                                                                    a * 100, 2)) + '%\n' + r'$\beta$ error: ' + str(round(abs(gf.beta - b) / b * 100, 2)) + '%'))
    plt.ylim([0, 0.012])
    plt.xlim([0, 500])
    plt.legend()
    subplot_id += 1
plt.subplots_adjust(left=0.11, bottom=0.08, right=0.95,
                    top=0.89, wspace=0.33, hspace=0.58)
plt.show()

'''
Fit_Gamma_2P parameters using 10 samples:
Alpha: 19.426036067937076
Beta: 4.690126148584235

Fit_Gamma_2P parameters using 100 samples:
Alpha: 36.26423078012859
Beta: 3.292935791420746

Fit_Gamma_2P parameters using 1000 samples:
Alpha: 28.825237245698354
Beta: 4.062929181298052

Fit_Gamma_2P parameters using 10000 samples:
Alpha: 30.30127379917658
Beta: 3.960086262727073
'''
