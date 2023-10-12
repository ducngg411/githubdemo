from random import *
from string import *

while True:
    strength = int(input("Strength [0 to terminate]? "))
    if strength == 0:
        break
    if strength > 10:
        length = 20
    else:
        length = strength*2
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = letters
    if strength >= 2:
        characters += letters.upper()
    elif strength >= 5:
        characters += "0123456789"
    if strength >= 7:
        characters += punctuation
    password = ""
    for i in range(length):
        r = randint(0, len(characters)-1)
        password += characters[r]
    print(f"Your password is {password}")