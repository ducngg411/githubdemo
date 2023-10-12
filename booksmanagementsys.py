def book_management():
    names = []
    genres = []
    authors = []
    publication_years = []

    running =  True
    while running:
        print_menu()  
        choice = int(input('Enter your choice:'))
        if choice == 1:
            add_book(names,authors, genres, publication_years )
        if choice == 2:
            delete_book(names,authors, genres, publication_years )
        if choice == 3:
            edit_book(names,authors, genres, publication_years)
        if choice == 4:
            search_book(names,authors, genres, publication_years)
        if choice == 5: 
            print_book_with_year(names,authors, genres, publication_years)
        if choice == 6:
            print('Program End')
            running = False
        else:
            print('Invalid Input, Try again')

def print_menu():
    print('1. Add book')
    print('2. Delete book')
    print('3. Edit book')
    print('4. Search books by genre')
    print('5. Print book by publication year')
    print('6. Quit') 

def add_book(names,authors, genres, publication_years ):
    name = input('Enter the title of book:')
    author = input('Enter the authors: ')
    genre = input('Enter book genre:')
    publication_year = int(input('Enter the publication year'))
    names.append(name)
    authors.append(author)
    genres.append(genre)
    publication_years.append(publication_year)
    print(f'Book "{name}" added ')
    
def delete_book(names,authors, genres, publication_years):
    name = input('Enter the title of books: ')
    for i in range(len(names)):
        if names[i] == name:
            names.pop[i]
            authors.pop[i]
            genres.pop[i]
            publication_years.pop[i]
            print(f'Book "{name}" deleted')
            return
    print(f'Book {name} not found')
    
def edit_book(names,authors, genres, publication_years):
    name = input('Enter book title: ')
    for i in range(len(names)):
        if names[i] == name:
            author = input('Enter new authors: ')
            authors[i] == author
            genre = input('Enter new genre:')
            genres[i] = genre
            publication_year = int(input('Enter new publication year'))
            publication_years[i] = publication_year
            print(f'Book "{name} updated')
            return
    print(f'Book {name} not found')
        
def search_book(names,authors, genres):
    genre = input('Enter genre to search:')
    for i in range(len(genres)):
        if genres[i] == genre:
            print(f'Book found under genre "{genre}"')
            print(f'{names[i]} by {authors[i]}')
        else: 
            print('Invalid genre')

def print_book_with_year(names,authors,publication_years):
    for i in range(publication_years):
        print('Book sorted by publication year:')
        print(f'{names[i]} by {authors[i] ({publication_years})}')

