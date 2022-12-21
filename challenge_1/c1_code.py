# puzzle 1
def max_calories(path):
	calorie_lst = []

	with open(path, 'r') as f:
		sm, mx = 0, 0
		for line in f.readlines():
			if line == '\n':
				calorie_lst.append(sm)
				mx, sm = sm if sm > mx else mx, 0
			else:
				sm += eval(line)

	return mx

	# f.read().split('\n\n') built-ins O(n) time anyways... we can get more efficient control on our own
	# could also split into paragraphs & stop summing if > max, but likely not always more efficient (two O(n) processes)

# puzzle 2
def top_three_calories(path):
	max_lst = []

	with open(path, 'r') as f:
		sm = 0
		for line in f.readlines():
			if line == '\n':
				i, sml = min_helper(max_lst) if len(max_lst) else (0, 0)
				if len(max_lst) < 3 or (sm > sml and max_lst.pop(i)):
					max_lst.append(sm)
				sm = 0
			else:
				sm += eval(line)

	return sum(max_lst)

def min_helper(lst): #	A utility function that returns the minimum of a non-empty list and its index.
	assert len(lst)
	mn = 0
	for i in range(1, len(lst)):
		if lst[i] < lst[mn]:
			mn = i
	return (mn, lst[mn])




