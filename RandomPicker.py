import random as r

class RandomPicker():
    def __init__(self, data):
        self.total_award = []
        self.data = data
    
    def pick_winner(self, num):
        award = []
        while len(award) < num:
            pass