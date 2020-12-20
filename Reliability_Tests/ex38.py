from reliability.Nonparametric import RankAdjustment
import matplotlib.pyplot as plt

f = [5248, 7454, 16890, 17200, 38700, 45000, 49390, 69040, 72280, 131900]
rc = [3961, 4007, 4734, 6054, 7298, 10190, 23060, 27160, 28690, 37100, 40060,
      45670, 53000, 67000, 69630, 77350, 78470, 91680, 105700, 106300, 150400]
a_trials = [0, 0.3, 1]
for a in a_trials:
    RankAdjustment(failures=f, right_censored=rc,
                   print_results=False, a=a, label=str(a))
plt.legend(title="Heuristic 'a'")
plt.title('Effect of rank adjustment heuristic')
plt.show()
