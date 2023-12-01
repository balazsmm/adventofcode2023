def sum_calib_value(filtered_numbers):
	return sum(int(ln[0]+ln[-1]) for ln in filtered_numbers)

def filter_numbers(caldoc):
	return ["".join([ch for ch in ln if ch.isnumeric()]) for ln in caldoc.split("\n")]

with open("day1_input", "r") as cdoc:
	calibration_document = cdoc.read().strip()
	
NRS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def analyze_numbers(caldoc):
	lines = caldoc.split("\n")
	filtered_number_strings = []
	for line in lines:
		ret_line = ""
		while len(line) > 0:
			if line[0].isnumeric():
				ret_line += line[0]
				line = line[1:]
				continue
			else:
				for checked_alphanum in NRS:
					if line.startswith(checked_alphanum):
						ret_line += str(NRS.index(checked_alphanum) + 1)
						line = line[len(checked_alphanum)-1:]
						continue
			line = line = line[1:]
		filtered_number_strings.append(ret_line)
	return filtered_number_strings
	
def numval(line_slice):
	if line_slice[0].isnumeric():
		return line_slice[0]
	elif (validnr := [str(NRS.index(element) + 1) for element in NRS if line_slice.startswith(element)]):
		return str(validnr[0])
	return ""
	
def short_analyze_numbers_with_overlap(caldoc):
	return ["".join([numval(line[pos:])for pos, ch in enumerate(line)]) for line in caldoc.split("\n")]
	
if __name__ == "__main__":
	print(filter_numbers(calibration_document))
	print("Sum of calibration values: {}, final: {}".format(sum_calib_value(filter_numbers(calibration_document)), sum_calib_value(analyze_numbers_with_overlap(calibration_document))))
	