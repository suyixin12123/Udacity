"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.time_millis = lambda: 1000 * timeit.default_timer()
        self.move_start = self.time_millis()
        self.time_left = lambda : 2000 - (self.time_millis() - self.move_start)

    def test_upper(self):
        isolationPlayer = game_agent.IsolationPlayer(score_fn=sample_players.open_move_score(self.game, self.game.active_player))
        minmaxPlayer = game_agent.MinimaxPlayer(isolationPlayer)
        move = minmaxPlayer.get_move(self.game, self.time_left)
        print(move)


if __name__ == '__main__':
    unittest.main()
