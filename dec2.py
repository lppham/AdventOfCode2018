# COMPLETE

from collections import Counter

# Part 1
two = 0
three = 0
length = 0
with open('input/dec2') as dec2:
	for line in dec2:
		length = len(line)
		ctr = Counter(line)
		two += 1 if 2 in ctr.values() else 0
		three += 1 if 3 in ctr.values() else 0

print two * three

print length

# Part 2
same = set()
for i in xrange(length-1):
	same = set()
	with open('dec2') as dec2:
		for line in dec2:
			test = line[:i] + line[i+1:]
			if test in same:
				print test
			same.add(test)
