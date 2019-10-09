import sim
import random

elos = [955,965,975,985,995,1005,1015,1025,1035,1045]
players = [sim.Player(elos[i]) for i in range(10)]

# print(players)

# sim.do_round(players)
# sim.sort_players(players)

# print(players)

random.shuffle(players)

for i in range(10):
	print("doing round " + str(i))
	print(players)
	sim.do_round(players)
	sim.sort_players(players)
	print(players)
	print("\n")