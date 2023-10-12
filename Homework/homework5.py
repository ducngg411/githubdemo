students = ['John','Peter','Mary','Jane','Tom','Jerry','Alice','Bob']
departments = ['IT','GD','IT','Biz','Biz','GD','IT','GD']
GPAs = [3.5, 3.0, 3.2,2.6, 3.8, 3.9, 3.7, 3.4]

# Enter department name, find students in that department and print their names and GPAs
name = input('Enter the department name: ')
found_de = []
found_departments = None

for i in range(len(departments)):
    if departments[i] == name:
        found_departments = i
        found_de.append[found_departments]
        break
    
if found_departments == None:
    print(f'Departments {name} not found')

else:
    print(f'Student name: {students[found_departments]}, GPAs: {GPAs[found_departments]}')