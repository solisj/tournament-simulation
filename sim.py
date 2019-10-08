import random
from enum import Enum

k = 0
avg_score = 2.5
debug = True

class Difficulty(Enum):
  """An enum to represent the different difficulties of the brackets."""
  EASY   = 1
  MEDIUM = 2
  HARD   = 3

class Player:
  """A class that will represent a player's skill as well as their current score."""
  def __init__(self, elo):
    self.elo = elo
    self.score = 0

  def get_elo(self):
    return self.elo

  def get_score(self):
    return self.score

  def add_score(self, new_score):
    self.score += new_score

  def add_elo(self, new_elo):
     self.elo += new_elo

def get_win_prob(elos):
  """Given a list of elos, return a list of the expected scores."""
  #based on https://stats.stackexchange.com/q/66398
  q = []
  for elo in elos:
    q.append(10 ** (elo / 400))
  
  expected_scores = []
  for i in range(len(elos)):
    expected_scores.append(q[i]/sum(q))

  return expected_scores

def get_rankings(elos):
  """Given a list of elos, return a list of the rankings if one round were played (i.e. "run one simulation")."""
  #get expected scores (or probabilities)
  expected_scores = get_win_prob(elos)

  rankings = [] #will have rankings in order (1st, 2nd, ...)
  for i in range(len(elos)): #determine 1st, then 2nd, etc. in order
    total_weight = 1
    for player_index in rankings: 
      total_weight -= expected_scores[player_index]
    for j in range(len(elos)):
      #if this is the last possible player, then just add it 
      #if j == (len(elos) - 1):
      #  rankings.append(j)
      #  break
      if not j in rankings: #if this player has not won already
        if random.random() < ( expected_scores[j] / total_weight ): 
          rankings.append(j)
          break
        total_weight -= expected_scores[j]
  return rankings

def score_distribution(num_players, difficulty = Difficulty.MEDIUM):
  """Return a list of score distributions given the number of players and the difficulty."""
  #initialize scores list 
  scores = []
  for i in range(num_players,0,-1):
    scores.append(i)

  #adjust scores so its average is the same as other distributions of the same difficulty
  expected_total = avg_score * num_players
  actual_total = sum(scores)
  for i in range(num_players):
    scores[i] *= (expected_total/actual_total)

  #adjust scores based on difficulty
  if difficulty == Difficulty.EASY:
    difficulty_adjustment = 1
  if difficulty == Difficulty.MEDIUM:
    difficulty_adjustment = 2
  if difficulty == Difficulty.HARD:
    difficulty_adjustment = 4

  for i in range(num_players):
    scores[i] *= difficulty_adjustment

  return scores

def adjust_one_bracket(bracket):
  """
  Adjust the elos and scores of the players in one bracket.
  Input: bracket, a list of the players in the bracket.
  """
  elos = []
  for player in bracket:
    elos.append(player.get_elo())

  rankings = get_rankings(elos)

  for i in range(len(bracket)): #adjust each player's elo and score
    #find the players you won and lost to    

    won_against = []
    lost_against = []
    for j in range(len(bracket)):
      if i != j:  
        if rankings[i] > rankings[j]:
          won_against.append(bracket[j])
        elif rankings[i] < rankings[j]:
          lost_against.append(bracket[j])

    #adjust elo
    
    for other_player_index in won_against:
      elos = [bracket[i].get_elo(),bracket[other_player_index].get_elo()]
      bracket[i].add_elo(k*(1-get_win_prob(elos)[0])/(len(bracket)-1))
    for other_player_index in lost_against:
      elos = [bracket[i].get_elo(),bracket[other_player_index].get_elo()]
      bracket[i].add_elo(k*(0-get_win_prob(elos[0]))/(len(bracket)-1))

    #adjust score
    bracket[i] += score_distribution(len(bracket))[rankings[i]-1] #adjust score based on ranking (and score distribution)

def sort_players(players):
  """Given a list of players, sort them by score."""
  if len(players) > 1:
    for i in range(len(players)-1): #bubblesort
      for j in range(len(players)-1):
        if players[j].get_score() > players[j+1].get_score(): #swap if not in order
          temp = players[j]
          players[j] = players[j+1]
          players[j+1] = temp

def do_round(players):
  """
  Perform one round, adjusting the player's elo and score accordingly.
  Input: players, a list representing players.
  """
  sort_players(players)
  
  #use players to make a list of the brackets, ordered from lowest bracket to highest

  bracket_sizes = [4, 3, 3] #the sizes of the brackets
  total_used = 0
  brackets = [] #a list of lists representing players in different brackets
  for i in range(len(bracket_sizes)):
    brackets.append(players[total_used:total_used+bracket_sizes[i]])
    total_used += bracket_sizes[i]

  #adjust brackets one by one

  for bracket in brackets:
    adjust_one_bracket(bracket)

if debug:
  elos = [1000,1000,1000]
  wins = [0,0,0] #find how many times each player won in the simulation
  for i in range(1000):
    rankings = get_rankings(elos)
    for j in range(len(wins)):
      wins[j] += 1 if rankings[j] == 0 else 0
  print(wins)
  #elos = [800,1200]
  #print(rankings)
