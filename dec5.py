# COMPLETE
with open('input/dec5') as dec5:
	line = dec5.readline()

def foldr(acc, s):
	s = list(s)
	while s:
		first = s.pop(0)
		if acc[-1].upper() == first.upper() and acc[-1].isupper() != first.isupper():
			# this means they are the same
			acc = acc[:-1]
		else:
			acc += first

	return len(acc) -1

print foldr("#", line)

alpha = "abcdefghijklmnopqrstuvwxyz"

arr = [0] * len(alpha)

for i in range(len(alpha)):
	letter = alpha[i]
	arr[i] = foldr('#', line.replace(letter, "").replace(letter.upper(), ""))


print min(arr)