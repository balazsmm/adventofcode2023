import unittest
import day2

test1_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()



class Day2_test(unittest.TestCase):
	def test_sums(self):
		self.assertEqual(day2.checkline("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), 2)
		self.assertEqual(day2.checkline("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), 0)
		self.assertEqual(day2.sum_of_possible_games(test1_data), 8)
		self.assertEqual(day2.sum_of_powers_of_colors(test1_data), 2286)


if __name__ == '__main__':
	unittest.main()
