def int_to_bit_on_list(lst):
    quant_of_bits = len(format(max(lst), "b"))
    new_lst = []
    for i in range(len(lst)):
        bits = list(format(lst[i], "b"))
        new_lst += ['0'] * (quant_of_bits - len(bits)) + bits
    return [int(num) for num in new_lst]


if __name__ == "__main__":
    print(int_to_bit_on_list([3, 17]))
    print(int_to_bit_on_list([]))
