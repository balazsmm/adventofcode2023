import unittest
import day7

ranks= ([1,1,1,1,1], [1,1,1,2], [1,2,2], [1,1,3], [2,3], [1,4], [5])
value_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

testdata = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def evaluate_hand(hand):
	return ranks.index(sorted([hand.count(letter) for letter in set(hand)]))

def rank_by_number_sequence(hand):
	return sum(pow(13, nr_plc) * value_ranks.index(nr_str) for nr_plc, nr_str in enumerate(hand[::-1]))

class MyTestCase(unittest.TestCase):
	def test_processing(self):
		self.assertEqual(day7.process_data(testdata), [("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)])
		self.assertEqual(evaluate_hand("T55J5"), 3)
		self.assertEqual(evaluate_hand("KK677"), 2)
		self.assertTrue(rank_by_number_sequence("32T3K") < rank_by_number_sequence("KK677"))
		self.assertTrue(rank_by_number_sequence("KTJJT") < rank_by_number_sequence("KK677"))
	
	def test_cardset(self):
		self.assertEqual(day7.total_winnings(day7.process_data(testdata), day7.rank_tuple), 6440)
		self.assertEqual(day7.total_winnings(day7.process_data(testdata), day7.rule2_rank_tuple), 5905)



if __name__ == '__main__':
	unittest.main()
