tree = [int(x) for x in open('input/dec8').readline().split(' ')]


def parse(t):
	n_children, n_metas = t[:2]
	rest = t[2:]
	vals = []
	total = 0

	for i in xrange(n_children):
		total_child, val, rest = parse(rest)
		total += total_child
		vals.append(val)

	this_meta = rest[:n_metas]
	total += sum(this_meta)

	if n_children == 0:
		return total, sum(this_meta), rest[n_metas:]
	else:
		val = sum([vals[x-1] for x in this_meta if 0 < x <= n_children])
		return total, val, rest[n_metas:]

print parse(tree)
