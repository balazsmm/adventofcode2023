import unittest
from day5 import Almanac

testdata = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class AlmanacTestCase(unittest.TestCase):
	def test_almanac_data(self):
		almanac = Almanac(testdata)
		self.assertEqual(almanac.seeds, [79, 14, 55, 13])
		self.assertEqual(almanac.mappings[0], [[50, 98, 2], [52, 50, 48]])
		self.assertEqual(almanac.mappings[5], [[0, 69, 1], [1, 0, 69]])
		final_record =  almanac.map_record_to_next_stage(almanac.seeds, -1)
		self.assertEqual(min(final_record), 35)
		self.assertEqual(almanac.map_value_to_next_stage(79, -1), 82)
		self.assertEqual(almanac.map_value_to_next_stage(55, -1), 86)
		test_seed_range = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
		self.assertEqual([n for n in almanac.convert_seeds_to_seed_range_gen()], test_seed_range)
		self.assertEqual(almanac.minimum_of_seed_ranges_mappings(), 46)


if __name__ == '__main__':
	unittest.main()
