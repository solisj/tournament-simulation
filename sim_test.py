import unittest
import sim

class TestPlayer(unittest.TestCase):
  def test_addscore(self):
    player = sim.Player(1000)
    self.assertEqual(player.get_score(),0)
    player.add_score(1)
    self.assertEqual(player.get_score(),1)
  def test_getwinprob(self):
    elo1 = 1000
    elo2 = 1000
    self.assertEqual(sim.get_win_prob(elo1,elo2),0.5)
    elo3 = 800
    elo4 = 1200
    self.assertEqual(sim.get_win_prob(elo3,elo4),1/11)
  def test_sortplayers(self):
    player1 = sim.Player(1000)
    player1.add_score(1)
    player2 = sim.Player(1000)
    player2.add_score(2)
    player3 = sim.Player(1000)
    player3.add_score(3)
    players = [player1, player3, player2]
    sim.sort_players(players)
    self.assertEquals(players[0].get_score(), 1)
    self.assertEquals(players[1].get_score(), 2)
    self.assertEquals(players[2].get_score(), 3)

if __name__ == '__main__':
  unittest.main()
