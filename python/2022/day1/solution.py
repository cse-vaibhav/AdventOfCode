
def comp(p1: list, p2: list) -> bool:
    return p1[1] > p2[1]

with open("input", 'r') as inp:
    elf = 1;
    lines = inp.readlines();
    pairs: list = []
    s: int = 0
    for line in lines:
        if (len(line.strip()) == 0):
            pairs.append([elf, s])
            elf += 1;
            s = 0
            continue;
        s += int(line.strip());


    pairs.sort(key=lambda p: p[1], reverse=True);
    print(sum([p[1] for p in pairs[:3]]))
