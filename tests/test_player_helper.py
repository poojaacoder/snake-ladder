#!/usr/bin/env python

from src.utils.player_helper import player_move
from src.constants.board_objects import BoardObjects
import unittest

__author__     = "Pooja Deshmukh"


class TestUtils(unittest.TestCase):

    def test_player_turn_with_moves(self):
        expected = "pooja rolled a 2 and moved from 42 to 44"
        assert player_move("pooja", 2, 42, 44, "") == expected

    def test_player_turn_with_no_move(self):
        expected = "pooja rolled a 6 and but can't move from 99"
        assert player_move("pooja", 6, 99, 99, "") == expected
    
    def test_player_turn_with_ladder(self):
        excepted = "pooja rolled a 6 and climbed the ladder at 10 and moved from 4 to 32"
        assert player_move("pooja", 6, 4, 32, BoardObjects.ladder) == excepted
    
    def test_player_turn_with_crocodile(self):
        expected = "pooja rolled a 3 and eaten by crocodile at 24 and moved from 21 to 19"
        assert player_move("pooja", 3, 21, 19, BoardObjects.crocodile) == expected
    
    def test_player_turn_with_snake(self):
        expected = "pooja rolled a 5 and bitten by snake at 49 and moved from 44 to 9"
        assert player_move("pooja", 5, 44, 9, BoardObjects.snake) == expected

    
    def test_player_turn_with_mine(self):
        expected = "pooja rolled a 1 and end up going in mine 4 , so will be waiting at 3 and won't play for next 2 turns"
        assert player_move("pooja",1, 3, 3, BoardObjects.mine) == expected