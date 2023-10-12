age = int(input('Enter your real age:'))

if age < 18:
    print("You are not eligible to apply for a driver's license") 
if age > 18:
    print("You are eligible to apply for a driver's license.") 
if age >= 21: 
    print("You are also eligible to rent a car.")  
if age <21: 
    print("You need to be at least 21 years old to rent a car.")
else:
    print('Invalid Age')