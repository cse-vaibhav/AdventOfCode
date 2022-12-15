#!/usr/bin/env python3

import sys
import re
from rich import print
# import pandas as pd

def manhattan(p1: tuple, p2: tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);

class Sensor:

    def __init__(self, sensor: tuple, beacon: tuple):
        self.loc = sensor;
        self.beacon = beacon;
        self.man = manhattan(sensor, beacon);

    @classmethod
    def createEmptySensor(cls):
        return Sensor( (-1, -1), (-1, -1) );

    def isEmpty(self):
        return sensor[0] == -1;

    def check_beacon(self, beacon: tuple) -> bool:
        return self.beacon == beacon;

    def min_y(self) -> int:
        return self.loc[1] - self.man - 1;

    def max_y(self) -> int:
        return self.loc[1] + self.man + 1;

    def min_x(self) -> int:
        return self.loc[0] - self.man - 1;
    def max_x(self) -> int:
        return self.loc[0] + self.man + 1;

    def check_location(self, x, y) -> bool:

        distance: int = abs(x - self.loc[0]) + abs(y - self.loc[1]);
        if distance > self.man:
            return False;

        return distance <= self.man;

    def next_x(self, x, y) -> bool:
        # check if location is in sensor range
        if not self.check_location(x, y):
            return False;

        # return next absicca that falls outside range
        return self.loc[0] + self.man - abs(y - self.loc[1]) + 1;


class Part1:

    def __init__(self, row: int):
        self.row = row;

        self.sensors: set[Sensor] = set();
        self.beacons: set[tuple] = set();
        self.closest: dict[Sensor, tuple] = dict();
        self.parseInput();
        self.solve();

    def check_location(self, location):
        for sensor in self.sensors:
            beacon: bool = sensor.check_beacon(location);
            loc: bool = sensor.check_location(*location);
            if beacon:
                return False;
            if loc:
                return True;
        return False;

    def parseInput(self):
        filename = sys.argv[1]

        self.minx: int = 9999;
        self.miny: int = 9999;
        self.maxx: int = -1;
        self.maxy: int = -1;
        with open(filename, 'r') as f:
            reg = re.compile( r'x=(-?\d+), y=(-?\d+)' )
            lines = f.readlines();

            for line in lines:
                sensor, beacon = reg.findall(line.strip());

                sensor = (int(sensor[0]), int(sensor[1]))
                beacon = (int(beacon[0]), int(beacon[1]))

                self.sensors.add( Sensor(sensor, beacon) )
                self.beacons.add( beacon )

                # self.maxx = max( [self.maxx, sensor[0], beacon[0]] )
                # self.maxy = max( [self.maxy, sensor[1], beacon[1]] )
                # self.minx = min( [self.minx, sensor[0], beacon[0]] )
                # self.miny = min( [self.miny, sensor[1], beacon[1]] )

                self.closest.setdefault( sensor, (0,0) );
                self.closest[sensor] = beacon;
    def solve(self):
        xmin = 999999999999;
        xmax = -1;

        for sensor in self.sensors:
            xmin = min( xmin, sensor.min_x() );
            xmax = max( xmax, sensor.max_x() );

        print(xmin, xmax);

        locations = list(filter(self.check_location, [ (x, self.row) for x in range(xmin, xmax) ]));
        print(len(locations))

        return;


class Part2:

    def __init__(self):
        self.scan_size = int(sys.argv[2]);

        self.sensors: set[Sensor] = set();
        self.beacons: set[tuple] = set();
        self.closest: dict[Sensor, tuple] = dict();
        self.parseInput();
        self.solve();

    def check_location(self, location) -> Sensor:
        for sensor in self.sensors:
            beacon: bool = sensor.check_beacon(location);
            if beacon:
                return Sensor.createEmptySensor();

        for sensor in self.sensors:
            loc: bool = sensor.check_location(*location);
            if loc:
                return sensor;

        return Sensor.createEmptySensor();

    def check_location2(self, location) -> bool:
        for sensor in self.sensors:
            beacon: bool = sensor.check_beacon(location);
            loc: bool = sensor.check_location(*location);
            if beacon:
                return False;
            if loc:
                return True;
        return False;


    def parseInput(self):
        filename = sys.argv[1]

        # self.minx: int = 9999;
        # self.miny: int = 9999;
        # self.maxx: int = -1;
        # self.maxy: int = -1;
        with open(filename, 'r') as f:
            reg = re.compile( r'x=(-?\d+), y=(-?\d+)' )
            lines = f.readlines();

            for line in lines:
                sensor, beacon = reg.findall(line.strip());

                sensor = (int(sensor[0]), int(sensor[1]))
                beacon = (int(beacon[0]), int(beacon[1]))

                self.sensors.add( Sensor(sensor, beacon) )
                self.beacons.add( beacon )

                # self.maxx = max( [self.maxx, sensor[0], beacon[0]] )
                # self.maxy = max( [self.maxy, sensor[1], beacon[1]] )
                # self.minx = min( [self.minx, sensor[0], beacon[0]] )
                # self.miny = min( [self.miny, sensor[1], beacon[1]] )

                self.closest.setdefault( sensor, (0,0) );
                self.closest[sensor] = beacon;
    def solve(self):
        loop: int = 0;

        for y in range(0, self.scan_size+1):
            x = 0;
            while x < self.scan_size:
                updated: bool = False;
                loop += 1;
                sensor: Sensor = self.check_location( (x,y) )
                next_x: int = sensor.next_x(x, y);

                if next_x:
                    updated = True;
                    x = next_x;
                else:
                    x += 1;
                    continue;

                if x < self.scan_size:

                    currVal = self.check_location2( (x, y) );
                    if not currVal:
                        solution = ( x * 4000000 ) + y
                        print(solution)
                        exit();

if __name__ == "__main__":
    filename = sys.argv[1];
    part2 = Part2();
