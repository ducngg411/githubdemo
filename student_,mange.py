# Student info 
student_id = [1111, 2222, 3333, 4444]
student_name = ['Duc', 'Dat', 'Khoa', 'Quang']
student_grade = [8.2, 9.0, 6.2, 4.3]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice:' ))
        if choice == 1:
            add_student()
        elif choice == 2:
            edit_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            search_student()
        elif choice == 5:
            show_all()
        else: 
            print('Invalid value, Try again!')        

def print_menu():
    print('STUDENT MANAGEMENT')
    print()
    print('1. Add student')
    print('2. Edit student')
    print('3. Delete student')
    print('4. Search by name')
    print('5. Show all')

def add_student():
    id = int(input('Enter student id: '))
    name = input('Enter student name: ')
    grade = float(input('Enter student grade: '))

    student_id.append(id)
    student_name.append(name)
    student_grade.append(grade)

    print('Add student successfully!')

def edit_student():
    print('To edit you need provide student name')
    name = input('Name: ')

    i = -1
    for i in range(len(student_name)):
        if student_name[i] == name:
            new_grade = float(input('Enter new grade: '))
            student_grade[i] == new_grade
            print(f'Student {name} updated!')
            return
    print(f'Student {name} not found!')
        
def delete_student():
    print('To edit you need provide student name')
    name = input('Name: ')

    i = -1 
    for i in range(len(student_name)):
        if student_name[i] == name:
            del student_id[i]
            del student_name[i]
            del student_grade[i]
            print('Delete successfully!')
            return
    print(f'Student {name} not found!')

def search_student():
    print('To edit you need provide student name')
    name = input('Name: ')

    i = -1
    for i in range(len(student_name)):
        if name in student_name[i]:
            print(f'Student: {name} | ID: {student_id[i]} | Grade: {student_grade[i]}')
        
    print(f'Student {name} not found!')

def show_all():
    print(f'{"ID":20} | {"Name":10} | {"Grade":10} |' )
    print(f'{"-"*20:20}  {"-"*12:10}  {"-"*12:10} ' )
    for i in range(len(student_name)):
        print(f'{student_id[i]:20} | {student_name[i]:10} | {student_grade[i]:10} |')

#### MAIN ####

main()
