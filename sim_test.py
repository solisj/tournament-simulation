import unittest
import sim

class TestPlayer(unittest.TestCase):
  def test_addscore(self):
    player = sim.Player(1000)
    self.assertEqual(player.get_score(),0)
    player.add_score(1)
    self.assertEqual(player.get_score(),1)
  def test_getwinprob(self):
    elos = [1000,1000]
    self.assertEqual(sim.get_win_prob(elos),[0.5,0.5])
    elos = [800, 1200]
    self.assertEqual(sim.get_win_prob(elos),[1/11,10/11])
    elos = [1000,1000,1000]
    self.assertEqual(sim.get_win_prob(elos),[1/3,1/3,1/3])
  def test_scoredistribution(self):
    num_players = 4
    difficulty = sim.Difficulty.EASY
    scores = sim.score_distribution(num_players, difficulty)
    self.assertEqual(scores,[4,3,2,1])
  def test_sortplayers(self):
    player1 = sim.Player(1000)
    player1.add_score(1)
    player2 = sim.Player(1000)
    player2.add_score(2)
    player3 = sim.Player(1000)
    player3.add_score(3)
    players = [player1, player3, player2]
    sim.sort_players(players)
    self.assertEqual(players[0].get_score(), 1)
    self.assertEqual(players[1].get_score(), 2)
    self.assertEqual(players[2].get_score(), 3)

if __name__ == '__main__':
  unittest.main()
