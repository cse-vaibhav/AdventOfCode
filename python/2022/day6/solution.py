#!/usr/bin/env python3

from collections import Counter

# part 1
# unique_characters = 4
# part2
unique_characters = 14

with open("input.txt", 'r') as f:
    lines = f.readlines();
    for line in lines:
        line = line.strip();
        for i in range(len(line) - unique_characters - 1):
            substr = line[i:i+unique_characters];
            count = Counter(substr);
            if (all([True if x == 1 else False for y,x in count.items()])):
                print(i+unique_characters);
                break;
