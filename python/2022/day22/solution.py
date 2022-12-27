from rich import print
import sys


def writeGrid(grid: list[list[str]]) -> None:
    with open("grid.txt", "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")


def parseInput():
    filename = sys.argv[1]
    grid: list[list[str]] = []
    max_cols: int = -1
    with open(filename, "r") as f:
        lines: list[str] = f.readlines()
        for line in lines:
            if len(line.strip()) == 0:
                break
            max_cols = max(max_cols, len(line.rstrip()))

        for line in lines:
            if len(line.strip()) == 0:
                break
            grid.append(list(line.rstrip().ljust(max_cols)))
    print(len(grid), len(grid[0]))
    return grid, lines[-1].strip()


def parseDirections(dirs: str):
    n: int = len(dirs)
    d: list = []
    num: int = 0
    for i in range(n):
        if dirs[i] in ["R", "L"]:
            d.append(int(dirs[num:i]))
            d.append(dirs[i])
            num = i + 1
        elif i == n - 1:
            d.append(int(dirs[num : i + 1]))
    return d


def rotate(currDir: str, d: str) -> str:
    if currDir == ">" and d == "R":
        return "v"
    elif currDir == ">" and d == "L":
        return "^"
    elif currDir == "<" and d == "R":
        return "^"
    elif currDir == "<" and d == "L":
        return "v"
    elif currDir == "^" and d == "R":
        return ">"
    elif currDir == "^" and d == "L":
        return "<"
    elif currDir == "v" and d == "R":
        return "<"
    elif currDir == "v" and d == "L":
        return ">"


def changePos(grid: list[list[str]], currPos: tuple, di: str) -> tuple[tuple, bool]:
    directionMap: dict = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    d: tuple = directionMap[di]
    rows: int = len(grid)
    cols: int = len(grid[0])
    blocked: bool = False

    x, y = currPos
    new_pos: tuple = ((x + d[0]) % rows, (y + d[1]) % cols)
    x, y = new_pos
    # print(rows, x, cols, y, di)
    if grid[x][y] == "#":
        blocked = True
        return currPos, blocked

    elif grid[x][y] == " " or x >= rows or y >= cols or x < 0 or y < 0:
        x, y = currPos
        # going right
        if di == ">":
            if "." in grid[x] and "#" in grid[x]:
                y = min(grid[x].index("."), grid[x].index("#"))
            elif "#" not in grid[x]:
                y = grid[x].index(".")

            if grid[x][y] == "#":
                blocked = True
                y = currPos[1]
        # going left
        elif di == "<":

            if "." in grid[x] and "#" in grid[x]:
                y = max(
                    cols - grid[x][::-1].index(".") - 1,
                    cols - grid[x][::-1].index("#") - 1,
                )
            elif "#" not in grid[x]:
                y = cols - grid[x][::-1].index(".") - 1

            if grid[x][y] == "#":
                blocked = True
                y = currPos[1]
        # going down
        elif di == "v":
            for i in range(rows):
                if grid[i][y] == ".":
                    x = i
            if x == currPos[0]:
                blocked = True
        # going up
        else:
            for i in range(rows - 1, -1, -1):
                if grid[i][y] == ".":
                    x = i
            if x == currPos[0]:
                blocked = True
        new_pos = (x, y)

    return new_pos, blocked


def part1():

    faceMap: dict = {">": 0, "v": 1, "<": 2, "^": 3}

    grid, dirs = parseInput()
    dirs = parseDirections(dirs)
    pos: tuple = (0, min(grid[0].index("."), grid[0].index("#")))
    face: str = ">"
    grid[0][pos[1]] = face

    for d in dirs:
        # move
        if d not in ["R", "L"]:
            for _ in range(d):
                pos, blocked = changePos(grid, pos, face)
                if blocked:
                    break
                x, y = pos
                grid[x][y] = face
        else:
            face = rotate(face, d)
            grid[x][y] = face

    x, y = pos
    x += 1
    y += 1
    print(1000 * x + 4 * y + faceMap[face])
    writeGrid(grid)


part1()
