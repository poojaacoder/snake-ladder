from src.constants.board_objects import BoardObjects


def player_move(player, dice_face, initial_pos, final_pos, action):
    if initial_pos != final_pos:
        if action == BoardObjects.snake:
            return f"{player} rolled a {dice_face} and bitten by snake at {initial_pos + dice_face} and moved from {initial_pos} to {final_pos}"
        elif action == BoardObjects.ladder:
            return f"{player} rolled a {dice_face} and climbed the ladder at {initial_pos + dice_face} and moved from {initial_pos} to {final_pos}"
        elif action == BoardObjects.crocodile:
            return f"{player} rolled a {dice_face} and eaten by crocodile at {initial_pos + dice_face} and moved from {initial_pos} to {final_pos}"
        elif action == BoardObjects.mine:
            return f"{player} rolled a {dice_face} and end up going in mine {initial_pos + dice_face} , so will be waiting at {initial_pos} and won't play for next 2 turns"
        else:
            return f"{player} rolled a {dice_face} and moved from {initial_pos} to {final_pos}"

    return f"{player} rolled a {dice_face} and but can't move from {initial_pos}"
