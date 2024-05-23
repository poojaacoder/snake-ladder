#!/usr/bin/env python
from src.services.player import Player
from src.services.dice import Dice
from src.services.board import Board
from src.constants.messages import ExceptionMessage, Msg
import sys

__author__     = "Pooja Deshmukh"

class Game:
    def __init__(self, dice_faces, no_of_dices, dice_stratergy,  board_size):
        self.dice = Dice(dice_faces, no_of_dices, dice_stratergy)
        self.board = Board(board_size)
        self.players = {}
        self.winners = []
        self.active_players = 0
        self.allowed_to_play = True
        self.mine_holding_turn = 0
        self.automate = True

    """
    set players
    """
    def set_players(self, players,start_positions):
        self.active_players = len(players)

        if self.active_players < 2:
            raise Exception(ExceptionMessage.not_enough_players)

        for player in players:
            self.players[player] = Player(player, start_positions[player], True)

    """
    set snake, ladder, crocodile and mine
    """
    def set_snake_ladders(self, snakes, ladders, crocodiles, mines):
        for snake in snakes:
            try:
                self.board.set_snakes(snake)
            except:
                continue

        for ladder in ladders:
            try:
                self.board.set_ladder(ladder)
            except:
                continue
                          
        for crocodile in crocodiles:
            try:
                self.board.set_crocodiles(crocodile)
            except:
                continue

        for mine in mines:
            try:
                self.board.set_mines(mine)
            except:
                continue
    
    def add_winner(self, winner):
        self.winners.append(winner)


    """
    get mode of play, manual takes input from user and,
    automatic generates random dice values
    """
    def get_mode_of_play(self):
        mode_of_play = input(Msg.manual_or_automate_choice)
        if mode_of_play.lower() == Msg.yes :
            return False
        elif mode_of_play.lower() == Msg.no:
            return True
        else:
            raise Exception(ExceptionMessage.invalid_choice)

    """
    start game function, which iterate til it goes to game end,
    handling playing status of playersand executes the
    playing turns
    """
    def start_game(self):
        print(Msg.welcome)
        self.automate = self.get_mode_of_play()
        while True:
            for _, playerObject in self.players.items():
                if not playerObject.get_win_status():
                    if playerObject.get_holding_turns() == 0:
                        playerObject.play_move(self.dice, self.board, self.players, self.automate)
                        if self.board.get_player_status(playerObject.get_position()):
                            playerObject.set_win_status()
                            self.add_winner(playerObject.name)
                            print(f"{playerObject.name} wins the game !!")
                            self.active_players -= 1

                    else:
                        print(f"{playerObject.get_name()} stucked at mine, won't be playing")
                        update_holding_turns = playerObject.get_holding_turns() - 1
                        playerObject.set_holding_turns(update_holding_turns)

                if self.active_players < 2:
                    print(Msg.game_over)
                    sys.exit()
