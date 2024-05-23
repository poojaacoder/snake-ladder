#!/usr/bin/env python


import unittest
from src.services.game import Game


__author__     = "Pooja Deshmukh"


class TestSnake_ladder(unittest.TestCase):
    """
    Tests for snake_ladder package.
    """

    def setUp(self):
        self.board_size = 100
        self.players = ["pooja", "aparna"]
        self.dice_faces = 6
        self.snakes = [[62,5], [33, 6], [49,9],[88,16], [41,20],[56,53],[98,64],[93,73],[95,75]]
        self.ladders = [[2, 37], [27, 46], [10, 32], [51, 68], [61, 79], [65, 84], [71, 91], [81, 100]]
        self.crocodiles = [[11] ,[18], [23], [24], [36]]
        self.starting_postions = {
            "pooja":0,
            "aparna":0
        }
        self.mines = [ [4],[12], [25], [35], [44], [55], [66], [92]]
        self.snake_ladder_game = Game(self.dice_faces, self.board_size)
        self.snake_ladder_game.set_snake_ladders(self.snakes, self.ladders, self.crocodiles,self.mines)
        self.snake_ladder_game.set_players(self.players, self.starting_postions)


    def test_add_winner(self):
        expected = ["pooja"]
        self.snake_ladder_game.add_winner("pooja")
        assert self.snake_ladder_game.winners == expected

    def test_dice_score(self):
        assert self.snake_ladder_game.dice.get_random_face() > 0

