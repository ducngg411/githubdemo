import string 

single_character = input('Enter a character from the alphabet: ')

#make a list of alphabet lowercase and uppercase
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

if single_character in alphabet:
    vowel = ('a','e','i','o','u','A','E','I','O','U')
    if single_character in vowel:
        print('Vowel')
    elif single_character != vowel:
        print('Consonant')
elif single_character != alphabet:
    print('Invalid')