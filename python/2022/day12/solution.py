#!/usr/bin/env python3

import sys
import time
import rich
from heapq import heappush, heappop

debug: bool = False
# debug: bool = True


def timeit(func):
    def func2(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("Time taken: ", end - start)
        return res

    return func2


def log(*args) -> None:
    if not debug:
        return
    rich.print(*args)


class Solution:
    def __init__(self):
        self.inputFile = sys.argv[1]
        self.visited = set()
        self.grid = self.parseInput()

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.max = int(1e30)
        self.min_steps: int = self.max
        self.nodes_roamed: int = 0

    @timeit
    def part1(self):
        self.start = self.solve("e")

        print()
        self.visited.remove(self.start)
        self.nodes_roamed = self.min_steps
        self.solve("E")

    @timeit
    def part2(self):
        # self.start = self.solve("e")
        # print()
        # self.visited.remove(self.start)
        # self.nodes_roamed = self.min_steps
        self.solve("E")
        return

    def parseInput(self) -> list[list[str]]:
        with open(self.inputFile, "r", encoding="utf-8") as inp:
            lines: list = []
            row: int = 0
            for line in inp.readlines():
                line = line.strip()
                lines.append(line)
                if line.count("S") != 0:
                    self.start = (row, line.index("S"))

                row += 1

            log(lines)
            log(self.start)
            return lines

    def getValidNeighbours(self, currPos: tuple) -> tuple:
        neighbours: set = {(1, 0), (-1, 0), (0, -1), (0, 1)}

        cx, cy = currPos
        curr_height = self.grid[cx][cy]
        if curr_height == "S":
            curr_height = "a"
        elif curr_height == "E":
            curr_height = "z"

        next_neighbours = []
        for n in neighbours:
            nx, ny = (cx + n[0], cy + n[1])

            if (
                not (0 <= nx < self.rows and 0 <= ny < self.cols)
                or (nx, ny) in self.visited
            ):
                continue

            neighbour_height = self.grid[nx][ny]
            if neighbour_height == "S":
                neighbour_height = "a"
            elif neighbour_height == "E":
                neighbour_height = "z"

            if ord(neighbour_height) - ord(curr_height) > 1:
                continue

            next_neighbours.append((nx, ny))

        return next_neighbours

    def solve(self, final_char: str):
        self.visited.clear()

        pq = [(0 if self.min_steps == self.max else self.min_steps, self.start)]
        self.min_steps = self.max
        while True:
            if not pq:
                break

            steps, node = heappop(pq)
            if node not in self.visited:
                self.nodes_roamed += 1
                self.visited.add(node)
                x, y = node
                if self.grid[x][y] == final_char:
                    self.min_steps = min(steps, self.min_steps)
                    print(f"Steps '{final_char}' : ", steps)
                    print(f"Nodes Roamed '{self.nodes_roamed}' : ", steps)
                    return (x, y)

                neighbours = self.getValidNeighbours(node)
                for neighbour in neighbours:
                    heappush(pq, (steps + 1, neighbour))


solution = Solution().part1()
