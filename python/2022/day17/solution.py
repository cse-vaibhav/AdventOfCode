#!/usr/bin/env bash

import sys
from rich import print
from time import sleep
from tqdm import tqdm


class Rock:

    markedRocks: set = set()

    @classmethod
    def printChamber(cls, towerHeight: int):
        h = towerHeight + 5
        w = 7
        grid = [["." for _ in range(w)] for __ in range(h)]
        for key in cls.markedRocks:
            x, y = key
            grid[y][x] = "#"
        for y in range(h - 1, -1, -1):
            s = "".join(grid[y])
            print(str(y), s)
        print()

    @classmethod
    def addRock(cls, rock: tuple):
        cls.markedRocks.add(rock)

    @classmethod
    def checkRock(cls, rock: tuple):
        return rock in cls.markedRocks

    def __init__(self, rockType: int):
        self.type: int = rockType % 5
        self.rocks: list

        self.bottom: int
        self.left: int = 2

        self.getType()
        self.width: int = self.getRockWidth()

    def getType(self):
        rocks: list = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],  # horizontal line
            [(0, 1), (1, 1), (2, 1), (1, 0), (1, 2)],  # plus
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # reverse L
            [(0, 0), (0, 1), (0, 2), (0, 3)],  # vertical line
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # square
        ]

        self.rocks = rocks[self.type]

    def getRockWidth(self):
        width = 0
        for rock in self.rocks:
            width = max(width, rock[0])
        return width + 1

    def check_collision(self, towerBottom: int) -> bool:
        if self.bottom < towerBottom:
            return True

        if self.left < 0 or self.left + self.width > 7:
            return True

        for rock in self.rocks:
            if Rock.checkRock((rock[0] + self.left, rock[1] + self.bottom)):
                return True
        return False

    def move(self, direction: str):
        if direction == "<":
            self.left -= 1
        else:
            self.left += 1


class Part1:
    def __init__(self):
        self.input: str
        self.parseInput()

    def next_dir(self, curr: int) -> str:
        curr = curr % len(self.input)
        return self.input[curr]

    def next_rock(self, curr: int) -> Rock:
        return Rock(curr)

    def parseInput(self) -> None:
        with open(sys.argv[1], "r") as f:
            self.input = f.readline().strip()

    def solve(self):
        # rocks: int = 1000000000000;
        rocks: int = 2022

        towerHeight = 0
        towerBottom = 0
        jetDirection: int = 0

        for i in tqdm(range(rocks)):
            rock: Rock = self.next_rock(i)
            rock.bottom = towerHeight + 3
            rock.left = 2

            while True:
                direction: str = self.next_dir(jetDirection)
                jetDirection += 1

                rock.move(direction)
                if rock.check_collision(towerBottom):
                    rock.move("<" if direction == ">" else ">")

                rock.bottom -= 1
                if rock.check_collision(towerBottom):
                    rock.bottom += 1

                    for point in rock.rocks:
                        Rock.addRock((point[0] + rock.left, point[1] + rock.bottom))
                        towerHeight = max(towerHeight, point[1] + rock.bottom + 1)
                    break

        Rock.printChamber(towerHeight)
        print(towerHeight)


if __name__ == "__main__":
    part1 = Part1()
    part1.solve()
