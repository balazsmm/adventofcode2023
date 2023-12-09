import unittest
from day6 import racedata, racedata2, sum_eligible_combos_per_race

test_data = """Time:      7  15   30
Distance:  9  40  200"""

def bf_eligible_charge_time_combos(max_time, record_distance):
	counter = 0
	for charge_time in range(1, max_time):
		if (max_time - charge_time) * charge_time > record_distance:
			counter += 1
	return counter


class BoatRaceTestCase(unittest.TestCase):
	def test_race_data(self):
		self.assertEqual(racedata(test_data), [[7, 15, 30], [9, 40, 200]])
		self.assertEqual(sum_eligible_combos_per_race(racedata(test_data)), 288)
		self.assertEqual(racedata2(test_data), (71530, 940200))


if __name__ == '__main__':
	unittest.main()
