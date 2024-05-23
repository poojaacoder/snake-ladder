import random
from src.constants.messages import Msg


class Dice:

    def __init__(self, faces, no_of_dices, dice_stratergy):
        self.faces = faces
        self.no_of_dices = no_of_dices
        self.dice_stratergy = dice_stratergy

    def get_dice_face(self, player, is_automate):
        if is_automate == True:
            return self.get_random_face()
        else:
            print(f"{player}'s turn")
            dice_value = int(input(Msg.enter_face_dice_value))
            if dice_value > self.faces:
                print(Msg.invalid_dice, self.faces)
                dice_value = int(input(Msg.enter_value_again))
            print
            return int(dice_value)


    def get_random_face(self):
        while True:
            dice_score = random.randint(1, self.faces)  
            return dice_score
    

    def get_dice_face_result(self, player, is_automate):
       if self.dice_stratergy == "MAX":
           return self.get_dice_max(player, is_automate)
       elif self.dice_stratergy == "MIN":
           return self.get_dice_min(player, is_automate)
       elif self.dice_stratergy == "SUM":
           return self.get_dice_sum(player,is_automate)


    def get_dice_max(self, player, is_automate):
        max = 0
        for i in range(self.no_of_dices):
            print(i)
            value = self.get_dice_face(player,is_automate)
            if max < value:
                max = value
        return max 
    

    def get_dice_min(self, player, is_automate):
        min = 0
        for i in range(self.no_of_dices):
            if min > self.get_dice_face(player,is_automate):
                min = self.get_dice_face(player,is_automate)
            else:
                continue

        return min 

    def get_dice_sum(self, player, is_automate):
        sum = 0
        for i in range(self.no_of_dices):
            sum =  sum + self.get_dice_face(player,is_automate)
        return sum

                