import sys
from math import log


def convertToSNAFU(num: int) -> str:
    conversionMap: dict = {4: "2", 3: "1", 2: "0", 1: "-", 0: "="}

    snafu: str = ""

    while num:
        # highest degree of five it is divisible by
        x = int(log(num, 5) // 1)
        # how many times is it divisible by that degree
        y = int(num // 5**x)
        print(x, y)
        snafu += conversionMap[y]
        num = int(num % 5**x)

    print(snafu)


def convertToDecimal(num: str) -> int:
    conversionMap: dict = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

    decimal: int = 0
    ind: int = len(num) - 1
    for x in num:
        dig: int = conversionMap[x]
        decimal += int(dig * (5**ind))
        ind -= 1
    return decimal


def part1():
    filename = sys.argv[1]
    with open(filename, "r") as f:
        ans: int = 0
        for snafu in f.readlines():
            num: int = convertToDecimal(snafu.strip())
            ans += num
    print(convertToSNAFU(ans))


if __name__ == "__main__":
    # part1()
    print(convertToSNAFU(int(sys.argv[1])))
