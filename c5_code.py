# PUZZLE 1 - find which crates are at the top of each stack after all movements are complete

def top_crates(path):

	with open(path, 'r') as f:

		lines = f.readlines()
		crates = [[]]*(len(lines[0])//4)

		l = 0
		while lines[l].strip(): # crate description
			line, c = lines[l], 1

			while c < len(line):
				crate = line[c].strip()
				if crate:
					crates[(c-1)//4] = [crate] + crates[(c-1)//4]
				c += 4

			l += 1

		for line in lines[l+1:]: # moves
			line = line.split(' ')
			quantity, loc, new_loc = eval(line[1]), eval(line[3]) - 1, eval(line[5]) - 1
			for q in range(quantity):
				crates[new_loc].append(crates[loc].pop())

		return ''.join([crate[-1] for crate in crates])

"""
input looks like:

        [Q] [B]         [H]        
    [F] [W] [D] [Q]     [S]        
    [D] [C] [N] [S] [G] [F]        
    [R] [D] [L] [C] [N] [Q]     [R]
[V] [W] [L] [M] [P] [S] [M]     [M]
[J] [B] [F] [P] [B] [B] [P] [F] [F]
[B] [V] [G] [J] [N] [D] [B] [L] [V]
[D] [P] [R] [W] [H] [R] [Z] [W] [S]
 1   2   3   4   5   6   7   8   9 

move 1 from 4 to 1
move 2 from 4 to 8
move 5 from 9 to 6

We need to capture the crates into lists...which will make it easier to systematically move around items. 
XXX[space]XXX[space]XXX --> every index is 4 characters wide... create a list of len(line)/4 nested lists
"""

# PUZZLE 2 - find which crates are at the top of each stack, but multiple crates are now moved at once instead of one at a time.

def top_crates(path):

	with open(path, 'r') as f:

		lines = f.readlines()
		crates = [[]]*(len(lines[0])//4)

		l = 0
		while lines[l].strip(): # crate description
			line, c = lines[l], 1

			while c < len(line):
				crate = line[c].strip()
				if crate:
					crates[(c-1)//4] = [crate] + crates[(c-1)//4]
				c += 4

			l += 1

		for line in lines[l+1:]: # moves
			line = line.split(' ')
			quantity, loc, new_loc = eval(line[1]), eval(line[3]) - 1, eval(line[5]) - 1
			crates[new_loc].extend(crates[loc][-quantity:])
			crates[loc] = crates[loc][:-quantity]

		return ''.join([crate[-1] for crate in crates])



