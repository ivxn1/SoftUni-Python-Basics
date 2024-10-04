needed_book = input()
current_book = input()
checked_books = 0

while True:
    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {checked_books} books.')
        break

    if current_book != needed_book:
        checked_books += 1
        current_book = input()

    else:
        print('You checked', checked_books, 'books and found it.')
        break
