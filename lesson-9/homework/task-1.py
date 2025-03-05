import json
class Book:
    def __init__ (self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def to_dict(self):
        return {
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

class Member:
    def __init__ (self, name):
        self.name = name
        self.borrowed_books = []
    def to_dict(self):
        return {
            "borrowed_books": self.borrowed_books
        }
    
class Library():
    def __init__ (self, file=r"D:\Python\python-homework\lesson-9\homework\library.json"):
        self.file = file
        self.books = {}
        self.members = {}
        self.load_data()

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = Book(title, author)
            self.save_data()

    def add_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
            self.save_data()
            print("The book added successfully!")

    def borrowing_book(self, name, title):
        if name not in self.members:
            raise Exception("Member is not found")
        if title not in self.books:
            raise BookNotFoundException
        if self.books[title].is_borrowed:
            raise BookAlreadyBorrowedException
        if len(self.members[name].borrowed_books) > 3:
            raise MemberLimitExceededException
        
        self.books[title].is_borrowed = True
        self.members[name].borrowed_books.append(title)
        self.save_data()
        print("You borrowed the book")

    def returning_book(self, name, title):
        if title in self.members[name].borrowed_books:
            self.members[name].borrowed_books.remove(title)
            self.books[title].is_borrowed = False
            self.save_data()
            print("You returned the book!")

    def save_data(self):
        data = {
            "books": {title: book.to_dict() for title, book in self.books.items()},
            "members": {name: member.to_dict() for name, member in self.members.items()}
        }
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
                self.books = {title: Book(title, author) for title, author in data.get("books", {}).items()}
                self.members = {name: Member(name) for name in data.get("members", {})}
                for name, info in data.get("members", {}).items():
                    self.members[name].borrowed_books = info["borrowed_books"]
        except FileNotFoundError:
            self.books = {}
            self.members = {}


class BookNotFoundException(Exception):
    def __init__(self, message="Book is not found"):
        super().__init__(message)
        print(message)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message="The book is already borrowed"):
        super().__init__(message)
        print(message)

class MemberLimitExceededException(Exception):
    def __init__(self, message="Member cannot borrow more than 3 books"):
        super().__init__(message)
        print(message)


def menu():
    library = Library()
    while True:
        print("\nLIBRARY MENU")
        print("1. Becoming a member")
        print("2. Donating a book")
        print("3. Borrowing a book")
        print("4. Returning a book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            library.add_member(name)
            print("You become a member!")
        elif choice == "2":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)
        elif choice == "3":
            name = input("Enter your name: ")
            title = input("Enter the book title: ")
            library.borrowing_book(name, title)
        elif choice == "4":
            name = input("Enter your name: ")
            title = input("Enter the book title: ")
            library.returning_book(name, title)
        elif choice == "5":
            print("Thank you for choosing us")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()


