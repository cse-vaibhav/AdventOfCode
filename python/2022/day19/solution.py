
import sys
import re
import rich
from tqdm import tqdm

class Part1:

	def __init__(self):
		self.time: int = 24;

		self.robotsMade: list = ['ore'];
		self.robots: list = ['ore', 'clay', 'obsidian', 'geode'];
		self.resources: dict[str,list] = { resource : [0] for resource in self.robots };
		self.maxNeeded: dict[str,list] = { resource : [0] for resource in self.robots };
		self.robotCost: dict[str,list] = { robot : [ (0,0) ] for robot in self.robots };

		self.blueprints: int = 0;
		self.quality: int = 0;

		self.parseInput();

	def parseInput(self):
		filename = sys.argv[1];
		with open(filename, 'r') as f:
			lines = f.readlines();
			for line in lines:
				line = line.strip();
				inp = list(map(int, re.findall(r'(\d+)', line)))

				self.blueprints += 1;
				self.robotCost['ore'].append(inp[1]);
				self.robotCost['clay'].append(inp[2]);
				self.robotCost['obsidian'].append( (inp[3], inp[4]) );
				self.robotCost['geode'].append( (inp[5], inp[6]) );

				self.maxNeeded['ore'].append( max([inp[2], inp[3], inp[5]]) );
				self.maxNeeded['clay'].append( inp[4] );
				self.maxNeeded['obsidian'].append( inp[6] );

				for robot in self.robots:
					self.resources[robot].append(0);

	def collectResource(self, blueprint: int):
		for robot in set(self.robotsMade):
			cnt: int = self.robotsMade.count(robot);
			self.resources[robot][blueprint] += cnt;
			rich.print(robot, " += ", cnt, f"({self.resources[robot][blueprint]})")

	def makeRobot(self, blueprint: int) -> str:

		t = self.time;

		xclay = self.robotsMade.count('clay');
		yclay = self.resources['clay'][blueprint];
		zclay = self.maxNeeded['clay'][blueprint];
		checkClay: bool = xclay + yclay < zclay
		# checkClay: bool = xclay < zclay;

		xobsidian = self.robotsMade.count('obsidian');
		yobsidian = self.resources['obsidian'][blueprint];
		zobsidian = self.maxNeeded['obsidian'][blueprint];
		checkObsidian: bool = xobsidian + yobsidian < zobsidian;
		# checkObsidian: bool = xobsidian < zobsidian;
		
		xore = self.robotsMade.count('ore');
		yore = self.resources['ore'][blueprint];
		zore = self.maxNeeded['ore'][blueprint];
		checkOre: bool = xore + yore < zore;

		# geode bot
		if self.resources['ore'][blueprint] >= self.robotCost['geode'][blueprint][0] and self.resources['obsidian'][blueprint] >= self.robotCost['geode'][blueprint][1]:
			self.resources['ore'][blueprint] -= self.robotCost['geode'][blueprint][0];
			self.resources['obsidian'][blueprint] -= self.robotCost['geode'][blueprint][1];
			return 'geode'

		# obsidian bot
		elif checkObsidian and self.resources['ore'][blueprint] >= self.robotCost['obsidian'][blueprint][0] and  self.resources['clay'][blueprint] >= self.robotCost['obsidian'][blueprint][1]:
			self.resources['ore'][blueprint] -= self.robotCost['obsidian'][blueprint][0];
			self.resources['clay'][blueprint] -= self.robotCost['obsidian'][blueprint][1];
			return 'obsidian'

		# clay bot
		elif checkClay and self.resources['ore'][blueprint] >= self.robotCost['clay'][blueprint]:
			self.resources['ore'][blueprint] -= self.robotCost['clay'][blueprint];
			return 'clay'

		# ore bot
		elif checkOre and self.resources['ore'][blueprint] >= self.robotCost['ore'][blueprint]:
			self.resources['ore'][blueprint] -= self.robotCost['ore'][blueprint];
			return 'ore'

		return "";

	def solve(self):

		# for blueprint in range(1, self.blueprints + 1):
		blueprint: int = 1;
		self.robotsMade = ['ore'];

		for _ in range(1, self.time + 1):
			rich.print("== Minute ", _ , " ==")
			robot = self.makeRobot(blueprint);
			self.collectResource(blueprint);
			if len(robot) != 0:
				self.robotsMade.append(robot);
				rich.print(robot, "robot made", f"({self.robotsMade.count(robot)})");
			print();

		quality = blueprint * self.resources['geode'][blueprint]
		self.quality += quality;
		print(quality)

		rich.print(self.quality)
		rich.print(self.resources)
		rich.print(self.maxNeeded)
		rich.print(self.robotsMade)
		rich.print(self.robotCost)

if __name__ == "__main__":
	Part1().solve();

