class Library:
    book_list = []
    def entry_book(self, title, author):
        id = len(self.book_list)+101
        availability = 'Available'
        bk = Book(id, title, author, availability)
        self.book_list.append(bk)

    def view_book_info(self):
        print("\nLibrary Books: ")
        for i in self.book_list:
            i.view_book_info()

    def borrow_bk(self,id):
        for i in self.book_list:
            if i._book_id == id:
                i.borrow_book()
                return
        print("Invalid Book_ID")

    def return_bk(self,id):
        for i in self.book_list:
            if i._book_id == id:
                i.return_book()
                return
        print("Invalid Book_ID")

class Book():
    def __init__(self, book_id, title, author, availability):
        self._book_id = book_id
        self.__title = title
        self.__author = author
        self._availability = availability
        
    def borrow_book(self):
        if self._availability == 'Not Available':
            print(f'Book {self.__title} is Not Available')
        else:
            self._availability = 'Not Available'
            print(f'Book {self.__title} has been borrowed successfully.')

    def return_book(self):
        if self._availability == 'Available':
            print(f'Book {self.__title} has not been Borrowed')
        else:
            self._availability = 'Available'
            print(f'Book {self.__title} has been returned successfully.')

    def view_book_info(self):
        print(f'ID: {self._book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {self._availability}')



lib = Library()
lib.entry_book('Python Programming','John Doe')
lib.entry_book('Data Science Essentials','jane Smith')
lib.entry_book('Machine Learning','Alan Turing')
lib.entry_book('Artificial Intelligence','Marvin Minsky')
lib.entry_book('Deep Learning','Yann LeCun')
lib.entry_book('Cloud Computing','Christopher Manning')
lib.entry_book('Statistics for Data Scince','David C. Hsu')
lib.entry_book('Cyber Security','Wes Mckinney')
lib.entry_book('Power','Robert Greene')
lib.entry_book('Surrounded by Idiots','Thomas Erikson')

while True:
    print('\n________Welcome to the Library________')
    print('1. View All Books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit\n')

    a=int(input('Enter your choice : '))
    if a == 1:
        lib.view_book_info()
    elif a == 2:
        b=int(input('Enter Book_id : '))
        lib.borrow_bk(b)
    elif a == 3:
        b=int(input('Enter Book_id : '))
        lib.return_bk(b)
    elif a == 4:
        break
    else:
        print('Invalid Choice')