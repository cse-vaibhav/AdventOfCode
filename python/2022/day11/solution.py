#!/usr/bin/env python3

from rich import print
from typing import Optional
import sys
from math import lcm
from functools import reduce


class Monkey(object):

    master_divisor: int
    count: int = 0

    def __init__(self) -> None:
        self.id = Monkey.count
        self.inspections: int = 0
        self._items: list[int] = []
        self._test_number: int
        self.right_operand: str
        self.operator: str

        self.true: int
        self.false: int

        Monkey.count += 1

    # set the right-operand in the operation
    def set_operand(self, operand: str) -> None:
        self.right_operand = operand

    # set the operator in the operation
    def set_operator(self, operator: str) -> None:
        self.operator = operator

    # set the test to perform
    def set_test_number(self, test: int) -> None:
        self._test_number = test

    # set monkey to throw to if true
    def set_true(self, monkey: int):
        self.true = monkey

    # set monkey to throw to if false
    def set_false(self, monkey: int):
        self.false = monkey

    # return items held by monkey
    def getItems(self) -> list[int]:
        return self._items

    def setItems(self, items: list[int]) -> None:
        self._items = items

    # do the operation
    def doOperation(self, item: int, factor=1) -> int:
        if item == 0:
            return item
        ro = item if self.right_operand == "old" else int(self.right_operand)
        if self.operator == "*":
            # return ( item * ro ) // factor
            return ((item * ro) // factor) % Monkey.master_divisor
        else:
            # return ( item + ro ) // factor
            return ((item + ro) // factor) % Monkey.master_divisor

    # 9699690

    # test the items
    def test(self, item: int) -> bool:
        return (item % self._test_number) == 0

    def throwItem(self, factor=1) -> tuple[int, int]:
        item = self._items.pop(0)
        item = self.doOperation(item, factor)

        # throw to monkey 1 else monkey 2
        self.inspections += 1
        return (item, self.true) if self.test(item) else (item, self.false)

    # monkey obj to string conversion
    def __str__(self) -> str:
        return f"""
        Monkey {self.id}:
        Starting items: {", ".join(map(str, self._items))}
        Operation: new = old {self.operator} {self.right_operand}
        Test: divisible by {self._test_number}
            If true: throw to monkey  {self.true}
            If false : throw to monkey {self.false}"""

    @classmethod
    def parse_monkeys(cls, filename) -> list:
        with open(filename, "r") as f:
            lines = map(str.strip, f.readlines())

            monkeyList: list = []
            tmp_monkey: Monkey
            div_test: list[int] = []
            for line in lines:
                if line.startswith("Monkey"):
                    tmp_monkey = Monkey()
                elif line.startswith("Starting"):
                    l = line.split()[2:]
                    l = list(map(lambda x: x.strip(","), l))
                    l = list(map(int, l))
                    tmp_monkey.setItems(l)

                elif line.startswith("Operation"):
                    l = line.split()[4:]
                    tmp_monkey.set_operator(l[0])
                    tmp_monkey.set_operand(l[1])
                elif line.startswith("Test"):
                    l = line.split()
                    tmp_monkey.set_test_number(int(l[-1]))
                    div_test.append(int(l[-1]))
                elif line.startswith("If true"):
                    l = line.split()
                    tmp_monkey.set_true(int(l[-1]))
                elif line.startswith("If false"):
                    l = line.split()
                    tmp_monkey.set_false(int(l[-1]))
                    monkeyList.append(tmp_monkey)

            cls.master_divisor = reduce(lcm, div_test)
            print(cls.master_divisor)
            return monkeyList

    @classmethod
    def simulate_part1(cls, monkeys: list[object], rounds: int) -> None:
        for _ in range(rounds):
            n = len(monkeys)
            for i in range(n):
                monkey = monkeys[i]
                m = len(monkey.getItems())
                for _ in range(m):
                    item, to = monkey.throwItem(3)
                    monkeys[to]._items.append(item)
        inspections = []
        for monkey in monkeys:
            print(monkey.id, monkey.inspections)
            inspections.append(monkey.inspections)
        inspections.sort()
        print(inspections[-2] * inspections[-1])

    @classmethod
    def simulate_part2(cls, monkeys: list[object], rounds: int) -> None:
        for _ in range(rounds):
            # iterate over monkeys
            for monkey in monkeys:
                while monkey._items:
                    item, to = monkey.throwItem(1)
                    monkeys[to]._items.append(item)

        inspections = []
        for monkey in monkeys:
            print(monkey.id, monkey.inspections)
            inspections.append(monkey.inspections)
        inspections.sort()
        print(inspections[-2] * inspections[-1])


# monkeys = Monkey.parse_monkeys("input");
monkeys = Monkey.parse_monkeys("input")
Monkey.simulate_part2(monkeys, 10000)
