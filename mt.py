import random


def mt(x_0, n, a, b):
    """
    Mersenne-Twister PRNG which is default PRNG in Python.
    Without whole implementation.
    :param x_0: Seed
    :param n: Quantity of generated numbers
    :param a, b: Interval of generated integers
    :return: List of generated integers from interval <a,b>
    """
    random.seed(x_0)
    x = [x_0]
    for _ in range(n-1):
        x.append(random.randint(a, b))
    return x


if __name__ == "__main__":
    print(mt(x_0=1, n=10, a=0, b=31))

