ranks1= ([1,1,1,1,1], [1,1,1,2], [1,2,2], [1,1,3], [2,3], [1,4], [5])
value_ranks1 = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
rule2_extra_vals = {1: ([1, 1, 1, 1],), 3: ([1, 1, 1], [1, 1, 2]), 4: ([2, 2],), 5: ([1, 1], [1, 3], [1, 2]), 6: ([1], [4], [2], [3], [None], [])}
rule2_ranks = {tuple(tpl):ranks1.index(tpl) for tpl in ranks1}
rule2_ranks.update({tuple(tpl):nr for nr in rule2_extra_vals for tpl in rule2_extra_vals[nr]})
rule2_value_ranks = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')

def process_data(data):
	return [((g := line.strip().split(" "))[0], int(g[1])) for line in data.strip().split("\n")]

def rank_tuple(hand):
		return ranks1.index(sorted([hand[0].count(letter) for letter in set(hand[0])])), sum(pow(13, nr_plc) * value_ranks1.index(nr_str) for nr_plc, nr_str in enumerate(hand[0][::-1]))

def rule2_rank_tuple(hand):
	return rule2_ranks.get(tuple(sorted([hand[0].count(letter) for letter in set(hand[0])-{"J"}]))), sum(pow(13, nr_plc) * rule2_value_ranks.index(nr_str) for nr_plc, nr_str in enumerate(hand[0][::-1]))

def total_winnings(cardset, ranking_function):
	card_order = sorted([(*ranking_function(hand), hand[1]) for hand in cardset])
	return sum((card_order.index(rkhand)+1) * rkhand[2] for rkhand in card_order)

if __name__ == "__main__":
	with open("day7_input.txt", "r") as ifile:
		inp = ifile.read().strip()
	print("Total winnings: {}, by ruleset 2: {}".format(total_winnings(process_data(inp), rank_tuple), total_winnings(process_data(inp), rule2_rank_tuple)))
