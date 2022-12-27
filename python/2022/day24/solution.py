import rich
import sys


class Part1:
    def __init__(self):
        self.grid: list[list[str]] = []
        self.blizzards: list = []

        self.rows: int = 0
        self.cols: int = 0
        self.min_time: int = 99999

        self.parseInput()

        self.start: tuple = [0, 1]
        self.end: tuple = (self.rows - 1, self.cols - 2)
        self.solve(tuple(self.start), 0)
        print(self.min_time)

    def parseInput(self):
        filename = sys.argv[1]
        with open(filename, "r") as f:
            self.rows = 0
            for line in f.readlines():
                self.grid.append(list(line.strip()))

                i: int = 0
                for ch in self.grid[-1]:
                    if ch in [">", "<", "^", "v"]:
                        self.blizzards.append((self.rows, i))
                    i += 1

                self.rows += 1

            self.cols = len(self.grid[0])

    def moveBlizzards(self, reverse: bool = False) -> None:

        dirs: dict = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

        reverseDir: dict = {"<": ">", ">": "<", "^": "v", "v": "^"}
        rows: int = self.rows
        cols: int = self.cols
        for i in range(len(self.blizzards)):
            x, y = self.blizzards[i]

            blizzardDir: str = self.grid[x][y]

            d: tuple = dirs[blizzardDir]
            if reverse:
                d = dirs[reverseDir[blizzardDir]]

            self.grid[x][y] = "."
            self.blizzards[i] = ((x + d[0]) % rows, (y + d[1]) % cols)
            if self.grid[x][y] == "#":
                self.blizzards[i] = ((x + d[0]) % rows, (y + d[1]) % cols)

            x, y = self.blizzards[i]
            self.grid[x][y] = blizzardDir

    def solve(self, pos: tuple[int, int], time: int) -> None:

        # definitely not the minimum
        if time > self.min_time:
            return

        # reached destination
        if pos == self.end:
            self.min_time = min(self.min_time, time)
            return

        self.moveBlizzards()
        #           N       E       W        S
        for d in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            x, y = (pos[0] + d[0]) % self.rows, (pos[1] + d[1]) % self.cols
            if self.grid[x][y] in ["<", ">", "^", "v"]:
                continue
            self.solve((x, y), time + 1)
        self.solve(pos, time + 1)
        self.moveBlizzards(reverse=True)


if __name__ == "__main__":
    part1 = Part1()
