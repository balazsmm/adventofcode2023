def numbers_with_positions(schem):
	line_size = len(schem[0])-1
	for ln_nr, ln_content in enumerate(schem):
		char_pos = 0
		while char_pos < line_size:
			if schem[ln_nr][char_pos].isnumeric():
				new_number = schem[ln_nr][char_pos]
				nr_start_pos = char_pos
				while char_pos < line_size:
					char_pos += 1
					if schem[ln_nr][char_pos].isnumeric():
						new_number += schem[ln_nr][char_pos]
					else:
						break
				if adjacent_text_contains_symbol((ln_nr, nr_start_pos), len(new_number), len(schem) - 1, line_size, schem):
					yield new_number

			char_pos += 1


def numbers_with_positions_next_to_star(star_position, schem):
	line_size = len(schem[0]) - 1
	for ln_nr, ln_content in enumerate(schem):
		char_pos = 0
		while char_pos < line_size:
			if schem[ln_nr][char_pos].isnumeric():
				new_number = schem[ln_nr][char_pos]
				nr_start_pos = char_pos
				while char_pos < line_size:
					char_pos += 1
					if schem[ln_nr][char_pos].isnumeric():
						new_number += schem[ln_nr][char_pos]
					else:
						break
				if number_adjacent_to_position(star_position, (ln_nr, nr_start_pos), len(new_number), len(schem) - 1, line_size):
					yield new_number
			
			char_pos += 1


def number_adjacent_to_position(star_position, num_position, num_length, maxrow, maxline):
	
	min_x, min_y = num_position[1] - 1 if num_position[1] >= 1 else 0, num_position[0] - 1 if num_position[0] >= 1 else 0
	max_x, max_y = num_position[1] + num_length if num_position[1] + num_length <= maxline else maxline, \
		num_position[0] + 1 if num_position[0] + 1 <= maxrow else maxrow
	return (min_y <= star_position[0] <= max_y) and (min_x <= star_position[1] <= max_x)


def adjacent_text_contains_symbol(pos, length, maxrow, maxline, schem):
	min_x, min_y = pos[1]-1 if pos[1] >= 1 else 0,  pos[0]-1 if pos[0] >= 1 else 0
	max_x, max_y = pos[1]+length+1 if pos[1]+length+1 <= maxline else maxline, pos[0]+1 if pos[0]+1 <= maxrow else maxrow
	return [schem[yv][xv] for yv in range(min_y, max_y+1) for xv in range(min_x, max_x)
									if (not schem[yv][xv].isnumeric() and schem[yv][xv] != ".")]


def adjacent_cube(pos, maxrow, maxline, schem):
	min_x, min_y = pos[1] - 3 if pos[1] >= 1 else 0, pos[0] - 1 if pos[0] >= 1 else 0
	max_x, max_y = pos[1] + 3 if pos[1] + 3 <= maxline else maxline, pos[0] + 1 if pos[0] + 1 <= maxrow else maxrow
	return (pos[0]-min_y, pos[1]-min_x), [schem[line][min_x:max_x+1] for line in range(min_y, max_y+1)]


def find_all_star_pos(schem):
	for line_nr, line in enumerate(schem):
		for char_nr, char in enumerate(line):
			if char == "*":
				yield line_nr, char_nr


def find_all_double_numbered_stars(schem):
	sum_of_gears = 0
	for star_pos in find_all_star_pos(schem):
		check_cube = adjacent_cube(star_pos, len(schem), len(schem[0]), schem)
		all_num = [nr for nr in numbers_with_positions_next_to_star(*check_cube)]
		if len(all_num) == 2:
			sum_of_gears += int(all_num[0])*int(all_num[1])
	
	return sum_of_gears


def all_parts_numbers(_schematic):
	return [int(nr) for nr in numbers_with_positions(_schematic)]


if __name__ == "__main__":
	with open("day3_input.txt", "r") as ifile:
		schematic = [line.strip() for line in ifile.readlines()]
	print("Part1: {}".format(sum(all_parts_numbers(schematic))))
	print(("Part2: {}".format(find_all_double_numbered_stars(schematic))))
