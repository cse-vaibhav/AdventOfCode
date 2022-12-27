#!/usr/bin/env python3

from rich import print
from typing import Optional


def parseInput(filename: str) -> list[list[str]]:
    with open(filename, "r") as inp:
        lines = [list(line.strip()) for line in inp.readlines()]
        return lines


def findPath(
    grid: list[list[str]],
    visited: list[list[bool]],
    char: str,
    path: int,
    i: int,
    j: int,
    min_dist: int,
) -> int:

    if visited[i][j]:
        return min_dist

    rows: int = len(grid)
    cols: int = len(grid[0])

    if grid[i][j] == char:
        print(path, min_dist)
        return min(min_dist, path)

    visited[i][j] = True

    print(grid[i][j])
    maxList = [chr(ord(grid[i][j]) + 1), grid[i][j]]
    # up
    if i > 0 and grid[i - 1][j]:
        min_dist = min(
            min_dist, findPath(grid, visited, char, path + 1, i - 1, j, min_dist)
        )
    # down
    if i < rows - 1 and grid[i + 1][j]:
        min_dist = min(
            min_dist, findPath(grid, visited, char, path + 1, i + 1, j, min_dist)
        )
    # left
    if j > 0 and grid[i][j - 1] in [chr(ord(grid[i][j]) + 1), grid[i][j]]:
        min_dist = min(
            min_dist, findPath(grid, visited, char, path + 1, i, j - 1, min_dist)
        )
    # right
    if j < cols - 1 and grid[i][j + 1] in [chr(ord(grid[i][j]) + 1), grid[i][j]]:
        min_dist = min(
            min_dist, findPath(grid, visited, char, path + 1, i, j + 1, min_dist)
        )

    visited[i][j] = False

    return min_dist


def part1(filename: str):

    grid = parseInput(filename)
    rows: int = len(grid)
    cols: int = len(grid[0])

    visited: list[list[bool]] = [[False for j in range(cols)] for i in range(rows)]
    visited[0][0] = True

    print(findPath(grid, visited, "E", 0, 0, 1, 9999999))
    print(findPath(grid, visited, "E", 0, 1, 0, 9999999))
    return


part1("input.txt")
