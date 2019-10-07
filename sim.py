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

def adjust_one_bracket(bracket):
  """
  Adjust the elos and scores of the players in one bracket.
  Input: bracket, a list of the players in the bracket.
  """
  #TODO implement this

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

