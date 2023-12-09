class Almanac:
	def __init__(self, almanac_data):
		self.almanac_data = almanac_data.split("\n\n")
		self.seeds = [int(val) for val in self.almanac_data[0].split(":")[1].strip().split(" ")]
		self.get_maps()
		
	def convert_seeds_to_seed_range_gen(self):
		self.seed_ranges = [[self.seeds[i],self.seeds[i+1]] for i in range(0,len(self.seeds),2)]
		for range_pairs in self.seed_ranges:
			pointer = range_pairs[0]
			while pointer < range_pairs[0] + range_pairs[1]:
				yield pointer
				pointer += 1
		
	def minimum_of_seed_ranges_mappings(self):
		min_val = 11111111111111111111111111111111111111111111111
		for seed in self.convert_seeds_to_seed_range_gen():
			if (crn := self.map_value_to_next_stage(seed, -1)) < min_val:
				min_val = crn
		return min_val
	
	def get_maps(self):
		self.mappings = []
		for map in self.almanac_data[1:]:
			mapping_lines = map.split(":\n")[1]
			mapping_values = [[int(val) for val in line.strip().split(" ")] for line in mapping_lines.split("\n")]
			self.mappings.append(mapping_values)
			
	def map_value_to_mapping(self, value, mapping):
		for rule in mapping:
			if rule[1] <= value <=rule[1]+rule[2]-1:
				return rule[0]+ value - rule[1]
		return value
	
	def map_record_to_next_stage(self, record, stage):
		stage += 1
		print(stage)
		new_record = [self.map_value_to_mapping(elem, self.mappings[stage]) for elem in record]
		if stage < len(self.mappings) - 1:
			next_record_stage = self.map_record_to_next_stage(new_record, stage)
			return next_record_stage
		else:
			return new_record
	
	def map_value_to_next_stage(self, value, stage):
		stage += 1
		new_value = self.map_value_to_mapping(value, self.mappings[stage])
		if stage < len(self.mappings) - 1:
			next_value_stage = self.map_value_to_next_stage(new_value, stage)
			return next_value_stage
		else:
			return new_value

	def iteration_counter(self):
		print("Iterations: {}".format(sum(self.seeds[0: -1: 2])))


if __name__ == "__main__":
	with open("day5_input.txt", "r") as ifile:
		idata = ifile.read().strip()
	a = Almanac(idata)
	a.iteration_counter()