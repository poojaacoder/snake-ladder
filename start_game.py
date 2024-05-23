#!/usr/bin/env python

from src.services.game import Game
from src.constants.messages import FileName
from src.utils.read_file_helper import read_game_input_json

__author__     = "Pooja Deshmukh"


"""
main function, takes the json file FileName.input_file, as input and triggers the game
"""
def main():

    data = read_game_input_json(FileName.input_file)
    board_size = data['board_size']
    players_count = data['players_count']
    players = data['players_name']

    dice_faces = data['dice_faces']
    no_of_dice = data['no_of_dice']
    dice_stratergy = data['statergy']
    snakes_count = data['snakes']['count']
    snakes = []
    for pair in data['snakes']['pairs']:
        snakes.append(tuple(map(int,pair)))
    ladders_count = data['ladders']['count']
    ladders= []
    for pair in data['ladders']['pairs']:
        ladders.append(tuple(map(int,pair)))
    starting_positions = data['starting_positions']
    crocodiles = data['crocodiles']
    mines = data['mines']

    snake_ladder_game = Game(dice_faces, no_of_dice, dice_stratergy ,board_size )
    snake_ladder_game.set_players(players,starting_positions)
    snake_ladder_game.set_snake_ladders(snakes, ladders, crocodiles, mines)
    snake_ladder_game.start_game()


main()
