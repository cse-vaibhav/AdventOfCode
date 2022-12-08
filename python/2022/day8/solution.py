#!/usr/bin/env python3

from rich import print
from functools import reduce

with open("input", 'r') as f:
    lines = f.readlines();
    forest: list[list[int]] = [];
    for line in lines:
        forest.append( list(map(int, line.strip())) );

    rows: int = len(forest);
    cols: int = len(forest[0]);

    visible_trees = 0;
    visible_trees += 2 * (rows + cols) - 4
    max_scenic_score = 0; # part 2

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            height = forest[row][col];

            v = [ max(forest[row][0:col]) < height,
                  max(forest[row][col+1:cols]) < height,
                  max( [ forest[r][col] for r in range(row) ]) < height,
                  max( [ forest[r][col] for r in range(row+1,rows) ]) < height
                 ]

            if (any(v)):
                visible_trees += 1

            tmp = 0;
            score = 1;

            for k in range(col-1, -1, -1):
                tmp += 1
                if (forest[row][k] >= height):
                    break;
            score *= tmp;
            tmp = 0;

            for k in range(col+1,cols):
                tmp += 1
                if (forest[row][k] >= height):
                    break;
            score *= tmp;
            tmp = 0;

            for k in range(row-1, -1, -1):
                tmp += 1
                if (forest[k][col] >= height):
                    break;
            score *= tmp;
            tmp = 0;

            for k in range(row+1, rows):
                tmp += 1
                if (forest[k][col] >= height):
                    break;
            score *= tmp;
            tmp = 0;

            max_scenic_score = max(score, max_scenic_score);

    # part1
    print(visible_trees)
    print(max_scenic_score)
