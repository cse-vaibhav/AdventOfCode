import pprint
import collections
import pandas as pd
import numpy as np


def check_oxygen(oxygen_rating, row):
    for x in range(len(oxygen_rating)):
        if int(oxygen_rating[x]) != row[i]:
            return False
    return True


def part1():
    with open("input.txt", "r") as f:
        data = [s.strip("\n") for s in f.readlines()]
    gamma_rate = ""
    epsilon_rate = ""
    bits = collections.defaultdict(pd.Series)
    for i in range(len(data[0])):
        l = []
        for line in data:
            l.append(int(line[i]))
        bits[i] = pd.Series(l)
    for i in bits.keys():
        most_common = bits[i].mode()[0]
        least_common = 1 if (most_common == 0) else 0
        gamma_rate += str(most_common)
        epsilon_rate += str(least_common)
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)


def part2():

    rows = len(open("input.txt", "r").read().split("\n"))
    cols = len(open("input.txt", "r").read().split("\n")[0])
    matrix = np.array([0] * rows * cols).reshape((rows, cols))
    with open("input.txt", "r") as f:
        for i in range(rows):
            line = list(map(int, list(f.readline().strip("\n"))))
            matrix[i] = line

    oxygen_rating = ""
    co2_rating = ""

    # oxygen generator rating
    for row in matrix.transpose():
        new_matrix = np.array([])
        one_count = row.tolist().count(1)
        zero_count = len(row) - one_count
        most_common = 0 if (zero_count > one_count) else 1


part2()
