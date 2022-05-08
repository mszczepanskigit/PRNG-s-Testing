from freq_mon_test import freq_mon_test
from chi2_new import chi2_test
from mt import mt
from second_level import sec_l_test
from int_to_bit import int_to_bit_on_list

if __name__ == "__main__":
    p_values = []
    p_values2 = []
    N = 10000
    m2 = mt(x_0=1, a=0, b=7, n=1000*N)
    for k in range(1000):
        m_temp = m2[k * N:(k + 1) * N]
        oczekiwane = [N / 8] * 8
        obserwowane = [0]*8

        for i in m_temp:
            obserwowane[i] += 1
        p_values.append(chi2_test(obserwowane, oczekiwane))
        m_temp = int_to_bit_on_list(m_temp)
        p_values2.append(freq_mon_test(m_temp)[0])

    print(sec_l_test(p_values))
    print(sec_l_test(p_values2))