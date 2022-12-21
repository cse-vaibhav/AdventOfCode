
from rich import print
from typing import Self
from collections import defaultdict
import sys;

class Monkey:

	monkeys: defaultdict[str, Self] = defaultdict(Self)

	@classmethod
	def addMonkey(cls, monkey: Self):
		cls.monkeys[monkey.monkey] = monkey;

	@classmethod
	def getMonkey(cls, monkey: str) -> Self:
		return cls.monkeys[monkey];

	def __init__(self) -> None:
		self.monkey: str = "";
		self.number: int = 0;

		self.operator: str = "";
		self.left: str = "";
		self.right: str = "";

	def __repr__(self):
		return f"{self.monkey}: " + (f"{self.number}" if self.number != 0 else f"{self.left} {self.operator} {self.right}");

	def __hash__(self):
		return id(repr(self));

	def getNumber(self) -> int:
		if self.number != 0:
			return self.number;

		lo: int = Monkey.getMonkey(self.left).getNumber();
		ro: int = Monkey.getMonkey(self.right).getNumber();

		self.number = eval(f"int({lo} {self.operator} {ro})")
		return self.number;

class Part1:

	def parseInput(self):
		filename = sys.argv[1];
		with open(filename, 'r') as f:
			for line in f.readlines():
				monkey: Monkey = Monkey();
				l: list = line.split(': ');
				monkey.monkey = l[0];
				l = l[1].split();
				if len(l) == 1:
					monkey.number = int(l[0]);
				else:
					monkey.left = l[0];
					monkey.right = l[2];
					monkey.operator = l[1];
				Monkey.addMonkey(monkey);

	def solve(self):
		self.parseInput();
		print(Monkey.getMonkey('root').getNumber());

class Part2:
	def parseInput(self):
		filename = sys.argv[1];
		with open(filename, 'r') as f:
			for line in f.readlines():
				monkey: Monkey = Monkey();
				l: list = line.split(': ');
				monkey.monkey = l[0];
				l = l[1].split();
				if len(l) == 1:
					monkey.number = int(l[0]);
				else:
					monkey.left = l[0];
					monkey.right = l[2];
					monkey.operator = l[1];
				Monkey.addMonkey(monkey);

			root: Monkey = Monkey.getMonkey('root');
			root.operator = "==";
			# human: Monkey = Monkey.getMonkey('humn');
			# human.number *= 60;

	def findHuman(self, monkey: str, humanList: list) -> bool:
		if monkey == "humn":
			return True;

		m: Monkey = Monkey.getMonkey(monkey);

		if len(m.operator) == 0:
			return False;

		if self.findHuman(m.left, humanList):
			humanList.append(m.left);
			return True;

		if self.findHuman(m.right, humanList):
			humanList.append(m.right);
			return True;

		return False;

	def getHumanList(self) -> list:
		humanList: list = [];
		root: Monkey = Monkey.getMonkey('root');
		self.findHuman('root', humanList);
		return humanList;

	def solve(self):
		self.parseInput();
		humanList: list = self.getHumanList();
		opMap: dict[str, str] = {
			"*" : "/",
			"/" : "*",
			"+" : "-",
			"-" : "+"
		};

		root: Monkey = Monkey.getMonkey('root');
		queue: list = [root]
		while queue:
			front: Monkey = queue.pop(0);
			lm: Monkey = Monkey.getMonkey(front.left);
			rm: Monkey = Monkey.getMonkey(front.right);
			op: str = front.operator;
			if front.left in humanList:
				if op == '==':
					lm.number = rm.getNumber();
				else:
					lm.number = eval(f"int({front.getNumber()} {opMap[op]} {rm.getNumber()})")

				if front.left == "humn":
					print("ans", lm.getNumber());
					break;
				else:
					queue.append(lm);

			elif front.right in humanList:
				if op == "==":
					rm.number = lm.getNumber();
				elif op in ["+", "*"]:
					rm.number = eval(f"int({front.getNumber()} {opMap[op]} {lm.getNumber()})")
				else:
					rm.number = eval(f"int({lm.getNumber()} {op} {front.getNumber()})")

				if front.right == "humn":
					print("ans", rm.getNumber());
					break;
				else:
					queue.append(rm);

if __name__ == "__main__":
	Part2().solve();
	# print(Monkey.monkeys)

