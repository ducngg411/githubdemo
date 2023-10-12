from random import randint

minimum = int(input("Min: "))
maximum = int(input("Max: "))

n_randoms = int(input("How many random numbers? "))
output = ""
for counter in range(n_randoms):
    random_value = randint(minimum, maximum)
    if random_value == 7:
        continue  
    elif random_value == 0:
        output = "Bad luck, no random values for you"  
        break
    else:
        output += f" {random_value}"  # Add the random number to the output string
print(output)

print()
input("Press return to continue ...")
