from lcg import lcg
import numpy as np
from second_level import sec_l_test
from chi2_test_new import chi2_test
import matplotlib.pyplot as plt
import csv
from birthday_spacing import birthday_spacing_test
import random
def list_to_csv(lst):
    with open('./generated_numbers.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_NONE)
        wr.writerow(lst)

m = lcg(mod=13, a=1, c=5, x_0=1, n=2**20)
plt.hist(m,bins=13,color='steelblue' ,edgecolor='black', linewidth=1.2)
plt.title("LCG(mod=13,a=1,c=5,x_0=1)")
plt.show()
print(len(m))
# obliczamy liczebnosc pudelek do testu chi2

oczekiwane = (2**20)/13
obserwowane = [0 for _ in range(13)]

for i in m:
    obserwowane[i] += 1

#print(obserwowane)
#print(oczekiwane)

#p-wartosc dla jednego testu chi2
print(chi2_test(obserwowane, oczekiwane))

p_values = []
p_values2 = []

m2 = lcg(mod=13, a=1, c=5, x_0=1, n=1000*2**20)
for k in range(1000):
    m_temp = m2[k*2**20:(k+1)*2**20]
    oczekiwane = (2 ** 20) / 13
    obserwowane = [0 for _ in range(13)]
    for i in m_temp:
        obserwowane[i] += 1
    p_values.append(chi2_test(obserwowane, oczekiwane))
    m_temp = np.array(m_temp)
    p_values2.append(birthday_spacing_test(m_temp+1,13))

# second-level testing z uzyciem chi2
plt.hist(p_values)
plt.show()

# second-level testing z uzyciem birthday spacing test

plt.hist(p_values2)
plt.show()