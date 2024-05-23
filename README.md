## Snake Ladder Game

A python snake and ladder game, with additional hurdles of crocodile and mine

## Game Features

1. Snake always takes you to the cell where its tail is, and has to be a number less than
where you are at currently.

2. Ladder takes you up (strictly).

3. If a player (A) comes to a cell where another player (B) is placed already, the previously
placed player (B) has to start again from 1.

4. Crocodile, which takes you exactly 5 steps back.

5. Mine which holds you for 2 turns.

6. A manual override must exist for the interviewer to verify the edge cases/ to write unit
tests. The program should take the following as input:
Starting location of each player.
○ The D die values that each player rolled in a turn.

7. An override to manually enter the D die values that each player rolled in each turn.
(Absent in example. Any input format is fine)

## Instruction to run

1. `cd snake-ladder`
2. `pip3 install -r requirements.txt`
2. `python3 start_game.py`

## Unit tests

`python3 -m unittest tests/<file_name>`