from mt import mt
import random
import matplotlib.pyplot as plt
from birthday_spacing import birthday_spacing_test
from freq_mon_test import freq_mon_test
from longest_run_test import longest_runs_test
from scipy.stats import kstest
from chi2_new import chi2_test
from pair_test import pair_test


if __name__ == "__main__":
    nums = mt(x_0=0, n=5000, a=0, b=7)
    nums2 = [random.random() for _ in range(500)]
    plt.hist(nums, bins=8, rwidth=0.85, color="m", density=True)
    plt.title("5000 numbers from {0, 1, 2 ,3 ,4, 5 ,6, 7}")
    plt.show()
    plt.plot(nums2, color="m", ls="-", alpha=1)
    plt.title("500 numbers from interval (0,1)")
    # plt.show()

    numbers_int = mt(x_0=0, n=2**20, a=0, b=7)
    numbers_bits = mt(x_0=0, n=2**20, a=0, b=1)
    numbers_int2 = mt(x_0=1, n=2 ** 20, a=0, b=2**16)

    longest_runs_test(numbers_bits)
    freq_mon_test(numbers_bits)
    #print(birthday_spacing_test(mt(x_0=0, n=2**20, a=1, b=8), 8))
    print(kstest([random.random() for _ in range(2**20)], 'uniform', N=2**20))
    obsv = [0]*8
    for x in numbers_int:
        obsv[x] += 1
    print(chi2_test(obs=obsv, exp=[2**20/8]*8))
    print(pair_test(numbers_int))
