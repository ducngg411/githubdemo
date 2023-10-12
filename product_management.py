def product_management(products):
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_product(products)
        elif choice == 2:
            edit_product(products)
        elif choice == 3:
            delete_product(products)
        elif choice == 4:
            filter_product(products)
        elif choice == 5:
            print_all(products)
        elif choice == 0:
            print('Program ends')
            running = False
        else: 
            print('Invalid choice, try again')

def print_menu():
    print('1. Add product')
    print('2. Edit product')
    print('3. Delete product')
    print('4. Filter product')
    print('5. Print all')

def add_product(products):
    name = input('Enter new product name: ')
    if name in products:
        print('Product {name} already exists')
        return
    price = float(input('Enter new product price: '))
    products[name] = price 
    print(f'Product {name} added successfully.')
    print(products)

def edit_product(products):
    name = input('Enter name of product: ')
    if name in products:
        new_price = float(input('Enter a new price: '))
        products[name] = new_price
        print(f'New price of {name} is {new_price}')
    else:
        print(f'Product {name} not found')
        
def delete_product(products):
    name = input('Enter name of product you want to delete:')
    if name in products:
        products.pop(name)
        print(products)
        print(f'Delete {name} successfully')
    else:
        print(f'Product {name} not found')

# method 1
def filter_product(products):
    filter_price = float(input('Enter price to filter: '))
    for name, price in products.items():
        if price >= filter_price:
            print(f'{name} - {price}')
    else:
        print('No product have this price')
    
# method 2
# def filter_product(products):
#     filter_price =  float(input('Enter price to filter: ')
#     for name in products:
#         price = products[name]:
#         if price >= filter_price:
#             print(f'{name} - {name}')

def print_all(products):
    for name, price in products.items():
        print(f'{name} - {price}')

products = {'Computer': 100, 'Keyboard': 200, 'Mouse': 10, 'Monitor': 500}
product_management(products)