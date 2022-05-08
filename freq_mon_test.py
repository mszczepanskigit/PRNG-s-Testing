import math
from bits_files import bin_to_list
from scipy.stats import norm
import random
from int_to_bit import int_to_bit_on_list

def freq_mon_test(list_of_bits):
    sum_stat = 0
    n = len(list_of_bits)
    for i in range(n):
        sum_stat += 2 * int(list_of_bits[i]) - 1
    sum_stat = sum_stat / math.sqrt(n)
    p_val = 2 * (1 - norm.cdf(abs(sum_stat)))
    #print(f"Statistic: {sum_stat} \nP-value: {p_val}")
    return p_val, sum_stat


if __name__ == "__main__":
    freq_mon_test(int_to_bit_on_list([random.randint(0, 7) for _ in range(1000)]))

