# COMPLETE
initial = "##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##.."
# 1623

GENS = 20
form = {}

with open('input/dec12') as dec12:
	for line in dec12:
		split = line.replace(" ", "").rstrip('\n').split('=>')
		if len(split) == 2:
			form[split[0]] = split[1]

app = "".join([".."] * GENS)
print len(initial)
initial = app + "*" + initial[1:] + app

prev = initial
pots = ""
p_ctr = 0 
for k in range(142):
	pots = ""

	prev = prev.strip('.')
	prev = "...." + prev + "...."

	for i in range(len(prev)):
		if i < 2 or i >= len(prev) - 2:
			pots += '.'
		else:
			test_set = prev[i-2:i+3]
			if '^' in test_set:
				test_set = test_set.replace('^', '.')
			elif '*' in test_set:
				test_set = test_set.replace('*', '#')

			if prev[i] == '^' or prev[i] == '*':
				f = form[test]
				pots += '^' if f == '.' else '*'
			else:
				pots += form[test_set]

	if prev.strip('.') == pots.strip('.'):
		break

	prev = pots

	ctr = 0
	start = 0
	for i in range(len(pots)):
		if pots[i] in "^*":
			start = i

	for i in range(len(pots)):
		if pots[i] in "#*":
			ctr += i - start

	if ctr - p_ctr != 32:
		print k
	else:
		print "d" + str(k)

	p_ctr = ctr

print len(initial)
print len(pots)
print ctr

print ctr + ((50000000000) - 142) * 32

# * is #
# ^ is .