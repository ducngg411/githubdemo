import random as rd

name = False

while not name:
    number = rd.randint(1, 100)
    print('Your lucky number is', number)

    answer = input("Enter your name: ")
    name = answer == ""