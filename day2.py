from functools import reduce
from operator import mul

limits = {"red":12, "green": 13, "blue":14}

def checkline(line):
	game, args = (parts := line.strip().split(":"))[0].split()[1], parts[1].split(";")
	return 0 if any(int(arg.split()[0])>limits[arg.split()[1].strip(",")] for argspart in args for arg in argspart.split(",")) else int(game)

def power_of_line_maxes(line):
	args, mxs = [arg for args in line.strip().split(":")[1].split(";") for arg in args.split(",")], {}
	for arg in args:
		if (value := int(arg.split()[0]))>mxs.get((color :=arg.split()[1].strip(",")), 0):
			mxs[color] = value
	return reduce(mul, mxs.values())

def sum_of_possible_games(gdata):
	return sum(checkline(data) for data in gdata)

def sum_of_powers_of_colors(gdata):
	return sum(power_of_line_maxes(data) for data in gdata)

if __name__ == "__main__":
	with open("day2_input.txt", "r") as ifile:
		idata = ifile.readlines()
		
	print("Sum of potential game numbers: {}".format(sum_of_possible_games(idata)))
	print("Sum of powers of colors: {}".format(sum_of_powers_of_colors(idata)))
