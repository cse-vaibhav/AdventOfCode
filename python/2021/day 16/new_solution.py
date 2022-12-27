#!/usr/bin/env python3

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet:
    def __init__(self, packet):
        self.pkt = self.toBinary(packet)
        self.version = int(packet[:3], 2)
        self.id = int(packet[3:6], 2)
        self.isLiteral = self.id == 4

    def toBinary(self, packet):
        return "".join(map(lambda x: hex_map[x], packet))
