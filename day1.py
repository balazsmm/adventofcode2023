def sum_calib_value(filtered_numbers):
	return sum(int(ln[0]+ln[-1]) for ln in filtered_numbers)

def filter_numbers(caldoc):
	return ["".join([ch for ch in ln if ch.isnumeric()]) for ln in caldoc.split("\n")]

NRS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def numval(line_slice):
	if line_slice[0].isnumeric():
		return line_slice[0]
	elif (validnr := [str(NRS.index(element) + 1) for element in NRS if line_slice.startswith(element)]):
		return str(validnr[0])
	return ""

def short_analyze_numbers_with_overlap(caldoc):
	return ["".join([numval(line[pos:])for pos, ch in enumerate(line)]) for line in caldoc.split("\n")]

if __name__ == "__main__":
	with open("day1_input", "r") as cdoc:
		calibration_document = cdoc.read().strip()
	
	print("Sum of calibration values: {}, final: {}".format(sum_calib_value(filter_numbers(calibration_document)), sum_calib_value(short_analyze_numbers_with_overlap(calibration_document))))
