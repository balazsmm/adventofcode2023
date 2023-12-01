import unittest
import day1
from day1prelim import analyze_numbers, analyze_numbers_with_overlap

testdata = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

checkdata = """12
38
12345
7"""

testdata2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

class CalibrationTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(day1.filter_numbers(testdata), checkdata.split("\n"))  # add assertion here
		self.assertEqual(day1.sum_calib_value(day1.filter_numbers(testdata)), 142)
		self.assertEqual(day1.sum_calib_value(analyze_numbers(testdata2)), 281)
		self.assertEqual(day1.sum_calib_value(analyze_numbers_with_overlap(testdata2)), 281)
		self.assertEqual(day1.sum_calib_value(day1.short_analyze_numbers_with_overlap(testdata2)), 281)


if __name__ == '__main__':
	print(day1.analyze_numbers(testdata2))
	unittest.main()
