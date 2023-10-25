from abc import ABC, abstractmethod

# Abstract base class for LibraryItem
class LibraryItem(ABC):
    def __init__(self, title, author_or_director):
        self.title = title
        self.author_or_director = author_or_director
        self.checked_out = False

    @abstractmethod
    def check_out(self, student):
        pass

# Derived class Book
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    def check_out(self, student):
        if not self.checked_out:
            print(f"{student.name} has checked out the book: '{self.title}' by {self.author_or_director}.")
            self.checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

class DVD(LibraryItem):
    def __init__(self, title, director):
        super().__init__(title, director)

    def check_out(self, student):
        if not self.checked_out:
            print(f"{student.name} has checked out the DVD: '{self.title}' directed by {self.author_or_director}.")
            self.checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

class Student:
    def __init__(self, name):
        self.name = name

    def check_out_item(self, library_item):
        library_item.check_out(self)

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
dvd1 = DVD("Inception", "Christopher Nolan")

student1 = Student("Kalyani")

student1.check_out_item(book1)
student1.check_out_item(dvd1)
student1.check_out_item(book1)  # Trying to check out the same book again
