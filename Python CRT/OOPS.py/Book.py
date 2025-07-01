'''
Write a python program to create a book class declare the states as
BookName
AuthorName
PublisherName
PublisherDate
CategoryOfBook
i) Create 5 objects & Initialize the values using Constructor where out of five
    -Create 1st object using one parameterized Constructor
    -Create 2nd object using two parameterized Constructor
    -Create 3rd object using three parameterized Constructor
    -Create 4th object using four parameterized Constructor
    -Create 5th object using five parameterized Constructor
ii) Access the values using Accessor Methods
iii) Update the values using Mutator method for Name of the Book
'''
class Book1:
    def __init__(self,bookname):
        self.Book_Name=bookname
    def Set_Book_Name(self):
        self.Book_Name='Python'
    def Get_Details(self):
        print(f"Book Name : {self.Book_Name}")
class Book2:
    def __init__(self,bookname,authorname):
        self.Book_Name=bookname
        self.Author_Name=authorname
    def Set_Book_Name(self):
        self.Book_Name='Python'
    def Get_Details(self):
        print(f"Book Name : {self.Book_Name}")
        print(f"Author Name : {self.Author_Name}")
class Book3:
    def __init__(self):
        print("Object is created")
class Book4:
    def __init__(self,bookname,authorname,publishername,publisherdate):
        self.Book_Name=bookname
        self.Author_Name=authorname
        self.Publisher_Name=publishername
        self.Publisher_Date=publisherdate
    def Set_Book_Name(self):
        self.Book_Name='Python'
    def Get_Details(self):
        print(f"Book Name : {self.Book_Name}")
        print(f"Author Name : {self.Author_Name}")
        print(f"Publisher Name : {self.Publisher_Name}")
        print(f"Publisher Date : {self.Publisher_Date}")
class Book5:
    def __init__(self,bookname,authorname,publishername,publisherdate,categoryofbook):
        self.Book_Name=bookname
        self.Author_Name=authorname
        self.Publisher_Name=publishername
        self.Publisher_Date=publisherdate
        self.Category_of_Book=categoryofbook
    def Set_Book_Name(self):
        self.Book_Name='Python'
    def Get_Details(self):
        print(f"Book Name : {self.Book_Name}")
        print(f"Author Name : {self.Author_Name}")
        print(f"Publisher Name : {self.Publisher_Name}")
        print(f"Publisher Date : {self.Publisher_Date}")
        print(f"Category of Book : {self.Category_of_Book}")
B1=Book1("Java")
B1.Set_Book_Name()
B1.Get_Details()
print("-------------------")
B2=Book2("Java","R.D.Sharma")
B2.Set_Book_Name()
B2.Get_Details()
print("-------------------")
B3=Book3()
print("-------------------")
B4=Book4("Java","R.D.Sharma","Mukesh Publishers","09-06-2005")
B4.Set_Book_Name()
B4.Get_Details()
print("-------------------")
B5=Book5("Java","R.D.Sharma","Mukesh Publishers","09-06-2005","Education")
B5.Set_Book_Name()
B5.Get_Details()
print("-------------------")