#!/usr/bin/env python3

from rich import print
from collections import defaultdict
from typing import List

with open("input", "r") as f:
    lines: List[str] = f.readlines();
    threshold: int = 100_000;

    # folders: dict[str, list[str]] = dict()
    # files: dict[str, list[tuple[int,str]]] = dict()
    sizes: defaultdict = defaultdict(int)

    currPath: list = []
    for cmd in lines:
        cmd = cmd.strip();
        l = tuple(cmd.split())
        match l:
            case ('$', 'cd', '..'):
                currPath.pop();
            case ('$', 'cd', p):
                sizes.setdefault(p, 0);
                currPath.append(p);
            case ('$', 'ls'):
                pass
            case ('dir', p):
                pass
            case (s, f):
                sizes[tuple(currPath)] += int(s)
                path = currPath[: -1];
                while path:
                    sizes[tuple(path)] += int(s)
                    path.pop()
                pass
            case _:
                break

    print( sum( [ d for d in sizes.values() if d <= threshold ] ) )

    space_needed = 70_000_000 - sizes[("/",)]
    print( min([ s for s in sizes.values() if s + space_needed >= 30_000_000]) )
