def lcg(mod, a, c, x_0, n):
    """
    LCG(mod, a, c, x_0, n) PRNG of n numbers.
    :param mod: Modulo
    :param a: Coefficient near x_{n-1}
    :param c: Last term in computing
    :param x_0: Seed
    :param n: Quantity of generated numbers
    :return: List of generated numbers
    """
    x = [x_0]
    for i in range(1, n):
        x.append((a * x[i-1] + c) % mod)
    return x


if __name__ == "__main__":
    print(lcg(mod=13, a=1, c=5, x_0=1, n=20))
