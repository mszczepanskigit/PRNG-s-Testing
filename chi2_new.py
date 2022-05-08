import numpy as np

from scipy.stats import chisquare
from scipy.stats.distributions import chi2

# obs : zaobserwowana liczba kul w i-tym pudelku
# exp : oczekiwana liczba kul w i-tym pudelku

def chi2_test(obs, exp):
    chi_square_stat = sum((np.array(obs) - np.array(exp))**2 / np.array(exp))
    #print("chi_square_stat = ", chi_square_stat, ", p-value = ", p_value)
    deg_of_freedom = len(obs) - 1
    #print("p-value = ", chi2.sf(chi_square_stat, deg_of_freedom))
    return chi2.sf(chi_square_stat, deg_of_freedom)