import random 
from characters import characters

def randomItemPicker(password, length):
        for x in range(length):
            password.append(characters[random.randrange(0, len(characters))])