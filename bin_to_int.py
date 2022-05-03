def bin_to_int(binary):
    int_val, i, n = 0, 0, 0
    while binary != 0:
        a = binary % 10
        int_val = int_val + a * pow(2, i)
        binary = binary // 10
        i += 1
    return int_val


if __name__ == "__main__":
    print(bin_to_int(10101))
