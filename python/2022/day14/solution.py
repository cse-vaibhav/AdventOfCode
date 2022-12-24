#!/usr/bin/env python3

import sys
from rich import print
# import pandas as pd

class Point:
    def __init__(self, x: int=0, y: int=0):
        self._x: int = x;
        self._y: int = y;

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y;

    # def __cmd__(self, other):
    #     return

    # def __ne__(self, other):
    #     return hash(repr(self)) != hash(repr(other));

    def __str__(self):
        return f" Point {self._x} {self._y} ";

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

    def __str__(self):
        return f" Sand {self._x} {self._y} "

class Cave:

    def __init__(self):
        self.source: list= Point(500, 0);
        self.occupied: list[Point] = [];
        self.bounds: list[tuple[int, int]] = []

    # part1
    def check_bounds_part1(self, x: int, y: int) -> bool:
        if x in self.bounds[0] or y in self.bounds[1]:
            return False
        return True;

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
                for i in range(1,len(l)):
                    x0, y0 = map(int, l[i-1].split(','))
                    x1, y1 = map(int, l[i].split(','))
                    minx = min([x1, x0, minx]);
                    maxx = max([x0, x1, maxx]);
                    maxy = max([y0, y1, maxy]);

                    if x0 == x1:
                        for y in range(min(y0,y1), max(y1,y0)+1):
                            rock = Rock( x0, y );
                            if (rock not in self.occupied):
                                self.occupied.append( rock );
                    elif y0 == y1:
                        for x in range(min(x0,x1), max(x0,x1)+1):
                            rock = Rock( x, y0 );
                            if (rock not in self.occupied):
                                self.occupied.append( rock );

        self.bounds = [ (minx-1,maxx+1), (miny-1, maxy+1) ];
    def dropSand_part1(self) -> bool:
        x, y = 500, 0;
        while (True):
            # down
            if not self.check_bounds_part1(x, y):
                return False;
            elif not Rock(x, y+1) in self.occupied and not Sand(x, y+1) in self.occupied:
                y = y + 1;
            # slide left diagonally
            elif not Rock(x-1,y+1) in self.occupied and not Sand(x-1, y+1) in self.occupied:
                x = x - 1;
                y = y + 1;
            # slide right diagonally
            elif not Rock(x+1, y+1) in self.occupied and not Sand(x+1,y+1) in self.occupied:
                x = x + 1;
                y = y + 1;
            else:
                self.occupied.add( Sand(x, y) );
                break;
        return True;

    def simulate_part1(self) -> None:
        units: int = 0;
        while (self.dropSand_part1()):
            units += 1;

    # part2
    def check_bounds_part2(self, x: int, y: int) -> bool:

        if x < self.bounds[0][0]:
            bound = (x, self.bounds[0][1]);
            self.bounds[0] = bound
            rock = Rock(x, self.bounds[1][1]);
            if rock not in self.occupied:
                self.occupied.append(rock);

        elif x > self.bounds[0][1]:
            bound = (self.bounds[0][0], x);
            self.bounds[0] = bound
            rock = Rock(x, self.bounds[1][1]);
            if rock not in self.occupied:
                self.occupied.append(rock);


        if y in self.bounds[1]:
            return False
        return True;

    def generateMap_part2(self) -> None:
        if (len(sys.argv) == 1):
            print(" No Input!! ");
            return None;

        xmin: int = 99999;
        xmax: int = -1;
        ymax: int = -1;
        ymin: int = -1;

        filename = sys.argv[1];
        with open(filename, 'r') as inp:
            lines = inp.readlines();
            for line in lines:
                l = line.strip().split(' -> ');
                for i in range(1,len(l)):
                    x0, y0 = map(int, l[i-1].split(','))
                    x1, y1 = map(int, l[i].split(','))
                    ymax = max([y0, y1, ymax]);
                    xmax = max([x0, x1, xmax]);
                    xmin = min([x0, x1, xmin]);

                    if x0 == x1:
                        for y in range(min(y0,y1), max(y1,y0)+1):
                            rock = Rock( x0, y );
                            if (rock not in self.occupied):
                                self.occupied.append( rock );
                    elif y0 == y1:
                        for x in range(min(x0,x1), max(x0,x1)+1):
                            rock = Rock( x, y0 );
                            if (rock not in self.occupied):
                                self.occupied.append( rock );

            ymax += 2
            xmin *= 2;
            xmax *= 2
            for x in range(xmin, xmax):
                rock = Rock( x, ymax );
                if rock not in self.occupied:
                    self.occupied.append( rock );
            self.bounds = [ (xmin, xmax), (ymin, ymax) ];

    def dropSand_part2(self) -> bool:

        x = self.last_loc.getX();
        y = self.last_loc.getY();
        while True:
            if not self.check_bounds_part2(x, y):
                return False;

            # down
            if Point(x, y+1) not in self.occupied:
                y = y + 1;
            # slide left diagonally
            elif Point(x-1, y+1) not in self.occupied:
                x = x - 1;
                y = y + 1;
            # slide right diagonally
            elif Point(x+1,y+1) not in self.occupied:
                x = x + 1;
                y = y + 1;
            else:
                self.occupied.append( Point(x, y) );
                break;

        return True;

    def simulate_part2(self) -> None:
        units: int = 0;
        while (self.source not in self.occupied):
            self.last_loc: Point = Point(500, 0);
            if (self.dropSand_part2()):
                units += 1;
                print(units);
        print(units);

cave = Cave();
cave.generateMap_part2();
cave.simulate_part2();
