#!/usr/bin/env python3

def part1():
    with open("input", 'r') as f:
        lines = f.readlines();
        cnt = 0
        for i in range(0, len(lines)):
            x = lines[i].strip().split(',')
            x[0] = x[0].split('-')
            x[1] = x[1].split('-')
            print(x)

            p1 = set([ y for y in range(int(x[0][0]), int(x[0][1])+1) ])
            p2 = set([ y for y in range(int(x[1][0]), int(x[1][1])+1) ])

            if len(p1-p2) == 0 or len(p2-p1) == 0:
                cnt += 1
        print(cnt)

def part2():
    with open("input", 'r') as f:
        lines = f.readlines();
        cnt = 0
        for i in range(0, len(lines)):
            x = lines[i].strip().split(',')
            x[0] = x[0].split('-')
            x[1] = x[1].split('-')
            print(x)

            p1 = set([ y for y in range(int(x[0][0]), int(x[0][1])+1) ])
            p2 = set([ y for y in range(int(x[1][0]), int(x[1][1])+1) ])

            if len(p1.intersection(p2)) != 0:
                cnt += 1
        print(cnt)


part2();
