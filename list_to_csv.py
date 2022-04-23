import csv
import random


def list_to_csv(lst):
    with open('./generated_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lst)


if __name__ == "__main__":
    list_to_csv([random.randint(0, 31)] for _ in range(10))
    with open('./generated_numbers.csv', 'r') as f:
        for i in f:
            print(i)
