from collections import defaultdict
from functools import reduce
import rich
import sys
import time


class Elf:

    proposed: defaultdict = defaultdict(int)
    groups: list[tuple[str]] = [
        ("N", "NE", "NW"),
        ("S", "SE", "SW"),
        ("W", "NW", "SW"),
        ("E", "NE", "SE"),
    ]

    @classmethod
    def getProposed(cls, pos: tuple):
        return cls.proposed[pos]

    @classmethod
    def mark(cls, pos: tuple):
        cls.proposed[pos] += 1

    @classmethod
    def clear(cls):
        cls.proposed.clear()
        cls.groups.append(cls.groups.pop(0))

    def __init__(self):
        self.pos: tuple = (0, 0)
        self.proposed: tuple = (0, 0)

    def __repr__(self):
        return f"Elf at {self.pos}"

    def propose(self, grove: list[list[str]]):

        rows: int = len(grove)
        cols: int = len(grove[0])

        def checkBounds(pos: tuple) -> bool:
            x, y = pos
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            return True

        dirs: defaultdict = defaultdict(
            tuple,
            {
                "N": (-1, 0),
                "S": (1, 0),
                "E": (0, 1),
                "W": (0, -1),
                "NW": (-1, -1),
                "NE": (-1, 1),
                "SE": (1, 1),
                "SW": (1, -1),
            },
        )

        # check if elves are around
        x, y = self.pos
        # no one is around
        values: list = list(dirs.values())
        case2: bool = False
        for d in values:
            dest = (x + d[0], y + d[1])
            if checkBounds(dest) and grove[dest[0]][dest[1]] == "#":
                case2 = True
                self.proposed = self.pos
                break

        if case2:
            groups: list = Elf.groups.copy()

            for group in groups:
                occupied: bool = False
                for d in group:
                    x, y = self.pos
                    x = x + dirs[d][0]
                    y = y + dirs[d][1]
                    if checkBounds((x, y)):
                        if grove[x][y] == "#":
                            occupied = True
                            break
                if occupied:
                    continue

                x, y = self.pos
                first: tuple = dirs[group[0]]

                # check if out of boundary
                if not checkBounds(((x + first[0]), (y + first[1]))):
                    continue

                # propose that spot
                self.proposed = ((x + first[0]), (y + first[1]))
                break

        Elf.mark(self.proposed)

    def move(self, grove: list[list[str]]):
        if Elf.getProposed(self.proposed) > 1:
            return

        # rich.print(self.pos)
        # rich.print(self.proposed)

        x, y = self.pos
        grove[x][y] = "."
        self.pos = self.proposed

        x, y = self.pos
        grove[x][y] = "#"


class Part1:
    def __init__(self):
        self.grove: list = []
        self.rows: int = 0
        self.cols: int = 0
        self.parseInput()

    def parseInput(self):
        filename = sys.argv[1]
        with open(filename, "r") as f:
            for line in f.readlines():
                self.grove.append(list(line.strip()))

            self.rows = len(self.grove)
            self.cols = len(self.grove[0])
        # rich.print(self.grove)

    def writeGrove(self):
        with open("grove.txt", "w") as f:
            for row in self.grove:
                f.write("".join(row) + "\n")

    def solve(self):
        rounds: int = int(sys.argv[2])
        elves: list[Elf] = []

        minx: int = 9999
        miny: int = 9999
        maxx: int = -1
        maxy: int = -1

        # make elves
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grove[i][j] == "#":
                    elf: Elf = Elf()
                    elf.pos = (i, j)
                    elf.proposed = (i, j)
                    elves.append(elf)

        for r in range(rounds):
            print(Elf.groups)

            # first half
            for elf in elves:
                elf.propose(self.grove)

            # second half
            for elf in elves:
                elf.move(self.grove)

            # print("== Round ", r+1, " ==")
            # rich.print(self.grove)
            self.writeGrove()
            Elf.clear()

        for elf in elves:
            i, j = elf.pos
            minx = min(minx, i)
            miny = min(miny, j)
            maxx = max(maxx, i)
            maxy = max(maxy, j)

        print(minx, maxx, miny, maxy, len(elves))
        ans: int = (maxx - minx + 1) * (maxy - miny + 1) - len(elves)
        print(ans)


if __name__ == "__main__":
    part1 = Part1()
    part1.solve()
