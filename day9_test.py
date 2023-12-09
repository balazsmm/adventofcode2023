import unittest

import day9
from day9 import process_data, dfx_stack, sum_of_extrapolates


testdata = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def extrapolates(data):
	for line in data:
		yield line


class OasisTestCase(unittest.TestCase):
	def test_dfx_data(self):
		self.assertEqual(process_data(testdata)[1][1:4], [3, 6, 10])
		self.assertEqual([dfx_stack(line) for line in extrapolates(process_data(testdata))], [18, 28, 68])
		self.assertEqual(sum_of_extrapolates(day9.process_data(testdata)), 114)
		self.assertEqual(sum_of_extrapolates(day9.process_data(testdata), historic=True), 2)
	# for dataline in day9.process_data(testdata):
	# 	dfx_stack(dataline)


if __name__ == '__main__':
	unittest.main()
