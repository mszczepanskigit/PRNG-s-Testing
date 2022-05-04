from bin_to_int import bin_to_int


def binary_to_mod8(txt):
    list_of_numbers = []
    with open(txt) as file:
        temp = []
        for line in file:
            for num in line:
                if num != "\n":
                    if len(temp) == 3:
                        x = int(temp[0])*100 + int(temp[1])*10 + int(temp[2])
                        x = bin_to_int(x)
                        list_of_numbers.append(x)
                        temp = []
                    temp.append(int(num))
    return list_of_numbers


if __name__ == "__main__":
    print(binary_to_mod8("e.txt"))