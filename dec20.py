import networkx

pathways = open('dec20').read()[1:-1]

path_stack = []

start = {0}
end = set()
pos = {0}

cardinal = {"N" :   1,
			"S" :  -1,
			"E" :  1j,
			"W" : -1j,}


rooms = networkx.Graph()

for move in pathways:
	if move == "(":
		path_stack.append((start, end))
		start, end = pos, set()
	elif move in "NSEW":
		direct = cardinal[move]
		rooms.add_edges_from((r, r + direct) for r in pos)
		pos = {r + direct for r in pos}
	elif move == "|":
		end.update(pos)
		pos = start
	elif move == ")":
		pos.update(end)
		start, end = path_stack.pop()

shortest_paths = networkx.algorithms.shortest_path_length(rooms, 0)

print "Part 1: ", max(shortest_paths.values())
print "Part 2: ", sum(1 for r in shortest_paths.values() if r >= 1000)