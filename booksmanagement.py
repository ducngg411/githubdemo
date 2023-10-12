def book_management(books, total_sale):
    running =  True
    while running:
        print_menu()  
        choice = int(input('Enter your choice:'))
        if choice == 1:
            add_book(books)
        elif choice == 2:
            edit_price(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4: 
            total_sale = sell_book(books,total_sale)
        elif choice == 5:
            show_total_sales(total_sale)
        elif choice == 6:
            print_all(books)
        elif choice == 7:
            print('Program End')
            running = False
        else:
            print('Invalid Input, Try again')

def print_menu():
    print('1. Add a book')
    print("2. Edit a book's price")
    print('3. Search for a book by name')
    print('4. Sell a book')
    print('5. Show total sales')
    print('6. Print all books') 
    print('7. Quit')

def add_book(books):
    new_books = input('Enter a new books: ')
    books_price = float(input('Enter book prices: '))
    if new_books not in books:
        books[new_books] = books_price
        print('Book added successfully')
        print(books)
    else: 
        print(f'{books} is already in the store')

def edit_price(books):
    new_books = input('Enter name of books: ')
    new_price = float(input('Enter new price of books: '))
    if new_books in books:
        books[new_books] = new_price
        print('Books edited successfully!')
        print(books)
    else: 
        print(f'{books} not found')

def search_book(books):
    new_books = input('Enter name of books:')
    if new_books in books:
        print(f'Price of this books is {books[new_books]}')
    else: 
        print(f'Books not Found')

def sell_book(books,total_sale):
    delete_book = input('Enter name of books to sell: ')
    if delete_book in books:
        total_sale += books[delete_book]
        books.pop(delete_book)
        print(f'Sell successful: {delete_book}')
    else: 
        print(f'{delete_book} not found')
    return total_sale

def show_total_sales(total_sale):
    print(f"Total Sales: ${total_sale:.2f}")

def print_all(books):
    print('All books in store: ')
    for books, price in books.items():
        print(f'{books} : price: ${price:.2f}')


books = {'The Great Gatsby': 9.99, 'To Kill a Mockingbird': 7.99, '1984': 8.99, 'The Catcher in the Rye': 6.99}
total_sale = 0 
book_management(books, total_sale)