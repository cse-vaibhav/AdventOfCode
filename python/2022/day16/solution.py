
import re
import sys
# from rich import print
from pandas import DataFrame
import time

def timeit(func):
    def func2(*args, **kwargs):
        start = time.time();

        func(*args, **kwargs);

        end = time.time();
        print(end - start);
    return func2;

class Valve(object):

    valves = {};

    def __init__(self):
        self.flowRate: int= -1;
        self.valve: str;
        self.to: list[str] = [];
        self.opened: bool = False;

        # time since opened
        self.time: int = 0;

    def __hash__(self):
        return id(self);

    def __eq__(self, other):
        return id(self) == id(other);

    def __repr__(self):
        return f"Valve {self.valve} has flow rate={self.flowRate}; tunnels lead to valves {', '.join(self.to)}"

    def setFlowRate(self, flowRate: int) -> None:
        self.flowRate = flowRate;

    def setValve(self, valve: str) -> None:
        Valve.valves.setdefault(valve, None)
        self.valve = valve;
        Valve.valves[valve] = self;

    def addValve(self, valve: str) -> None:
        self.to.append(valve);

    @classmethod
    def getValve(cls, valve: str):
        return cls.valves[valve];

class Part1:

    def __init__(self):
        self.max_time: int = 30;
        self.max_pressure: int = -1;
        self.path: list[str] = [];
        self.paths: set[tuple[str]] = set();
        self.dp: DataFrame;

        return;

    def helper(self, time: int = 1, currValve: str="AA", currPressure: int=0) -> int:

        if time > 30:
            return 0;

        self.path.append(currValve);
        if tuple(self.path) in self.paths:
            self.path.pop();
            return 0;

        print(self.path)
        valve: Valve = Valve.getValve(currValve);
        currPressure += valve.flowRate * (self.max_time - time);
        opened_now: bool = False;
        if not valve.opened and valve.flowRate > 0:
            time += 1;
            opened_now = True;
            valve.opened = True;

        currPressure = max(currPressure, 
            max([self.helper(time+1, v, currPressure) for v in valve.to]))

        if opened_now:
            valve.opened = False;

        self.paths.add( tuple(self.path) )
        self.max_pressure = max(self.max_pressure, currPressure);
        self.path.pop();
            
        return currPressure;
  
    @timeit
    def solve(self):

        valves = [key for key in Valve.valves.keys()]
        valve_count:int = len(Valve.valves);
        opened_valves: int = 0;
        self.dp = DataFrame([ [-1 for x in range(0,self.max_time+1)] for y in range(valve_count)],
            columns=range(0,self.max_time+1),
            index=valves);

        print(self.helper());

        print(self.dp)
        print(self.max_pressure)

def parseInput():
    filename = sys.argv[1];
    reg = re.compile(r'Valve (.{2}) has .* rate=(\d+); .* valve(s)? (.*)')
    with open(filename, 'r') as f:
        lines = f.readlines();
        for line in lines:
            valve = Valve();
            inp = reg.findall(line.strip())[0]
            valve.setFlowRate( int(inp[1]) )
            valve.setValve(inp[0]);
            for to in inp[3].split(', '):
                valve.addValve(to);

if __name__ == "__main__":
    parseInput();
    Part1().solve();
            
    