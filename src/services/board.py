#!/usr/bin/env python

from src.services.ladder import Ladder
from src.services.snake import Snake
from src.services.crocodile import Crocodile
from src.services.mine import Mine
from src.constants.board_objects import BoardObjects
from src.constants.messages import ExceptionMessage

__author__     = "Pooja Deshmukh"

class Board:

    def __init__(self, size):
        self.board = {}
        self.size = size

    def set_snakes(self, snake):
        if snake[0] in self.board:
            raise Exception(ExceptionMessage.already_occupied)
        self.board[snake[0]] = (BoardObjects.snake, Snake(snake[0], snake[1]))

    def set_ladder(self, ladder):
        if ladder[0] in self.board:
            raise Exception(ExceptionMessage.already_occupied)
        self.board[ladder[0]] = (BoardObjects.ladder, Ladder(ladder[0], ladder[1]))
    
    def set_crocodiles(self, crocodile):
        if crocodile[0] in self.board:
            raise Exception(ExceptionMessage.already_occupied)
        self.board[crocodile[0]] = (BoardObjects.crocodile, Crocodile(crocodile[0], crocodile[0]-5))
    
    def set_mines(self, mine):
        if mine[0] in self.board:
            raise Exception(ExceptionMessage.already_occupied)
        self.board[mine[0]] = (BoardObjects.mine, Mine(mine[0], mine[0]))



    def move_to_new_position(self, curr_pos, action):
        if curr_pos > self.size:
            return -1, ''

        if curr_pos in self.board:
            if self.board[curr_pos][0] == BoardObjects.snake:
                new_pos = self.board[curr_pos][1].tail
                if curr_pos > new_pos:
                    curr_pos = new_pos
                    action = BoardObjects.snake
                else:
                    return curr_pos, ''
            elif self.board[curr_pos][0] == BoardObjects.ladder:
                new_pos = self.board[curr_pos][1].end
                if curr_pos < new_pos:
                    curr_pos = new_pos
                    action = BoardObjects.ladder
                else:
                    return curr_pos, ''
            elif self.board[curr_pos][0] == BoardObjects.crocodile:
                curr_pos = self.board[curr_pos][1].tail
                action = BoardObjects.crocodile
            elif self.board[curr_pos][0] == BoardObjects.mine:
                curr_pos = self.board[curr_pos][1].new
                action = BoardObjects.mine
        return curr_pos, action

    def get_player_status(self, pos):
        return self.size == pos
