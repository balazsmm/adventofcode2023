import unittest
from day3 import adjacent_text_contains_symbol, all_parts_numbers,\
		find_all_star_pos, adjacent_cube, find_all_double_numbered_stars

testdata1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")


class PartNumberCase(unittest.TestCase):
	def test_adjacency(self):
		self.assertTrue(adjacent_text_contains_symbol((0, 0), 3, 9, 9, testdata1))  # add assertion here
		self.assertFalse(adjacent_text_contains_symbol((0, 5), 3, 9, 9, testdata1))  # add assertion here
		self.assertTrue(adjacent_text_contains_symbol((2, 6), 3, 9, 9, testdata1))  # add assertion here
		self.assertEqual(all_parts_numbers(testdata1), [467, 35, 633, 617, 592, 755, 664, 598])
		self.assertEqual(sum(all_parts_numbers(testdata1)), 4361)
		self.assertEqual(list(find_all_star_pos(testdata1)), [(1, 3), (4, 3), (8, 5)])
		self.assertEqual(adjacent_cube((4, 3), 9, 9, testdata1)[1], ["......#", "617*...", ".....+."])
		self.assertEqual(adjacent_cube((1, 3), 9, 9, testdata1)[1], ["467..11", "...*...", "..35..6"])
		self.assertEqual(find_all_double_numbered_stars(testdata1), 467835)


if __name__ == '__main__':
	unittest.main()
