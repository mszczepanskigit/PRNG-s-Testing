import numpy as np
from scipy.stats import chisquare
from scipy.stats.distributions import chi2

# argument to lista p-value
# najlepiej miec 1000–10000 p_wartosci, kazda na podstawie testu dla n = 2^20 - 2^32 wygenerowanych liczb

def sec_l_test(p_wartosci):
    R = len(p_wartosci)
    s = 10
    o = [0 for _ in range(10)]
    e = [R/s for _ in range(10)]
    e = np.array(e)
    for j in p_wartosci:
        for i in range(1,s+1):
            if (j >= (i-1)/s) and (j < i/s):
                o[i-1] += 1
    o = np.array(o)
    stat = sum(((o-e) ** 2)/e)
    p_final = chi2.sf(stat, s-1)
    return p_final

