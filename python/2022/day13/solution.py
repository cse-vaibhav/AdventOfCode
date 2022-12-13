#!/usr/bin/env python3

from rich import print
import json
from functools import cmp_to_key

def check(left, right, mix=False) -> int:

    # both are integers
    if isinstance(left, int) and isinstance(right, int):
        if (left == right):
            return 2;
        elif left < right:
            return 1
        else:
            return 0;

    # both are lists;
    elif isinstance(left, list) and isinstance(right, list):

        ln = len(left);
        rn = len(right);

        l = 0;
        r = 0;

        while l < ln or r < rn:

            if l >= ln:
                return 1
            elif r >= rn:
                return 0;

            resp = check(left[l], right[l]);
            if (resp != 2):
                return resp;
            l += 1;
            r += 1
        return 2;
    # one of them is list
    else:

        if isinstance(left, int):
            return check([left], right, True);
        elif isinstance(right, int):
            return check(left, [right], True)

    return False;


def compare1(packet):

    if isinstance(packet, list):
        return compare1(packet[0]) if packet else 0;
    return packet

with open("input", 'r') as f:
    lines = f.readlines();
    lineCount = len(lines)
    packets = []

    for i in range(0, lineCount):
        line = lines[i].strip();
        if line:
            packets.append(json.loads(line))

    # part 1
    ans1 = 0;
    packet = 1;
    for i in range(0,len(packets), 2):

        if check(packets[i], packets[i+1]):
            ans1 += packet;
        packet += 1;
    print(ans1)

    # part2
    packets.extend( [ [[6]], [[2]] ] )

    while True:
        swap = False;
        for i in range(len(packets)-1):
            if (check( packets[i], packets[i+1] ) == 0):
                packets[i], packets[i+1] = packets[i+1], packets[i];
                swap = True;
        if (swap == False):
            break;

    idx2 = packets.index( [[2]] ) + 1
    idx6 = packets.index( [[6]] ) + 1
    print(packets)
    print(idx2, idx6)
    print( idx2 * idx6 )
