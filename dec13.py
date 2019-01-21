# COMPLETE

turns = { "^" : "<^>",
		  "v" : ">v<",
		  "<" : "v<^",
		  ">" : "^>v" }

step = { "^" : (-1, 0),
		  "v" : (1, 0),
		  "<" : (0, -1),
		  ">" : (0, 1) }


up_moves = { "/"  : ">",
		     "\\" : "<",
		     "|"  : "^",
		     "-"  : None }

down_moves = { "/"  : "<",
		     "\\" : ">",
		     "|"  : "v",
		     "-"  : None }


left_moves = { "/"  : "v",
		     "\\" : "^",
		     "|"  : None,
		     "-"  : "<" }

right_moves = { "/"  : "^",
		     "\\" : "v",
		     "|"  : None,
		     "-"  : ">" }

moves = { "^" : up_moves,
		  "v" : down_moves,
		  "<" : left_moves,
		  ">" : right_moves}


class Cart():
	def __init__(self, idx, x, y, direction, prev=None):
		self.id = idx
		self.x = x
		self.y = y
		self.prev = prev
		self.direction = direction
		self.turn = 0 % 3
		self.moved = False

	def turner(self, tracks):
		self.direction = turns[self.direction][self.turn]
		self.turn = (self.turn + 1) % 3

	def move(self, tracks, carts):

		# Should only be moved once a turn
		if self.moved == True:
			return

		dx, dy = step[self.direction]
		nx, ny = self.x + dx, self.y + dy

		#print self.id, self.x, self.y, nx, ny
		# check collision
		if tracks[nx][ny] in carts: # maybe check if object is there




			return self.id, tracks[nx][ny]

		# check intersection
		elif tracks[nx][ny] == "+":
			self.turner(tracks)
			tracks[self.x][self.y] = self.prev
			self.prev = tracks[nx][ny]
			tracks[nx][ny] = self.id
			self.x, self.y = nx, ny

		# check corner and others
		else:
			self.direction = moves[self.direction][tracks[nx][ny]]
			tracks[self.x][self.y] = self.prev
			self.prev = tracks[nx][ny]
			tracks[nx][ny] = self.id
			self.x, self.y = nx, ny

		self.moved = True
		return None

	def remove(self, tracks):
		tracks[self.x][self.y] = self.prev


# Get input
with open('input/dec13') as dec13:
	mine = [list(line) for line in dec13]


# Get all meta data on carts
carts = {}
cnum = 0

for x in xrange(len(mine)):
	for y in xrange(len(mine[0])):
		char = mine[x][y]
		if char in "^v<>":
			cart = Cart(cnum, x, y, char, "|" if char in "^v" else "-")
			carts[cnum] = cart
			mine[x][y] = cnum
			cnum += 1 

while True:
	for i in carts:
		carts[i].moved = False
	ct = 0
	for x in xrange(len(mine)):
		for y in xrange(len(mine[0])):
			if mine[x][y] in carts:
				ret = carts[mine[x][y]].move(mine, carts)

				if ret:
					carts[ret[0]].remove(mine)
					carts[ret[1]].remove(mine)
					a = carts.pop(ret[0], None)
					b = carts.pop(ret[1], None)
				ct += 1
	#print len(carts)
	if len(carts) == 1:
		for key in carts:
			print carts[key].x, carts[key].y
			exit()


	#print ct