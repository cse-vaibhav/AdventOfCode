
def part1():
	with open('input.txt', 'r') as f:
		numbers = list(map(int, [x.strip('\n') for x in f.readlines()]))
		count = 0
		num = numbers[0]
		for x in numbers[1:]:
			if x > num:
				num = x
				count += 1
			else:
				num = x
		print(count)

def part2():
	with open('input.txt', 'r') as f:
		numbers = list(map(int, [x.strip('\n') for x in f.readlines()]))

	count = 0
	prev_sum = sum([numbers[i] for i in range(3)])
	for x in range(1,len(numbers)-2):
		s = sum([numbers[x+i] for i in range(3)])
		if s > prev_sum:
			prev_sum = s
			count += 1
		else:
			prev_sum = s

	print(count)

part2()

