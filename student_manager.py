def student_manager():
    names = []
    gpas = []

    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice:'))
        if choice == 1:
            add_student(names, gpas)
        elif choice == 2:
            delete_student(names,gpas)
        elif choice == 3:
            edit_student(names,gpas)
        elif choice == 4:
            search_student(names,gpas)
        elif choice == 5:
            print('Program ends')
            running = False
        else:
            print('Invalid choice, try again')

def print_menu():
    print('1. Add student')
    print('2. Delete student')
    print('3. Edit student')
    print('4. Search student')
    print('5. Quit')

def add_student(names, gpas):
    name = input('Enter student name: ')
    gpa = float(input('Enter student GPA:'))
    names.append(name)
    gpas.append(gpas)
    print(f'Student {name} added')

def delete_student(names, gpas):
    name = input('Enter student name:')
    for i in range(len(names)):
        if names[i] == name:
            names.pop(i)
            gpas.pop(i)
            print(f'Student {name} deleted')
            return
    print(f'Student {name} not found')

def edit_student(names, gpas):
    name = input('Enter student name: ')
    for i in range(len(names)):
        if name[i] == name:
            new_gpa = float(input('Enter new GPA: '))
            gpas[i] = new_gpa
            print(f'Student {name} updated')
            return
    print(f'Student {name} not found')

def search_student(names, gpas):
    gpa = float(input('Enter GPA: '))
    for i in range(len(names)):
        print(f'{names[i]}: GPA ')

student_manager()