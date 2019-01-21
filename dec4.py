# COMPLETE

from datetime import datetime
from datetime import timedelta
import operator
import re

def parse_time(s):
	pattern = re.compile(r"""\[(?P<time>.*?)\] # time
						 \s(?P<command>.*?)$   # command
						 """, re.VERBOSE)
	match = pattern.match(s)
	dt = datetime.strptime(match.group('time'), '%Y-%m-%d %H:%M')
	cmd = match.group('command')

	num = 0
	if cmd == "falls asleep":
		num = -1
	elif cmd == "wakes up":
		num = 0
	else:
		num = int(cmd.split(' ')[1][1:])

	return (dt, num)

def check_and_add(d, k, date):
	if k not in d:
		d[k] = { date : [0] * 60}
	else:
		d[k][date] = [0] * 60

with open('input/dec4') as dec4:
	times = sorted([parse_time(line) for line in dec4])

table = {}

last_guard = None
for time, status in times:
	if status > 0: # New guard on shift
		if time.hour != 0:
			date = (time + timedelta(days=1)).date()
		else:
			date = time.date()

		last_guard = status
		asleep = False
		a_time = 0
		check_and_add(table, last_guard, date)
	elif status == 0 and asleep:
		asleep = False
		for i in xrange(a_time, int(time.minute)):
			table[last_guard][time.date()][i] = 1

		a_time = 0
	else:
		asleep = True
		a_time = int(time.minute)

# Get minutes asleep
minutes_asleep = {}
for guard in table:
	minutes_asleep[guard] = sum([sum(table[guard][x]) for x in table[guard]])

print max(minutes_asleep.iteritems(), key=operator.itemgetter(1)) # Get max ID

# get minute he is most asleep
total_a_time = [sum(x) for x in zip(*table[3167].values())] # 3167 is guard num
the_minute = total_a_time.index(max(total_a_time))
ans1 = the_minute * 3167

# Part 2
highest_minute_per_guard = {}
max_highest = {}
for guard in table:
	highest_minute_per_guard[guard] = [sum(x) for x in zip(*table[guard].values())]
	max_highest[guard] = max(highest_minute_per_guard[guard])

guard_most_same_minutes, times = max(max_highest.iteritems(), key=operator.itemgetter(1))
the_minute = highest_minute_per_guard[guard_most_same_minutes].index(times)

print the_minute * guard_most_same_minutes	


