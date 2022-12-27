#!/usr/bin/env python3


def part1():
    score: int = 0
    with open("input", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            m: int = int(len(line) / 2)
            left = set(line[:m])
            right = set(line[m:])
            # print(left, right)
            intersect = left.intersection(right).pop()

            if intersect.islower():
                score += ord(intersect) - 96
            else:
                score += ord(intersect) - 64 + 26
        print(score)


def part2():
    score = 0
    with open("input", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            group = [set(lines[i + j].strip()) for j in range(3)]
            intersect = group[0].intersection(group[1]).intersection(group[2]).pop()

            if intersect.islower():
                score += ord(intersect) - 96
            else:
                score += ord(intersect) - 64 + 26
        print(score)


part2()
