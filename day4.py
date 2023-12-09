def process_input(input):
	return [[(s := textline.split(":")[1].split("|"))[0].split(), s[1].split()] for textline in input.split("\n")]


def sum_of_2_power_counts(data):
	return sum(pow(2, len(list(set(dataline[0]).intersection(set(dataline[1]))))-1) for dataline in data if len(list(set(dataline[0]).intersection(set(dataline[1])))) > 0)


def all_cards(data):
	all_cards = process_input(data)
	return process_slice(0, len(all_cards), all_cards)


def all_matching_numbers(line):
	return len(list(set(line[0]).intersection(set(line[1]))))


def process_slice(start, stop, data):
	cntr = 0
	for i in range(start, stop):
		if (plus_range := all_matching_numbers(data[i])) > 0:
			cntr += process_slice(i+1, i+plus_range+1, data)
		cntr += 1
	return cntr


if __name__ == "__main__":
	with open("day4_input.txt", "r") as ifile:
		i = ifile.read().strip()
	print("Part 1: {}, part2: {}".format(sum_of_2_power_counts(process_input(i)), all_cards(i)))
