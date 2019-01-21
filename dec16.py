# Complete

def addr(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] + res[b]
	return res

def addi(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] + b
	return res

def mulr(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] * res[b]
	return res

def muli(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] * b
	return res

def banr(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] & res[b]
	return res

def bani(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] & b
	return res

def borr(registers, a, b ,c):
	res = list(registers)
	res[c] = res[a] | res[b]
	return res

def bori(registers, a, b, c):
	res = list(registers)
	res[c] = res[a] | b
	return res

def setr(registers, a, b, c):
	res = list(registers)
	res[c] = res[a]
	return res

def seti(registers, a, b, c):
	res = list(registers)
	res[c] = a
	return res

def gtir(registers, a, b, c):
	res = list(registers)
	res[c] = bool(a > res[b])
	return res

def gtri(registers, a, b, c):
	res = list(registers)
	res[c] = bool(res[a] > b)
	return res

def gtrr(registers, a, b, c):
	res = list(registers)
	res[c] = bool(res[a] > res[b])
	return res

def eqir(registers, a, b, c):
	res = list(registers)
	res[c] = bool(a == res[b])
	return res

def eqri(registers, a, b, c):
	res = list(registers)
	res[c] = bool(res[a] == b)
	return res

def eqrr(registers, a, b, c):
	res = list(registers)
	res[c] = bool(res[a] == res[b])
	return res

OPERATIONS = [
	addr, addi,
	mulr, muli,
	banr, bani,
	borr, bori,
	setr, seti,
	gtir, gtri, gtrr,
	eqir, eqri, eqrr
]
dec16 = [line.rstrip('\n') for line in open('input/dec16')]

# Part 1
def possible(instructions, before, after):
	res = set()

	for op in OPERATIONS:
		apply_op = op(before, *instructions[1:])
		if apply_op == after:
			res.add(op)

	return res

i = 0
samples = []

while dec16[i].strip():
	before, instruct, after = dec16[i:i+3]
	i += 4

	samples.append( [list(map(int, instruct.split(' '))),
					eval(before[8:]),
					eval(after[8:])])

print len([sample for sample in samples if len(possible(*sample)) >= 3])

# Part 2
op_nums = { num : set(OPERATIONS) for num in range(16)}

# Remove ones we know to not be the op based on the samples
for sample in samples:
	op_nums[sample[0][0]].intersection_update(possible(*sample))

# Check which ones we've solved due to this
while True:
	unique = {}
	for op_num, ops in op_nums.items():
		if len(ops) == 1:
			unique[op_num] = ops
	for op_num_actual, op_actual in unique.items():
		for op_num_possible, op_possible in op_nums.items():
			if op_num_possible != op_num_actual:
				op_possible.difference_update(op_actual) # It can't be possible because we've narrowed it down

	if len(unique) == len(op_nums):
		break

for op_num in op_nums:
	op_nums[op_num] = unique[op_num].pop()

registers = [0, 0, 0, 0]

# Get after we parsed the samples to get the test exec
for line in dec16[i:]:
	if not line.strip(): #if white space, we move on:
		continue

	op_num, a, b, c = list(map(int, line.split(' ')))
	registers = op_nums[op_num](registers, a,b,c)

print registers[0]