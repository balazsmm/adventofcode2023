limits, pgn, pwc = {"red": 12, "green": 13, "blue": 14}, 0, 0
with open("day2_input.txt", "r") as ifile: idata = ifile.readlines();
for data in idata:
	game, args, mxs = *((parts := data.strip().split(":"))[0].split()[1], [elem for part in parts[1].split(";") for elem in part.split(",")]), {}
	pgn += 0 if any(int(arg.split()[0]) > limits[arg.split()[1].strip(",")] for arg in args) else int(game)
	for arg in args:
		if (value := int(arg.split()[0])) > mxs.get((color := arg.split()[1].strip(",")), 0):
			mxs[color] = value
	pwc += (mxs["red"]* mxs["green"]* mxs["blue"])
print(pgn, pwc)
