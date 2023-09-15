# In a library system, you can have an association relationship between the "Book" class and the "Author" class. Each book is associated with one or more authors. This allows you to track the authors of a book and their contributions.

# A
class Book:
    def __init__(self, title, authors):
        self.title = title
        self.authors = Author()
        self.authors = authors

# B
class Author:
    def __init__(self, name):
        self.name = name
    

def main():
    an_author = Author("F. Scott Fitzgerald") #B
    a_book = Book("The Great Gatsby", an_author) #A
