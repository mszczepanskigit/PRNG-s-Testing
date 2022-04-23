def int_to_bit(number):
    return format(number, "b")


if __name__ == "__main__":
    print(list(int_to_bit(21)))