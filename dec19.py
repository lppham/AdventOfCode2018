# COMPLETE

def do_cmd(fn):
    def final(before, instr):
        after = list(before)
        after[instr[3]] = fn(before, instr[1], instr[2])
        return after
    return final

addr = do_cmd(lambda before,x,y: before[x]+before[y])
addi = do_cmd(lambda before,x,y: before[x]+y)
mulr = do_cmd(lambda before,x,y: before[x]*before[y])
muli = do_cmd(lambda before,x,y: before[x]*y)
banr = do_cmd(lambda before,x,y: before[x] & before[y])
bani = do_cmd(lambda before,x,y: before[x] & y)
borr = do_cmd(lambda before,x,y: before[x] | before[y])
bori = do_cmd(lambda before,x,y: before[x] | y)
setr = do_cmd(lambda before,x,y: before[x])
seti = do_cmd(lambda before,x,y: x)
gtir = do_cmd(lambda before,x,y: 1 if x > before[y] else 0)
gtri = do_cmd(lambda before,x,y: 1 if before[x] > y else 0)
gtrr = do_cmd(lambda before,x,y: 1 if before[x] > before[y] else 0)
eqir = do_cmd(lambda before,x,y: 1 if x == before[y] else 0)
eqri = do_cmd(lambda before,x,y: 1 if before[x] == y else 0)
eqrr = do_cmd(lambda before,x,y: 1 if before[x] == before[y] else 0)

registers = [1, 0, 0, 0, 0, 0]

operations = {
	"addr" : addr,
	"addi" : addi,
	"mulr" : mulr,
	"muli" : muli,
	"banr" : banr,
	"bani" : bani,
	"borr" : borr,
	"bori" : bori,
	"setr" : setr,
	"seti" : seti,
	"gtir" : gtir,
	"gtri" : gtri,
	"gtrr" : gtrr,
	"eqir" : eqir,
	"eqri" : eqri,
	"eqrr" : eqrr
}

instructions = []
with open('input/dec19') as dec19:
	ip = 0
	for line in dec19:
		line = line.rstrip('\n')
		if line[0] = '#':
			ip = int(line[-1])
		else:
			instructions.append(line.split(" "))

while registers[ip] < len(instructions):
	instruct = instructions[registers[ip]]
	if registers[ip] == 1:
		'''
		What is actually running:
		while r[4] <= r[1]:
			while r[2] <= r[1]:
				if r[2] * r[4] == r[1]:
					r[0] += 4
				r[2] += 1
			r[4] += 1
			r[2] = 1
		'''
		big_num = registers[1]
		print sum([x for x in xrange(1, big_num + 1) if big_num % x == 0])
		break

	args = list(map(int, instruct[1:]))
	registers = operations[instruct[0]](registers, *args)
	registers[ip] += 1

print registers[0]