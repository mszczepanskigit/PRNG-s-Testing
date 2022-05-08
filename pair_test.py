from lcg import lcg
import random
from qcg import qcg
from chi2_new import chi2_test


def pair_test(lst):
    pairs = {}
    for i in range(len(lst) - 1):
        if not (lst[i], lst[i + 1]) in pairs:
            pairs[(lst[i], lst[i + 1])] = 1
        else:
            pairs[(lst[i], lst[i + 1])] += 1
    row = set()
    for key in pairs.keys():
        row.add(key[0])
    row = list(row)
    matrix = []
    for k in range(len(row)):
        row_elem1 = row[k]
        matrix.append([])
        for row_elem2 in row:
            matrix[k].append((row_elem1, row_elem2))
    matrix_of_values = []
    for i in range(len(matrix)):
        lst_row = matrix[i]
        matrix_of_values.append([])
        for tupl in lst_row:
            if pairs.get(tupl):
                matrix_of_values[i].append(pairs[tupl])
            else:
                matrix_of_values[i].append(0)
    observable_sum = []
    """for y in matrix:
        print(y)"""
    for y in matrix_of_values:
        # print(y)
        observable_sum.append(sum(y))
    p_val = chi2_test(obs=observable_sum, exp=[(len(lst) - 1) / len(matrix)] * len(matrix))
    return p_val


if __name__ == "__main__":
    # pair_test(qcg(m=11, a=1, b=2, c=3, x_0=7, n=100))
    # pair_test(lcg(mod=13, a=2, c=5, x_0=1, n=1000))
    from vb import vb
    from lcg import lcg
    from glcg import glcg
    from mt import mt
    from rc4 import rc4

    print(pair_test(glcg(mod=2**10, x_0=[1, 1, 1], n=2**16, coeffs=[3, 7, 68])))
