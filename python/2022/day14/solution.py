#!/usr/bin/env python3

import sys
from rich import print

class Point:
    def __init__(self, x: int=0, y: int=0):
        self._x: int = x;
        self._y: int = y;

    def __eq__(self, other):
        # print(self, other)
        return self._x == other._x and self._y == other._y;

    def __str__(self):
        return f" Point {self._x} {self._y} "

    def getX(self) -> int:
        return self._x;

    def getY(self) -> int:
        return self._y;

    def setY(self, y: int) -> None:
        self._y = y;

    def setX(self, x: int) -> None:
        self._x = x;

class Rock(Point):
    def __init(self, x: int, y: int):
        super().__init__(x, y);

    def __str__(self):
        return f" Rock {self._x} {self._y} "

class Sand(Point):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y);
        self._rest: bool = False;

    def __str__(self):
        return f" Sand {self._x} {self._y} "

    def setRest(self, rest: bool) -> None:
        self._rest = rest;

    def getRest(self) -> bool:
        return self._rest;

class Cave:

    def __init__(self):
        self.source: Point = Point(500, 0);
        self.rocks: list[Rock] = []
        self.sand: list[Sand] = []
        self.bounds: list[tuple[int, int]] = []

    def check_bounds(self, x: int, y: int) -> bool:
        if x in self.bounds[0] or y in self.bounds[1]:
            return False
        return True;


    # part1
    def generateMap_part1(self) -> None:
        if (len(sys.argv) == 1):
            print(" No Input!! ");
            return None;

        minx: int = 99999;
        miny: int = 0;
        maxx: int = -1;
        maxy: int = -1;

        filename = sys.argv[1];
        with open(filename, 'r') as inp:
            lines = inp.readlines();
            for line in lines:
                l = line.strip().split(' -> ');
                # print(l)
                for i in range(1,len(l)):
                    x0, y0 = map(int, l[i-1].split(','))
                    x1, y1 = map(int, l[i].split(','))
                    minx = min([x1, x0, minx]);
                    maxx = max([x0, x1, maxx]);
                    maxy = max([y0, y1, maxy]);

                    # print(x0, y0, x1, y1)
                    if x0 == x1:
                        for y in range(min(y0,y1), max(y1,y0)+1):
                            rock = Rock( x0, y );
                            if (rock not in self.rocks):
                                self.rocks.append( rock );
                    elif y0 == y1:
                        for x in range(min(x0,x1), max(x0,x1)+1):
                            rock = Rock( x, y0 );
                            if (rock not in self.rocks):
                                self.rocks.append( rock );

        self.bounds = [ (minx-1,maxx+1), (miny-1, maxy+1) ];
    def dropSand_part1(self) -> bool:
        x, y = 500, 1;
        while (True):
            # down
            # print( x, y )
            if not self.check_bounds(x, y):
                return False;
            elif not Rock(x, y+1) in self.rocks and not Sand(x, y+1) in self.sand:
                y = y + 1;
            # slide left diagonally
            elif not Rock(x-1,y+1) in self.rocks and not Sand(x-1, y+1) in self.sand:
                x = x - 1;
                y = y + 1;
            # slide right diagonally
            elif not Rock(x+1, y+1) in self.rocks and not Sand(x+1,y+1) in self.sand:
                x = x + 1;
                y = y + 1;
            else:
                self.sand.append( Sand(x, y) );
                break;
        return True;

    def simulate_part1(self) -> None:
        units: int = 0;
        while (self.dropSand_part1()):
            units += 1;
        print(units);


    # part2
    def generateMap_part2(self) -> None:
        if (len(sys.argv) == 1):
            print(" No Input!! ");
            return None;

        minx: int = 99999;
        miny: int = 0;
        maxx: int = -1;
        maxy: int = -1;

        filename = sys.argv[1];
        with open(filename, 'r') as inp:
            lines = inp.readlines();
            for line in lines:
                l = line.strip().split(' -> ');
                # print(l)
                for i in range(1,len(l)):
                    x0, y0 = map(int, l[i-1].split(','))
                    x1, y1 = map(int, l[i].split(','))
                    maxy = max([y0, y1, maxy]);

                    # print(x0, y0, x1, y1)
                    if x0 == x1:
                        for y in range(min(y0,y1), max(y1,y0)+1):
                            rock = Rock( x0, y );
                            if (rock not in self.rocks):
                                self.rocks.append( rock );
                    elif y0 == y1:
                        for x in range(min(x0,x1), max(x0,x1)+1):
                            rock = Rock( x, y0 );
                            if (rock not in self.rocks):
                                self.rocks.append( rock );

        self.bounds = [ (miny-2, maxy+2) ];

    def dropSand_part2(self) -> bool:
        x, y = 500, 1;
        while (True):
            # down
            # print( x, y )
            if not self.check_bounds(x, y):
                return False;
            elif not Rock(x, y+1) in self.rocks and not Sand(x, y+1) in self.sand:
                y = y + 1;
            # slide left diagonally
            elif not Rock(x-1,y+1) in self.rocks and not Sand(x-1, y+1) in self.sand:
                x = x - 1;
                y = y + 1;
            # slide right diagonally
            elif not Rock(x+1, y+1) in self.rocks and not Sand(x+1,y+1) in self.sand:
                x = x + 1;
                y = y + 1;
            else:
                self.sand.append( Sand(x, y) );
                break;
        return True;

    def simulate_part2(self) -> None:
        units: int = 0;
        while (self.dropSand_part2()):
            units += 1;
        print(units);

cave = Cave();
cave.generateMap_part1();
cave.simulate_part1();
