import unittest
import day8

testdata = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

testdata_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

testdata_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def step_to_destination(current_steps, dir_sequence, map, start, end):
	instruction = int(dir_sequence[current_steps % len(dir_sequence)])
	current_steps += 1
	if (next_step := map[start][instruction]) != end:
		return step_to_destination(current_steps, dir_sequence, map, next_step, end)
	else:
		return current_steps


def part2(i_data):
	dir_sequence, map = day8.process_input(i_data)
	len_dir, counter = len(dir_sequence), 0
	vector = [elem for elem in map if elem.endswith("A")]
	while not all(elem.endswith("Z") for elem in vector):
		instruction = int(dir_sequence[counter % len_dir])
		counter += 1
		vector = [map[position][instruction] for position in vector]
	return counter

class MappingTestCase(unittest.TestCase):
	def test_data(self):
		self.assertEqual(day8.process_input(testdata)[0], "10")  # add assertion here
		self.assertEqual(day8.process_input(testdata)[1]["CCC"], ["ZZZ", "GGG"])  # add assertion here
		inputs = day8.process_input(testdata)
		self.assertEqual(step_to_destination(0, *inputs, "AAA", "ZZZ"), 2)
		self.assertEqual(day8.part1(*day8.process_input(testdata)), 2)
		inputs = day8.process_input(testdata_2)
		self.assertEqual(step_to_destination(0, *inputs, "AAA", "ZZZ"), 6)
		self.assertEqual(day8.part1(*day8.process_input(testdata_2)), 6)
		self.assertEqual(part2(testdata_3), 6)
		self.assertEqual(day8.part2t2(*day8.process_input(testdata_3)), 6)

if __name__ == '__main__':
	unittest.main()

#Solution1: RecursionError: maximum recursion depth exceeded
