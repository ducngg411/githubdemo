students = ['John','Peter','Mary','Jane','Tom','Jerry','Alice','Bob']
departments = ['IT','GD','IT','Biz','Biz','GD','IT','GD']
GPAs = [3.5, 3.0, 3.2,2.6, 3.8, 3.9, 3.7, 3.4]

# Enter student name, find students and print his/her GPA and department
#Enter the product name, print the price & stock
name = input('Enter the student name: ')
found_students = None
for i in range(len(students)):
    if students[i] == name:
        found_students = 1
        break
if found_students == None:
    print(f'Students {name} not found')
else:
    print(f'departments: {departments[found_students]}, GPAs: {GPAs[found_students]}')
        

# Enter department name, find students in that department and print their names and GPAs

name = input('Enter the department name: ')

for i in range(len(students)):
    if departments[i] == name:
        print(f"Student Name: {students[i]}', 'GPA: {GPAs[i]}")




# Find best student (highest GPA)

i_max = 0
GPA_max = GPAs[0]

for i in range(len(GPAs)):
    if GPAs[i] > GPA_max:
        GPA_max = GPAs[i]
        i_max = i

print(f'The best students that has the highest GPA is {students[i_max]} with price {GPA_max}')


# Calculate average GPA of students in all departments

average_gpa = sum(GPAs) / len(GPAs)

print(f'Average GPA: {average_gpa:.2}')


