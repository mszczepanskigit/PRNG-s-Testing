def glcg(mod, coeffs, x_0, n):
    """
    GLCG(mod, coeffs, x_0, n) PRNG of n numbers.
    :param mod: Modulo
    :param coeffs: List of coefficients [a_0, a_1, ..., a_{k-1}]
    :param x_0: List of seed [x_0, x_1, ..., x_{k-1}]
    :param n: Quantity of generated numbers
    :return: List of generated numbers
    """
    x = x_0   # generated list
    coeffs_len = len(coeffs)
    for i in range(1, n):
        temp_sum = 0
        for j in range(coeffs_len):
            temp_sum += coeffs[j] * x[-j-1]
        x.append(temp_sum % mod)
    return x


if __name__ == "__main__":
    print(glcg(mod=10, coeffs=[2, 3], x_0=[1, 3], n=10))
