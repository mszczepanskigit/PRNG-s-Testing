from qcg import qcg
import matplotlib.pyplot as plt
from int_to_bit import int_to_bit_on_list
from freq_mon_test import freq_mon_test
from longest_run_test import longest_runs_test
from chi2_new import chi2_test
from pair_test import pair_test
from birthday_spacing import birthday_spacing_test
import numpy as np
from lcg import lcg
from scipy.stats import kstest

if __name__ == "__main__":
    nums = qcg(x_0=1, n=10_000, a=1, b=4, c=5, m=11)
    plt.hist(nums, bins=11, rwidth=0.85, color="cyan", density=True)
    plt.title(f"QCG : $x_0=1, n=1e5, a=1, b=4, c=5, m=11$")
    #plt.show()

    plt.plot(nums[1:100], color="cyan", ls="-", alpha=1)
    plt.title("100 numbers of QCG")
    #plt.show()

    nums2 = qcg(x_0=1, n=2**16, a=1, b=4, c=5, m=5)
    nums_bin = int_to_bit_on_list(qcg(x_0=1, n=2**16, a=1, b=3, c=11, m=16))

    #freq_mon_test(nums_bin)
    #longest_runs_test(nums_bin)
    #pair_test(nums2)
    nums2 = np.array(nums2[0:100]) + 1
    #print("to", birthday_spacing_test([x+1 for x in lcg(mod=7, a=1, c=5, x_0=1, n=200)], 7))
    nums_01 = [x/max(nums2) for x in nums2]
    print(kstest(nums_01, 'uniform', N=len(nums_01)))