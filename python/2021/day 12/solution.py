import numpy as np
import collections
import pprint


class Cave:
    pass


class Cave(Cave):
    caves = collections.defaultdict(Cave)
    paths = set()

    def __init__(self, cave_name):

        self.name = cave_name
        self.small = True if self.name.islower() else False
        self.connectedCaves = np.array([])

        Cave.caves[self.name] = self

    @classmethod
    def reset(cls):
        cls.caves.clear()
        cls.start_cave = None
        cls.end_cave = None
        cls.paths.clear()
        cls.special_cave = None

    @classmethod
    def addAdjacentCave(cls, caves):
        cave1, cave2 = caves
        c1 = cls.caves[cave1]
        c2 = cls.caves[cave2]
        c1.connectedCaves = np.append(c1.connectedCaves, c2)
        c2.connectedCaves = np.append(c2.connectedCaves, c1)

    @classmethod
    def findPaths(cls, curr_path, have_time=False):
        c = cls.caves[curr_path[-1]]
        for cave in c.connectedCaves:
            cond = not cave.name in curr_path
            if have_time:
                visits = collections.Counter(filter(str.islower, curr_path))
                is_cave_visited_twice = max(visits.values()) == 2
                cond = cave.name != "start" and (
                    not cave.small
                    or cave.small
                    and (not is_cave_visited_twice or not cave.name in curr_path)
                )
            else:
                cond = not cave.small or (cave.small and not cave.name in curr_path)

            if cave.name == "end":
                cls.paths.add(",".join(curr_path + ["end"]))

            elif cond:
                p = cls.findPaths(curr_path + [cave.name], have_time)
                if p != None:
                    cls.paths.add(",".join(p))


def part1():
    lines = len(open("input.txt", "r").readlines())
    with open("input.txt", "r") as f:
        for _ in range(lines):
            args = f.readline().strip("\n").split("-")
            for arg in args:
                if arg not in Cave.caves.keys():
                    Cave(arg)
            Cave.addAdjacentCave(args)

    Cave.findPaths(["start"])
    return len(Cave.paths)


def part2():
    lines = len(open("input.txt", "r").readlines())
    with open("input.txt", "r") as f:
        for _ in range(lines):
            args = f.readline().strip("\n").split("-")
            for arg in args:
                if arg not in Cave.caves.keys():
                    Cave(arg)
            Cave.addAdjacentCave(args)

    Cave.findPaths(["start"], have_time=True)
    return len(Cave.paths)


if __name__ == "__main__":

    print(f"Part1 : {part1()}")
    Cave.reset()
    print(f"Part2 : {part2()}")
