#COMPLETE
from collections import defaultdict
import heapq

ins = defaultdict(set)
outs = defaultdict(set)
ans = []

def add_nodes(i, o):
	if o not in ins:
		ins[o] = set()
	if i not in outs:
		outs[i] = set()

# Make a graph
with open('input/dec7') as dec7:
	for line in dec7:
		s = line.split(' ')
		s_out = s[1]
		s_in = s[7]

		outs[s_out].add(s_in)
		ins[s_in].add(s_out)

		add_nodes(s_in, s_out)

# Look for nodes with no incoming edges
order = []

for key in ins:
	if not ins[key]:
		heapq.heappush(order, key)

while order:
	node = heapq.heappop(order)
	ans.append(node)
	for edges in outs[node]:
		ins[edges].remove(nodes)
		if not ins[edges]:
			heapq.heappush(order, edges)

# Part 1
print "".join(ans)

# Part 2
from collections import defaultdict
import heapq

ins = defaultdict(set)
outs = defaultdict(set)
ans = []

def add_nodes(i, o):
	if o not in ins:
		ins[o] = set()
	if i not in outs:
		outs[i] = set()

# Make a graph
with open('input/dec7') as dec7:
	for line in dec7:
		s = line.split(' ')
		s_out = s[1]
		s_in = s[7]

		outs[s_out].add(s_in)
		ins[s_in].add(s_out)

		add_nodes(s_in, s_out)

# Look for nodes with no incoming edges
order = []

for key in ins:
	if not ins[key]:
		heapq.heappush(order.key)

times = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(61,87)))
elves = 5
nodes = []
time_left = []
total_time = 0
while order or nodes or time_left:
	# Get all that I can
	while elves > 0 and order:
		node = heapq.heappop(order)
		nodes.append(node)
		time_left.append(times[node])
		elves -= 1

	# Fast forward to the time the next is active
	min_t = min(time_left)
	total_time += min_t
	time_left = [x - min_t for x in time_left]
	new_time_left = []
	new_nodes = []

	for i in range(len(time_left)):
		if time_left[i] == 0:
			elves += 1
			ans.append(nodes[i])
			for edge in outs[nodes[i]]:
				ins[edge].remove(nodes[i])
				if not ins[edge]:
					heapq.heappush(order, edge)
		else:
			new_time_left.append(time_left[i])
			new_nodes.append(nodes[i])

	time_left = new_time_left
	nodes = new_nodes

print total_time