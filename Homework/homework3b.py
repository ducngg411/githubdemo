print('Welcome to Duc Nguyen Bank, please enter your income and credit score, we will determine the eligibility for a loan')
user_income = int(input('Enter your income:'))
user_creditscore = int(input('Enter your credit score:'))

if user_income > 50.000 and user_creditscore > 700:
    print("You are eligible for a loan with low interest rates.")
elif user_income > 100000 :
    print("You are eligible for a loan with the lowest interest rates.")
elif user_income > 30000 and user_creditscore > 500:
    print("You are eligible for a loan with moderate interest rates.")
elif user_income < 30000 or user_creditscore < 500:
    print("Sorry, you are not eligible for a loan at this time.")
else: 
    print('Invalid income and creditscore')