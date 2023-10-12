a, b = map(int, input().split())
c = []
d = []

i = 1
while i <= a:
    if a % i == 0:
        c.append(i)
    while i <= b:
        if b % i == 0:   
            d.append(i)
        i += 1
        break

checkduplicate = set(c) & set(d)
print(max(checkduplicate))