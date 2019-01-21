#COMPLETE

import re
from copy import deepcopy
with open('dec24') as dec24:
	lines = dec24.read()

pattern =  re.compile(r"(\d+) units each with (\d+) hit points (\([^)]*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)")
immune, infection = lines.split('\n\n')
teams_og = []

# Fancy Enumeration
N_UNITS, HP, DMG, DMG_TYPE, INITIATIVE, WEAK_TO, IMMUNE_TO = range(7)

# Parse the file
for team in [immune, infection]:
	groups = team.splitlines()[1:] # Omit the header
	side = []

	for group in groups:
		n_units, hp, affinity, dmg, dmg_type, initiative = pattern.match(group).groups()

		immune_to = set()
		weak_to = set()

		if affinity:
			weak_str = "weak to "
			lws = len(weak_str)
			immune_str = "immune to "
			lis = len(immune_str)

			affinity = affinity.lstrip("(").rstrip(" )")

			for aff in affinity.split("; "):
				if aff.startswith(weak_str):
					weak_to = set(aff[lws:].split(", "))
				elif aff.startswith(immune_str):
					immune_to = set(aff[lis:].split(", "))

		stats = [int(n_units), int(hp), int(dmg), dmg_type,
				 int(initiative), weak_to, immune_to]

		side.append(stats)

	teams_og.append(side)

def effective_power(g):
	return g[DMG] * g[N_UNITS]

def deal_dmg(attack, defend):
	mult = 1
	if attack[DMG_TYPE] in defend[IMMUNE_TO]:
		mult = 0
	elif attack[DMG_TYPE] in defend[WEAK_TO]:
		mult = 2
	return effective_power(attack) * mult

def simulate(boost = 0):
	teams = deepcopy(teams_og)
	for group in teams[0]:
		group[DMG] += boost

	while all(not all(u[N_UNITS] <= 0 for u in  team) for team in teams):
	#while any(u[N_UNITS] > 0 for u in team[0]) and any(u[N_UNITS] > 0 for u in team[1]):
		for i in range(2):
			teams[i].sort(key= lambda x: (effective_power(x), x[INITIATIVE]), reverse = True)
		# Target Selection
		# For each team, the highest power teammate picks first

		all_targets = []
		for i in range(2):
			allies = teams[i]
			enemies = teams[1-i]
			possible_targets = set(k for k in range(len(enemies)) if enemies[k][N_UNITS] > 0)
			picked_targets = [None] * len(allies)

			for k, t in enumerate(allies):
				if not possible_targets:
					break

				# gives you their ID
				best_target = max(possible_targets, key = lambda l : (deal_dmg(t, enemies[l]), effective_power(enemies[l]), enemies[l][INITIATIVE]))

				# If he's immune don't bother
				if deal_dmg(t, enemies[best_target]) == 0:
					continue

				# Add it to your pick list and remove from possible
				picked_targets[k] = best_target
				possible_targets.remove(best_target)
			all_targets.append(picked_targets)


		# Attacking
		attack_order = [(0, ai) for ai in range(len(teams[0]))] + [(1, ai) for ai in range(len(teams[1]))]
		attack_order.sort(key= lambda x: teams[x[0]][x[1]][INITIATIVE], reverse = True)

		did_dmg = False
		for ti, u_id in attack_order:
			target_id = all_targets[ti][u_id]
			if target_id is None:
				continue

			unit_stats = teams[ti][u_id]
			target_stats = teams[1-ti][target_id]

			dmg = deal_dmg(unit_stats, target_stats) // target_stats[HP]

			if dmg > 0 and teams[1-ti][target_id][N_UNITS] > 0:
				did_dmg = True


			teams[1-ti][target_id][N_UNITS] -= dmg
			if teams[1-ti][target_id][N_UNITS] < 0:
				teams[1-ti][target_id][N_UNITS] = 0

		if not did_dmg:
			break

	immune_left = sum(u[N_UNITS] for u in teams[0])
	infect_left = sum(u[N_UNITS] for u in teams[1])
	print "Part 1: ", immune_left, infect_left
	if immune_left > 0:
		return True
	return False

lo, hi = 0, 5000
results = {0 : False}

def calc_results(boost):
	if boost in results:
		return results[boost]

	results[boost] = simulate(boost)
	return results[boost]
'''
while True:
	lo_res = calc_results(lo)
	hi_res = calc_results(hi)
	mid = (lo + hi) / 2
	mid_res = calc_results(mid)

	if mid_res and not calc_results(mid-1):
		print "HERE"
		simulate(mid)
		exit()
	if not lo_res and not mid_res:
		lo = mid + 1
	elif hi_res and mid_res:
		hi = mid + 1
'''
for i in range(40, 60):
	print i, simulate(i)











