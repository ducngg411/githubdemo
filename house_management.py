# Global list for real estate data 
owners = ['John', 'Sara', 'Jessie', 'Mike']
prices = [110000, 120000, 3050000, 290000]
areas =[1400, 1170, 3890, 3200]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice:' ))
        if choice == 1:
            add_house()
        elif choice == 2:
            edit_price()
        elif choice == 3:
            sell_house()
        elif choice == 4:
            show_houses()
        elif choice == 5:
            print('Happy to do business with you!')
            running = False
        else:
            print('Invalid choice. Try again.')

def print_menu():
    print('1. Add house')
    print('2. Edit price')
    print('3. Sell a house')
    print('4. Show all house')
    print('5. Quit')

def add_house():
    owner = input('Enter owner name:')
    price = int(input('Enter price of house: '))
    area = int(input('Enter areas of house: '))

    owners.append(owner)
    prices.append(price)
    areas.append(area)

    print('Add House Successfully!')

def edit_price():
    print('Please enter the owner of the house to edit price:')
    owner = input('Owner: ')
    
    found = search_owner(owner)
    
    if found == -1:
        print('Owner not found.')
        return
    
    new_price = int(input('New price: '))
    prices[found] = new_price

    print('Price updated.')

def sell_house():
    print('Please enter the owner of the house to sell house:')
    owner = input('Owner: ')

    found = search_owner(owner)
    
    if found == - 1:
        print('Owner not found.')

    del owners[found]
    del prices[found]
    del areas[found]

    print('House sold!')

def search_owner(owner):
    for i in range(len(owners)):
        if owners[i] == owner:
            return i 
    return -1

def show_houses():
    print(f'{"Owner":20} | {"Price":10} | {"Area":10}')
    for i in range(len(owners)):
        print(f'{owners[i]:20} | {prices[i]:10} | {areas[i]:10}')


### Main ###

main()