import numpy as np
import math


# Y wektor wylosowanych liczb od 1 do k, k to maksymalna liczba zbioru, ktory losujemy
def birthday_spacing_test(Y, k):
    n = len(Y)
    Y = np.array(Y)
    y_pos = np.sort(Y)
    spacings = y_pos[1:] - y_pos[0:-1]
    spacings = np.append(spacings, k - y_pos[-1] + y_pos[0])
    spacings_sort = np.sort(spacings)
    equal_spacings = 0
    equal_temp = [0, 0]
    for i in range(1, len(spacings_sort)):
        equal_temp[0] = spacings_sort[i - 1]
        equal_temp[1] = spacings_sort[i]
        if equal_temp[0] == equal_temp[1]:
            equal_spacings += 1
    lam = n ** 3 / (4 * k)
    j = np.array([i for i in range(equal_spacings)])
    new_arr = []
    for num in j:
        # calculate factorial of each item
        res = np.math.factorial(num)
        # add result in new_arr
        new_arr.append(res)
    new_arr = np.array(new_arr)
    p_val = 1 - sum(lam ** j / new_arr * math.exp(-lam))
    return p_val
