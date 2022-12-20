# puzzle 1
def score_calc(path):
	opp_mvs = ['A', 'B', 'C']
	my_mvs = ['X', 'Y', 'Z']
	pts_dic = {"X": 1, "Y": 2, "Z": 3}
	win_lst = ['CX', 'BZ', 'AY'] # X defeats C, Z defeats B, Y defeats A
	tie_lst = ['AX', 'BY', 'CZ']

	moves_dic = {f'{mv1 + mv2}': pts_dic[mv2] + 6 * (
		mv1 + mv2 in win_lst and 1 or mv1 + mv2 in tie_lst and 0.5 or 0) for mv1 in opp_mvs for mv2 in my_mvs}

	score = 0
	with open(path, 'r') as f:
		for line in f.readlines():
			score += moves_dic[line[0] + line[2]]

	return round(score)

# puzzle 2
def updated_strategy_calc(path):
	outc = ['X', 'Y', 'Z']
	pts_dic = {"A": 1, "B": 2, "C": 3}
	win_dic = {'A':'B', 'B':'C', 'C':'A'}
	lose_dic = dict(zip(win_dic.values(), win_dic.keys()))
	tie_dic = dict(zip(win_dic.keys(), win_dic.keys()))
	outc_dic = {0: lose_dic, 1: tie_dic, 2: win_dic}

	score = 0
	with open(path, 'r') as f:
		for line in f.readlines():
			opp_mv = line[0]
			outcome = line[2]
			score += pts_dic[outc_dic[outc.index(outcome)][opp_mv]] + 3 * outc.index(outcome)

	return score

# note - Yes, these solutions are perhaps unecessarily complex. However, I feel they're cool.