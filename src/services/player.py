#!/usr/bin/env python

from src.services.board import Board
from src.services.dice import Dice
from src.constants.board_objects import BoardObjects
from src.utils.player_helper import player_move

__author__     = "Pooja Deshmukh"

class Player:

    def __init__(self, name, start_position, playing_status):
        self.name = name
        self.position = start_position 
        self.win_status = False
        self.playing_status = True
        self.holding_turns = 0

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position


    """
    play move function which will execute on each move changing postions based on 
    snake, ladder, crocodile , overlapping cell values and mines
    """
    def play_move(self, dice: Dice, board: Board, players, is_automate):
        curr_pos = self.get_position()
        # dice_face = dice.get_dice_face(self.get_name(),is_automate)
        dice_face = dice.get_dice_face_result(self.get_name(),is_automate)
        new_pos = curr_pos + dice_face
        action = ''

        new_pos, action = board.move_to_new_position(new_pos, action)

        # Iterate through all player objects to find out if its overlapping with any other player, 
        # once found out the old player needs to start from the 1 position
        for _, playerObj in players.items():
            if new_pos == playerObj.get_position() and self.get_name() != playerObj.get_name():
                print(f"Oops, {playerObj.get_name()} needs to start again from 1 as {self.get_name()} come to that cell")
                playerObj.set_position(1)

 
        if action == BoardObjects.mine:
            self.set_holding_turns(2)
            self.set_playing_status(False)

        if new_pos != -1:
            self.set_position(new_pos)
        else:
            new_pos = curr_pos
        print(player_move(self.get_name(), dice_face, curr_pos, new_pos, action))
        return action 

    
    """
    set player win status
    """
    def set_win_status(self):
        self.win_status = True

    """
    get player win status
    """
    def get_win_status(self):
        return self.win_status
    

    """
    set player playing status
    """
    def set_playing_status(self, status):
        self.playing_status = status


    """
    get player playing status
    """
    def get_player_status(self):
        return self.playing_status
    

    """
    set player holding turns value
    """
    def set_holding_turns(self, turns):
        self.holding_turns = turns


    """
    get player holding turns value
    """
    def get_holding_turns(self):
        return self.holding_turns
