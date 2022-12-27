import collections


def part1():
    with open("input.txt", "r") as f:
        cnt = collections.defaultdict(int)
        for i in range(10):
            ps = f.readline().split(" -> ")
            p1 = tuple(map(int, ps[0].split(",")))
            p2 = tuple(map(int, ps[1].split(",")))

            if p1[0] == p2[0]:
                high = max(p1[1], p2[1])
                low = min(p1[1], p2[1])
                for y in range(low, high + 1):
                    point = (p1[0], y)
                    cnt[point] += 1

            elif p1[1] == p2[1]:
                high = max(p1[0], p2[0])
                low = min(p1[0], p2[0])
                for x in range(low, high + 1):
                    point = (x, p1[1])
                    cnt[point] += 1
        print(sum([1 for i in cnt if cnt[i] > 1]))


def part2():
    with open("input.txt", "r") as f:
        cnt = collections.defaultdict(int)
        for i in range(500):
            ps = f.readline().split(" -> ")
            p1 = tuple(map(int, ps[0].split(",")))
            p2 = tuple(map(int, ps[1].split(",")))

            if p1[0] == p2[0]:
                high = max(p1[1], p2[1])
                low = min(p1[1], p2[1])
                for y in range(low, high + 1):
                    point = (p1[0], y)
                    cnt[point] += 1
            elif p1[1] == p2[1]:
                high = max(p1[0], p2[0])
                low = min(p1[0], p2[0])
                for x in range(low, high + 1):
                    point = (x, p1[1])
                    cnt[point] += 1
            else:
                x_high = max(p1[0], p2[0])
                y_high = max(p1[1], p2[1])
                x_low = min(p1[0], p2[0])
                y_low = min(p1[1], p2[1])

                slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                on_line = (
                    lambda point: True
                    if (y == (slope * (x - p1[0]) + p1[1]))
                    else False
                )

                for x in range(x_low, x_high + 1):
                    for y in range(y_low, y_high + 1):
                        point = (x, y)
                        if on_line(point):
                            cnt[point] += 1

        print(sum([1 for i in cnt if cnt[i] > 1]))


part2()
