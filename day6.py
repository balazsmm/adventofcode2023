from operator import mul
from functools import reduce


def racedata(input_data):
	return [[int(val) for val in line.split(":")[1].strip().split(" ") if val] for line in input_data.split("\n")]


def racedata2(input_data):
	return (int("".join([val for val in line.split(":")[1].strip().split(" ") if val])) for line in input_data.split("\n"))


def half_bf_eligible_charge_time_combos(max_time, record_distance):
	counter = 0
	for charge_time in range(1, int(max_time/2)+1):
		if (max_time - charge_time) * charge_time > record_distance:
			counter += 1
		
	return counter * 2 - (0 if max_time % 2 > 0 else 1)


def sum_eligible_combos_per_race(r_data):
	return reduce(mul, [half_bf_eligible_charge_time_combos(r_data[0][nr], r_data[1][nr]) for nr in range(0, len(r_data[0]))])


if __name__ == "__main__":
	with open("day6_input.txt", "r") as ifile:
		i_data = ifile.read().strip()
	print("Eligible combinations, part 1: {}, part 2: {}".format(sum_eligible_combos_per_race(racedata(i_data)), half_bf_eligible_charge_time_combos(*racedata2(i_data))))



