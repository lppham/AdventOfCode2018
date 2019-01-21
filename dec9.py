#Complete
# 446 players; last marble is worth 71522 points
from collections import deque, defaultdict



players = 446
marbles = 71522 + 1
marbles = 71522*100 + 1 #Part 2




circle = deque([0])
scores = [0 for _ in range(players)]

for marble in range(1, marbles):
	if marble % 23 != 0:
		circle.rotate(-1) # rotate is a counterclockwise motion, current marble at the end
		circle.append(marble)
	else:
		circle.rotate(7)
		scores[marble % players] += marble + circle.pop()
		circle.rotate(-1)


print max(scores)