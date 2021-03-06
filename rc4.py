import random
import random as rand
import matplotlib.pyplot as plt


def rc4(K: list, n, m=32):
    """
    RC4(m, K, n) PRNG of n numbers.
    :param m: Quantity of bytes
    :param K: Key : list
    :param n: Quantity of generated numbers
    :return: List of generated numbers
    """
    x = []
    S = [i for i in range(m)]
    L = len(K)
    j = 0
    for i in range(0, m):
        j = (j + S[i] + K[i % L]) % m
        S[i], S[j] = S[j], S[i]

    i, j = [0, 0]
    for _ in range(n):
        i = (i + 1) % m
        j = (j + 1) % m
        S[i], S[j] = S[j], S[i]
        x.append(S[(S[i] + S[j]) % m])
    return x


if __name__ == "__main__":
    x = rc4(m=32, K=[random.randint(a=0, b=31) for _ in range(17)], n=10000)
    print(x)
