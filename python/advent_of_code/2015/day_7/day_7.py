import input

class Instruction:
	def __init__(self, inputs, output, gate=None, shift=0):
		self.inputs = inputs
		self.gate = gate
		self.output = output
		self.shift = shift
		if self.gate == None and type(self.inputs[0]) == 'int':
			self.is_done = True
		else:
			self.is_done = False
		self.ready = False

	def update_inputs(self, wires):
		ready = True
		inputs = []
		for i in self.inputs:
			if i in wires:
				inputs.append(wires[i]) 
			else:
				try:
					inputs.append(int(i))
				except ValueError:
					inputs.append(i)
					ready = False	
		self.inputs = inputs
		self.ready = ready

	def run(self, wires):
		if self.gate == 'AND':
			wires[self.output] = self.inputs[0] & self.inputs[1]
		elif self.gate == 'OR':
			wires[self.output] = self.inputs[0] | self.inputs[1]
		elif self.gate == 'LSHIFT':
			wires[self.output] = self.inputs[0] << self.shift
		elif self.gate == 'RSHIFT':
			wires[self.output] = self.inputs[0] >> self.shift
		elif self.gate == 'NOT':
			wires[self.output] = (1 << 16) - 1 - self.inputs[0]
		else:
			wires[self.output] = self.inputs[0]
		self.is_done = True
		return wires


def process_input(puzzle_input):
	split = puzzle_input.split('\n')
	instructions = []
	wires = {}
	for inst in split:
		i = inst.split(' ')
		if i[0] == 'NOT':
			instructions.append(Instruction([i[1]], i[-1], i[0]))
		elif i[1] == 'LSHIFT' or i[1] == 'RSHIFT':
			instructions.append(Instruction([i[0]], i[-1], i[1], int(i[2])))
		elif i[1] == 'AND' or i[1] == 'OR':
			instructions.append(Instruction([i[0], i[2]], i[-1], i[1]))			
		else:
			try:
				wires[i[-1]] = int(i[0])
			except ValueError:
				instructions.append(Instruction([i[0]], i[-1]))
	return instructions, wires

def run_instructions(instructions, wires):
	while True:
		for inst in instructions:
			inst.update_inputs(wires)
			if inst.is_done == False and inst.ready == True:
				wires = inst.run(wires)
			if 'a' in wires:
				break
		if 'a' in wires:
			break
	return wires['a']

instructions, wires = process_input(input.puzzle_input)
a = run_instructions(instructions, wires)
print(a)

instructions2, wires2 = process_input(input.puzzle_input)
wires2['b'] = a
print(run_instructions(instructions2, wires2))




# wires = {'x': 123, 'y': 456}
# inst = Instruction(['x', 'y'], 'AND', 'd')

# print(inst.is_ready_to_run(wires))
# print(inst.is_done)

# wires = inst.run(wires)
# print(wires)
# print(inst.is_done)