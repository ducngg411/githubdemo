english = float(input('Enter your english score:'))
math = float(input('Enter your math score:'))
literature = float(input('Enter your literature score:'))
get_rank = [english, math, literature]
average_score = sum(get_rank) / 3
if  0 > english or english  > 10:
    print('invalid grade')
elif 0 > math or math  > 10:
    print('invalid grade')
elif 0 > literature or literature  > 10:
    print('invalid grade')    
elif average_score < 4.0:
    print('failed')
elif 4.0 <= average_score <= 6.5:
    print('pass')
elif 6.5 < average_score < 8.0:
    print('merit')
elif 8.0 <= average_score <= 10:
    print('distinction')


