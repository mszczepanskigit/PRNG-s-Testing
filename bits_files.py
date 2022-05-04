def bin_to_list(file_name):
    with open(file_name) as file:
        x = []
        for i in file:
            for j in i:
                if not j == '\n':
                    j = int(j)
                    if j in (0, 1):
                        x.append(j)
    return x


if __name__ == "__main__":
    e = bin_to_list("e.txt")
    print(e[1:5])