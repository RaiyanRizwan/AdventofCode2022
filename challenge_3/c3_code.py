# puzzle 1
def sum_duplicate_priorities(path):

	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet += alphabet.upper()

	with open(path, 'r') as f:
		sm = 0
		for line in f.readlines():
			compartment_one, compartment_two = line[:len(line)//2], line[len(line)//2:]
			duplicates = filter(lambda item: item in compartment_two, compartment_one)
			priority = next(map(lambda duplicate: alphabet.index(duplicate) + 1, duplicates))
			sm += priority

	return sm

# puzzle 2
def sum_badge_priorities(path):

	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet += alphabet.upper()

	group_rucksacks = []
	badge_priorities = []

	with open(path, 'r') as f:
		for line in f.readlines():
			group_rucksacks.append(line)
			if len(group_rucksacks) == 3:
				badge = filter(lambda item: item in group_rucksacks[0] and item in group_rucksacks[1], group_rucksacks[2])
				badge_priorities.append(alphabet.index(next(badge)) + 1)
				group_rucksacks = []

	return sum(badge_priorities)

