#!/usr/bin/env python3

from rich import print
import numpy as np

sample = "input.txt"
real = "input"
larger_input = "larger-input.txt"

def move(point: tuple, d: str) -> tuple:
    if d == "R":
        return ( point[0] + 1, point[1] )
    elif d == "L":
        return ( point[0] - 1, point[1] )
    elif d == "U":
        return ( point[0], point[1] + 1 )
    elif d == "D":
        return ( point[0], point[1] - 1 )

    return point


def part1(filename):
    with open(filename, 'r') as f:
        lines = list(map(str.strip, f.readlines()));

        rows: int = 0;
        cols: int = 0;
        r: int = 0;
        u: int = 0;



        for line in lines:
            l = line.split();
            if (l[0] in ['U', 'D']):
                u = max(u, u + int(l[1]))
            else:
                r = max(r, r + int(l[1]))

        rows = r;
        cols = u;
        print(rows, cols);

        # grid = np.array(['.']*cols*rows).reshape( (rows,cols) );
        head: list = [rows-1, 0]
        tail: list = [rows-1, 0]
        count = 1

        visited: set[tuple] = set();

        for line in lines:
            l = line.split();
            steps = int(l[1])
            d = l[0]

            for i in range(steps):
                # move head
                x, y = head;
                # grid[x][y] = ".";
                head = move(head, d);
                # print(head)
                # grid[x][y] = "H";

                # move tail
                xdiff = head[0] - tail[0];
                ydiff = head[1] - tail[1];
                # print( (abs(xdiff), abs(ydiff)) )

                if (head == tail or (abs(xdiff) <= 1 and abs(ydiff) <= 1)):
                    pass;
                else:
                    x, y = tail;
                    # grid[x][y] = "#";
                    if ( tail not in visited ):
                        count += 1
                        visited.add( tail )

                    if (head[0] != tail[0] and tail[1] != head[1]):
                        # diagonal
                        tail = move(tail, "D" if xdiff > 0 else "U");
                        tail = move(tail, "R" if ydiff > 0 else "L");
                    else:
                        tail = move(tail, d);

                    x, y = tail;
                    # print(tail)
                    # grid[x][y] = "T";
                # print(grid)
        print(count)


def part2(filename, knots=2):
    with open(filename, 'r') as f:
        lines = list(map(str.strip, f.readlines()));

        rope: list[tuple] = []
        for i in range(knots):
            rope.append( (0, 0) )

        visited: set[tuple] = set();

        sign = lambda x : 0 if x == 0 else 1 if x > 0 else -1;

        for line in lines:
            l = line.split();
            steps = int(l[1])
            d = l[0]

            for i in range(steps):
                # move head
                rope[0] = move(rope[0], d);

                # move tails
                for i in range(1, knots):
                    xdiff = rope[i-1][0] - rope[i][0];
                    ydiff = rope[i-1][1] - rope[i][1];
                    dist = max(abs(xdiff), abs(ydiff));
                    # if (dist <= 1):
                    if (abs(xdiff) > 1 or abs(ydiff) > 1):
                        if (ydiff == 0):
                            rope[i] = ( rope[i][0] + sign(xdiff), rope[i][1] )
                        elif (xdiff == 0):
                            rope[i] = ( rope[i][0], rope[i][1] + sign(ydiff))
                        else:
                            rope[i] = ( rope[i][0] + sign(xdiff), rope[i][1] + sign(ydiff) )
                visited.add( rope[knots-1] )

        print(len(visited))
        # print(visited)

part2(sample, 10)
part2(larger_input, 10)
part2(real, 10)
