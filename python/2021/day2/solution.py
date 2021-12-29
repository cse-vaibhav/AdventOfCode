
def part1():
	with open('input.txt', 'r') as f:
		horizontal_pos = 0
		depth = 0

		data = [x.strip('\n') for x in f.readlines()]

	for ins in data:
		cmd = ins.split()[0]
		steps = int(ins.split()[1])
		if cmd == 'forward':
			horizontal_pos += steps

		elif cmd == 'down':
			depth += steps
		elif cmd == 'up':
			depth -= steps

	res = depth*horizontal_pos
	return res

def part2():
	with open('input.txt', 'r') as f:
		with open('input.txt', 'r') as f:
			horizontal_pos = 0
			depth = 0
			aim = 0
			data = [x.strip('\n') for x in f.readlines()]

	for ins in data:
		cmd = ins.split()[0]
		x = int(ins.split()[1])

		if cmd == 'forward':
			horizontal_pos += x
			depth += aim*x
		elif cmd == 'down':
			aim += x

		elif cmd == "up":
			aim -= x

	res = horizontal_pos * depth

	return res




if __name__ == "__main__":
	print(f"{part1.__name__} : {part1()}")
	print(f"{part2.__name__} : {part2()}")