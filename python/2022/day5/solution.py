#!/usr/bin/env python3

# import math

stacks: dict = {}

def part1():
    with open("input", 'r') as f:
        # make stacks
        lines = f.readlines();
        ind: int = -1;
        for line in lines:
            ind += 1
            line = line.strip('\n');

            # if line is ' 1 2 ... n'
            if ("".join(line.split(' ')).isnumeric()):
                break;

            for j in range(len(line)):
                if (line[j] == '['):
                    # get stack number based on number of characters till this point
                    stack_no: int = j//4 + 1;
                    stacks.setdefault(stack_no, []);
                    stacks[stack_no].append(line[j+1]);

        # reverse the lists in stacks
        for k,v in stacks.items():
            stacks[k] = v[::-1]

        for i in range(ind+2, len(lines)):
            _line = lines[i].strip().split();
            count = int(_line[1]);
            _from = int(_line[3]);
            _to = int(_line[-1]);

            while (count != 0):
                stacks[_to].append(stacks[_from].pop());
                count -= 1

        # get top of all stacks
        top = []
        for k, v in stacks.items():
            top.append([k,v[-1]]);
        top.sort(key=lambda p : p[0]);
        print("".join( [ p[1] for p in top ] ))

        print(stacks)

def part2():
    with open("input", 'r') as f:
        # make stacks
        lines = f.readlines();
        ind: int = -1;
        for line in lines:
            ind += 1
            line = line.strip('\n');

            # if line is ' 1 2 ... n'
            if ("".join(line.split(' ')).isnumeric()):
                break;

            for j in range(len(line)):
                if (line[j] == '['):
                    # get stack number based on number of characters till this point
                    stack_no: int = j//4 + 1;
                    stacks.setdefault(stack_no, []);
                    stacks[stack_no].append(line[j+1]);

        # reverse the lists in stacks
        for k,v in stacks.items():
            stacks[k] = v[::-1]

        for i in range(ind+2, len(lines)):
            _line = lines[i].strip().split();
            count = int(_line[1]);
            _from = int(_line[3]);
            _to = int(_line[-1]);

            stacks[_to].extend(stacks[_from][-count:]);
            stacks[_from] = stacks[_from][:-count];

        # get top of all stacks
        top = []
        for k, v in stacks.items():
            if (len(v) == 0):
                continue;
            top.append([k,v[-1]]);
        top.sort(key=lambda p : p[0]);
        print("".join( [ p[1] for p in top ] ))

        print(stacks)

part2();
