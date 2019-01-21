points = []

with open('dec25') as dec25:
	for line in dec25:
		points.append(tuple(map(int, line.split(','))))

def manhattan(p0, p1):
	return sum([abs(x1 - x0) for x0, x1 in zip(p0, p1)])

class UnionFind:

	def __init__(self, n):
		self.n = n
		self.parents = [None] * n
		self.ranks = [1] * n
		self.num_forests = n

	def find(self, i):
		parent = self.parents[i]
		if parent is None:
			return i
		parent = self.find(parent)
		self.parents[i] = parent
		return parent

	def in_same_forest(self, i, j):
		return self.find(i) == self.find(j)

	def merge(self, i, j):
		i = self.find(i)
		j = self.find(j)

		if i == j:
			return

		ir = self.ranks[i]
		jr = self.ranks[j]

		if ir < jr:
			self.parents[i] = j
		elif ir > jr:
			self.parents[j] = i
		else:
			# Arbitrarily choose one
			self.parents[j] = i
			self.ranks[i] += 1

		self.num_forests -= 1


uf = UnionFind(len(points))

seen_idx = {}

for i, p in enumerate(points):
	seen_idx[p] = i

	for pp in seen_idx:
		if manhattan(p, pp) <= 3:
			uf.merge(i, seen_idx[pp])

print uf.num_forests

