# COMPLETE



freq = set()
found = False
res = 0
while not found:
	with open('input/dec1') as dec1:
		freq.add(res)
		for line in dec1:
			res += int(line)
			if res in freq:
				found = True
				print res
				break
			freq.add(res)

print res