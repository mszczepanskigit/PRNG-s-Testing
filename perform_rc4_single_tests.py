from rc4 import rc4
import random
import matplotlib.pyplot as plt
from birthday_spacing import birthday_spacing_test
from freq_mon_test import freq_mon_test
from longest_run_test import longest_runs_test
from pair_test import pair_test
from chi2_new import chi2_test
from scipy.stats import kstest
from int_to_bit import int_to_bit_on_list

if __name__ == "__main__":
    nums_single = rc4(K=[7], n=9 * 10 ** 6)

    nums_random1 = rc4(K=[24, 26, 2, 16], n=3 * 10 ** 6)
    nums_random2 = rc4(K=[31, 25, 19, 30, 22, 13, 8, 18], n=3 * 10 ** 6)
    nums_random3 = rc4(K=[8, 6, 16, 9, 19, 6, 4, 21, 30, 6, 22, 27, 20, 13, 30, 28], n=3 * 10 ** 6)
    nums_random = nums_random1 + nums_random2 + nums_random3

    nums_ordered = rc4(K=[5, 6, 7, 8, 9, 10, 11, 12], n=9 * 10 ** 6)
    """print("Single")
    print(kstest([x / 32 for x in nums_single], 'uniform', N=len(nums_single)))
    nums_single_chi2 = [0]*8
    for i in [x % 8 for x in nums_single]:
        nums_single_chi2[i] += 1
    print("chi2:", chi2_test(obs=nums_single_chi2, exp=[9*10**6/8]*8))
    print("pair:", pair_test(nums_single))
    nums_single_bit = int_to_bit_on_list(nums_single)
    print("freq:", freq_mon_test(nums_single_bit)[0])
    print("run:", longest_runs_test(nums_single_bit)[0])"""
    """
    print("Random")
    print(kstest([x / 32 for x in nums_random], 'uniform', N=len(nums_random)))
    nums_random_chi2 = [0] * 8
    for i in [x % 8 for x in nums_random]:
        nums_random_chi2[i] += 1
    print("chi2:", chi2_test(obs=nums_random_chi2, exp=[9 * 10 ** 6 / 8] * 8))
    print("pair:", pair_test(nums_random))
    nums_random_bit = int_to_bit_on_list(nums_random)
    print("freq:", freq_mon_test(nums_random_bit)[0])
    print("run:", longest_runs_test(nums_random_bit)[0])
    """
    print("Ordered")
    print(kstest([x / 32 for x in nums_ordered], 'uniform', N=len(nums_ordered)))
    nums_ordered_chi2 = [0] * 8
    for i in [x % 8 for x in nums_ordered]:
        nums_ordered_chi2[i] += 1
    print(chi2_test(obs=nums_ordered_chi2, exp=[9 * 10 ** 6 / 8] * 8))
    print(pair_test(nums_ordered))
    nums_ordered_bit = int_to_bit_on_list(nums_ordered)
    print(freq_mon_test(nums_ordered_bit))
    print(longest_runs_test(nums_ordered_bit))

    plt.hist(nums_ordered[1:13000], bins=32, rwidth=0.85, color="b", density=True)
    plt.title(f"13000 numbers of RC(4) with random key")
    plt.show()

    plt.plot(nums_ordered[1:100], color="b", ls="-", alpha=1)
    plt.title("100 numbers of RC(4) with random key")
    plt.show()
