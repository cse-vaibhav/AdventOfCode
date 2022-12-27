from collections import Counter, defaultdict
from MyPackage import timeit


@timeit.timeit
def part1():
    with open("input.txt", "r") as f:
        pos = Counter(map(int, f.read().split(",")))

    min_fuel = 2135415646

    for x in range(max(pos)):
        fuel = 0
        for y in pos.keys():
            # print(x, y)
            fuel += abs(y - x) * pos[y]

        if fuel < min_fuel and fuel > 0:
            min_fuel = fuel
    print(min_fuel)


@timeit.timeit
def part2():
    def calc_fuel(steps):
        return steps * (steps + 1) // 2

    with open("input.txt", "r") as f:
        pos = Counter(map(int, f.read().split(",")))

    min_fuel = 2135415646

    for x in range(max(pos)):
        fuel = 0
        for y in pos.keys():
            # print(x, y)
            fuel += calc_fuel(abs(y - x)) * pos[y]
        if fuel < min_fuel:
            min_fuel = fuel
    print(min_fuel)


@timeit.timeit
def sum1(steps):
    return steps * (steps + 1) // 2


@timeit.timeit
def sum2(steps):
    return sum([x for x in range(1, steps + 1)])


sum1(11)
sum2(11)
