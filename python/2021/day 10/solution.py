import pprint
				
def isCorrupted(line: str) -> bool:
	brackets = {
				'(':')',
				')':'(',
				'[':']',
				']':'[',
				'{':'}',
				'}':'{',
				'<':'>',
				'>':'<',
				}
	opened_brackets = []
	corrupted = 0
	for ch in line:
		if ch in ['(', '[', '<', '{']:
			opened_brackets.append(ch)
		else:
			if opened_brackets[-1] != brackets[ch]:
				corrupted = 1
				break
			else:
				opened_brackets.pop()
	if corrupted == 1:
		return True
	else:
		return False

def part1():
	
	score = 0
	score_map = {
				')' : 3,
				']' : 57,
				'}' : 1197,
				'>' : 25137,
				}
	brackets = {
				'(':')',
				')':'(',
				'[':']',
				']':'[',
				'{':'}',
				'}':'{',
				'<':'>',
				'>':'<',
				}

	with open("input.txt", 'r') as f:
		lines = [x.strip('\n') for x in f.readlines()]
	
	opened_brackets = []
	wrong_brackets = []
	for line in lines:
		for ch in line:
			if ch in ['{', '[', '<', '(']:
				opened_brackets.append(ch)
			else:
				if opened_brackets[-1] != brackets[ch]:
					wrong_brackets.append(ch)
					break
				else:
					opened_brackets.pop()

	for bracket in wrong_brackets:
		score += score_map[bracket]
	print(score)

def part2():
	with open("input.txt", 'r') as f:
		lines = [x.strip('\n') for x in f.readlines()]
	scores = []
	brackets = {
				'(':')',
				')':'(',
				'[':']',
				']':'[',
				'{':'}',
				'}':'{',
				'<':'>',
				'>':'<',
				}
	score_map = {
				')':1,
				']':2,
				'}':3,
				'>':4,
				}
	for line in lines:
		score = 0
		opened_brackets = []
		if not isCorrupted(line):
			for ch in line:
				if ch in ['(', '[', '{', '<']:
					opened_brackets.append(ch)
				else: opened_brackets.pop()
		else: continue
		correction_brackets = [brackets[x] for x in opened_brackets[::-1]]
		for bracket in correction_brackets:
			score *= 5
			score += score_map[bracket]
		scores.append(score)
	scores.sort()
	median = scores[len(scores) // 2]
	print(median)

part2()