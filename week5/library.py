class book:
    
    
    def __init__ (self,title, author, ISBN, availablity_status, books_borrowed):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availablity_status = True
        self.books_borrowed=[]

    def detail(self):
        return (f'Title: {self.title} "\n" Author: {self.author} "\n" ISBN: {self.ISBN} "\n" Availablity_status: {self.availablity_status}')

    def update(self):
        if self.title in self.borrowed:
            self.availablity_status= False 
        else:
            pass


class user(book):
    
    def __init__(self,name,ID,books_borrowed_by_the_user,books_returned_by_the_user):
        self.name=name
        self.ID=ID
        self.books_borrowed_by_the_user=[]
        self.books_returned_by_the_user=[]
    
    
    def borrow_book(self):
       
        if self.availablity_status:
            self.books_borrowed_by_the_user.append(self.title)
            self.books_borrowed.append(self.title)
            availablity_status=False
            return(f"{self.name} has borrowed the book {self.title}")
        else:
            return(f"The book is not available.")
    
    def return_book(self):

        if self.title in self.books_borrowed_by_the_user:
            self.books_borrowed_by_the_user.remove(self.title)
            self.books_borrowed.remove(self.title)
            availablity_status=True
            return(f"{self.name} has returned the book {self.title}")
        else:
            return(f"you've not borrowed the book.")

    def detail(self):
        print (f'''user name: {self.name}
                   user ID: {self.ID}
                   books borrowed by {self.name}: ''')    
    
        for borrowed in books_borrowed_by_the_user:
            print(borrowed)
        print (f"Books returned by {self.name}:")
        for returned in books_returned_by_the_user:
            print(returned)




class library(user):
    
    def __init__(self, list_books, list_users):
        self.list_books=[]
        self.list_users=[]

    def add_student(self):
        
        self.name= input("enter the name of the student to be added: ")
        self.ID= input("enter the ID of the student to be added: ")
        self.list_students.append([self.name, self.ID])
        return(f"{self.name} is added successfully.")
    
    def add_book(self):

        self.title= input("Enter the title of the book to be added: ")
        self.author = input("Enter the author of the book to be added: ")
        self.ISBN = input("Enter the ISBN of the book to be added: ")
        self.list_books.append([self.title, self.author, self.ISBN])
        return(f"Book {self.title} is addded successfully.")

class transaction(user):

    def __init__(self,books_borrowed, books_returned):
        self.books_borrowed=[]
        self.books_returned=[]

    def borrowing(self):
        self.title= input("Enter the title of the book to be borrowed: ")
        self.author = input("Enter the author of the book to be borrowed: ")
        self.ISBN = input("Enter the ISBN of the book to be borrowed: ")
        self.name = input("Who is borrowing the book? ")
        self.books_borrowed_by_the_user.append(self.title)
        self.books_borrowed.append(self.title)
        availablity_status= False
   
    def returning(self):
                
        if self.title in self.books_borrowed:
            self.name= input("Who has borrowed the book? ")
            self.books_borrowed_by_the_user.remove(self.title)
            self.books_borrowed.remove(self.title)
            availablity_status=True
            return(f"{self.name} has returned the book {self.title}")
        else:
               return(f"The book hasn't been borrowed.")