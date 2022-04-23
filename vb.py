def vb(x_0, n):
    """
    Visual Basic PRNG.
    :param x_0: Seed
    :param n: Quantity of generated numbers
    :return: List of generated numbers
    """
    x = [x_0]
    for i in range(1, n):
        x.append((1140671485 * x[i-1] + 12820163) % 2**24)
    return x


if __name__ == "__main__":
    print(vb(x_0=1, n=10))
