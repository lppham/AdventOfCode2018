# COMPLETE

import heapq
import collections
import itertools
# Container containing relevant meta data from each unit

def neighbors(x, y):
	return [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]	

class Unit():

	def __init__(self, race, pos, hp, ad):
		self.pos = pos
		self.hp = hp
		self.ad = ad
		self.is_elf = race
		self.dead = False

class ElfDied(Exception):
	pass

class Game():
	def __init__(self, board, hp, goblin_ad, elf_ad = 3, noElfDies = False):
		self.bound_i = len(board)
		self.bound_j = len(board[0])
		self.goblins, self.elves, self.walls = {}, {}, {}
		self.order = []
		self.noElfDies = noElfDies

		for i in xrange(self.bound_i):
			for j in xrange(self.bound_j):
				unit = None
				pos = (i,j)
				tile = board[i][j]
				self.walls[pos] = tile == "#"

				# Create a unit class for each unit
				if tile == "G":
					unit = Unit(False, pos, hp, goblin_ad)
					self.goblins[pos] = unit
				elif tile == "E":
					unit = Unit(True, pos, hp, elf_ad)
					self.elves[pos] = unit
				
				# If space is a unit, add it to the turn order
				if unit:
					heapq.heappush(self.order, (pos, unit))


	def isValid(self, i, j):
		pos = (i,j)
		return not self.walls[(i,j)] and pos not in self.elves and pos not in self.goblins
		# i < self.bound_i and i >= 0 and j >=0 and j < self.bound_j and 

	def shortestPath(self, unit, in_range):
		to_visit = collections.deque([(unit.pos, 0)])
		seen = set()
		distances = {unit.pos : (0, None)} 
		
		# DFS
		while to_visit:
			pos, dist = to_visit.popleft()
			for neigh in neighbors(*pos):
				if self.walls[neigh] or neigh in self.goblins or neigh in self.elves:
					continue
				if neigh not in distances or distances[neigh] > (dist + 1, pos): # Record the shortest distance seen so far
					distances[neigh] = (dist + 1, pos)
				if neigh not in seen and not any(neigh == node[0] for node in to_visit):
					to_visit.append((neigh, dist + 1))
			seen.add(pos)

		try:
			min_d, closest_pos = min((dist, pos) for pos, (dist, _) in distances.items() if pos in in_range)
		except ValueError:
			return None

		while distances[closest_pos][0] > 1: # Distance from initial pt. Trace back to closest pt
			closest_pos = distances[closest_pos][1]

		return closest_pos

	def move(self, unit):

		# Identify targets and allies
		targets = self.goblins if unit.is_elf else self.elves
		allies = self.elves if unit.is_elf else self.goblins

		taken = {p for p in targets}
		taken.update({p for p in allies if p != unit.pos})

		# Check which ones in range (adjacent free squares)
		in_range = set(adj for tar in targets for adj in neighbors(*tar) if not self.walls[adj] and adj not in taken)

		# Check if it can attack right now. If not, move
		if not unit.pos in in_range:
			# Check which ones reachable (do a shortest path to each one)
			# Find which one nearest
			# If there are more than one, use reading order
			closest_pos = self.shortestPath(unit, in_range)

			if closest_pos:
				del allies[unit.pos]
				unit.pos = closest_pos
				allies[unit.pos] = unit

		# Now check again if it can attack
		enemy = [targets[u] for u in neighbors(*unit.pos) if u in targets]

		if enemy:
			target = min(enemy, key = lambda u : (u.hp, u.pos))
			target.hp -= unit.ad

			if target.hp <= 0:
				del targets[target.pos]
				target.dead = True

				#print "An ally has been slain!"
				if target.is_elf == True and self.noElfDies:
					print "An ally has been slain!"
					raise ElfDied()
				# Removing form turn order happens later

	def run_round(self):
		new_order = []	
		while self.order:
			s_pos, unit = heapq.heappop(self.order)

			# check if the unit is still alive (he could've died)
			if not unit.dead:
				self.move(unit)
				heapq.heappush(new_order, (unit.pos, unit))
			else:
				print "deaded"
		self.order = new_order

	def play(self):
		num_rounds = 0
		while self.goblins and self.elves:
			self.run_round()
			num_rounds += 1

		num_rounds -= 1
		winner = self.elves if self.elves else self.goblins
		totals = sum(winner[unit].hp for unit in winner)

		return num_rounds * totals

def playGame1(f, hp, goblin_ad):
	board = [list(line.rstrip('\n')) for line in open(f)]
	return Game(board, hp, goblin_ad).play()

def playGame2(f, hp, goblin_ad):
	board = [list(line.rstrip('\n')) for line in open(f)]

	for elf_ad in itertools.count(4):
		try:
			ans = Game(board, hp, goblin_ad, elf_ad, noElfDies = True).play()
		except ElfDied:
			continue
		else:
			break

	return ans


#Part 1
print playGame1('input/dec15', 200, 3)

#Part 2
print playGame2('input/dec15', 200, 3)
