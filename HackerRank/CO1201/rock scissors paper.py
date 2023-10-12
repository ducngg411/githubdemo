import random as rd

playing =  True 

while playing:

    user_choice = input('Chose on in (rock, scissors, or paper): ')

    if user_choice not in ['rock','scissors','paper']:
        print('invalid input')
    else:
        computer_choice = rd.randint(1,3)

        #method 2: 
        #computer_choice = 'rock' if computer_choice ==1 else \ 
        #'scissors' if computer_choice == 2 else 'paper'

        if computer_choice == 1:
            computer_choice = 'rock'
        elif computer_choice == 2:
            computer_choice = 'scissors'
        elif computer_choice == 3:
            computer_choice = 'paper'
    
    if user_choice == computer_choice:
        print('Draw')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        ( user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        print('You win')
    else:
        print('You lose')

    answer = input('Do you want to play again? (y/n):')
    playing == answer == 'y'

    # result = 'Win'
    # if user_choice == 'Rock' and computer_choice == 'Scissor':
    #     if user_choice == 'Scissor' and computer_choice == 'paper':
    #         if user_choice == 'Paper' and computer_choice == 'Rock':
    #             print(result)