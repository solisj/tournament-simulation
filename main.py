import sim
import random

elos = [955,965,975,985,995,1005,1015,1025,1035,1045]
players = [sim.Player(elos[i]) for i in range(10)]

# print(players)

# sim.do_round(players)
# sim.sort_players(players)

# print(players)

#seeding round

print("doing seeding")
random.shuffle(players)
print(players)
sim.do_round(players, [4,3,3], [sim.Difficulty.EASY,sim.Difficulty.EASY,sim.Difficulty.EASY])
print(players)
sim.sort_players(players)
print(players)
for player in players:
	player.reset_score()
print(players)
print("\n")

#10 rounds

for i in range(1,10+1):
	print("doing round " + str(i))
	print(players)
	sim.do_round(players, [4,3,3], [sim.Difficulty.EASY,sim.Difficulty.MEDIUM,sim.Difficulty.HARD])
	sim.sort_players(players)
	print(players)
	print("\n")