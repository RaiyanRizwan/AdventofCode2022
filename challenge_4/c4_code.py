# puzzle 1
def redundant_pairs(path):
	with open(path, 'r') as f:
		redundant = 0
		for line in f.readlines():
			# XXX-XXX,XXX-XXX --> (min, max) (min, max)

			one, two = rec_eval(list(map(lambda e: e.split('-'), line.split(',')))) # thanks Kian Agahi for remining me .split() exists

			if one[0] <= two[0] and one[1] >= two[1] or one[0] >= two[0] and one[1] <= two[1]:
				redundant += 1

		return redundant

def rec_eval(nested_lst): 
	if not isinstance(nested_lst, list):
		return eval(nested_lst)
	return [rec_eval(lst) for lst in nested_lst]

# puzzle 2
def overlapping_pairs(path):
	with open(path, 'r') as f:
		redundant = 0
		for line in f.readlines():
			# XXX-XXX,XXX-XXX --> (min, max) (min, max)

			one, two = rec_eval(list(map(lambda e: e.split('-'), line.split(','))))

			if not (one[0] > two[1] or two[0] > one[1]):
				redundant += 1
 
		return redundant
