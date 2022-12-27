#!/usr/bin/env python3

import numpy as np
import rich


class Register:
    def __init__(self, filename):
        self._ins: list = []
        self.register: int = 1
        self._file = filename
        self.last_ins: int = 0

        self.strengths: list[tuple[int, int]] = [(-1, 0), (1, 0)]

    def __add(self, instructionType, val=0) -> None:
        self._ins.append((2 if instructionType == "addx" else 1, val))

    def __fill(self):
        with open(self._file, "r") as inp:
            lines = inp.readlines()
            for line in lines:
                l = line.strip().split()
                if l[0] == "noop":
                    self.__add(l[0])
                else:
                    self.__add(l[0], int(l[1]))

    def _reset(self):
        self.register = 1
        self._ins.clear()
        self.__fill()

    def simulateCycle(self, cycles) -> int:
        n: int = len(self.strengths)
        # increase the size of dp
        if n < cycles:
            self.strengths.extend([(-1, -1)] * (cycles - n + 1))
        elif self.strengths[cycles] != -1:
            return self.strengths[cycles]

        strength: int = 0
        # self.register = self.strengths[n-1];
        # s: int = self.last_ins;
        # print(cycles, n-1, self.register);
        # set to initial state
        self._reset()

        j: int = 0
        for i in range(1, cycles):
            item = self._ins[j]
            item = (item[0] - 1, item[1])

            if item[0] == 0:
                self.register += item[1]
                j += 1
            else:
                self._ins[j] = item

            strength = int(i * self.register)
            self.strengths[i] = (strength, j)

        strength = int(cycles * self.register)
        self.strengths[cycles] = (strength, j)
        return strength

    def draw(self):

        self.__fill()
        screen = np.array(["."] * 6 * 40).reshape((6, 40))
        sprite: list = [(0, 0), (0, 1), (0, 2)]
        crt: int = 0
        loc = (0, 0)
        reg: int = 1
        j: int = 0
        row: int = 0
        for i in range(len(self._ins)):

            # register value
            delay = self._ins[j][0]

            sprite = [(row, reg + 1), (row, reg), (row, reg - 1)]  # get sprite location

            # draw crt
            for _ in range(delay):
                screen[loc] = "#" if loc in sprite else "."
                crt += 1
                if crt % 40 == 0:
                    row += 1
                # print(reg, sprite, loc)
                loc = (int(crt / 40), (crt) % 40)
            reg += self._ins[j][1]
            j += 1

        print("\n".join(["".join(r) for r in screen]))


def part1(filename):
    register = Register(filename)
    cycleList = [20, 60, 100, 140, 180, 220]
    signalsStrengths = list(map(register.simulateCycle, cycleList))
    print(signalsStrengths)
    print(sum(signalsStrengths))


def part2(filename):
    register = Register(filename)
    register.draw()


part2("larger-input.txt")
part2("input")
