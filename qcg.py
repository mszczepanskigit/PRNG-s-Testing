def qcg(x_0, n, a, b, c, m=32):
    """
    Quadratic Congruent Generator (QCG) PRNG of n numbers.
    x(n) = a*x^2(n-1) + b*x(n-1) + c
    :param x_0: Seed
    :param n: Quantity of generated numbers
    :param a: Constant
    :param b: Constant
    :param c: Constant
    :param m: Modulo
    :return: List of generated numbers
    """
    x = [x_0]
    for i in range(1, n+1):
        x.append(((a*(x[i-1])**2 + b*(x[i-1]) + c) % m))
    return x


if __name__ == "__main__":
    print(qcg(x_0=3, n=10, a=2, b=3, c=0, m=32))
