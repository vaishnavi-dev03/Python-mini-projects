print("-----LIBRARY MANAGEMENT SYSTEM-----")
books=[]
def add_book():
    notebook=input("Enter the book name: ")
    author=input("Enter the author name: ")
    book={
        "book":notebook,
        "author":author,
        "available":True
    }
    books.append(book)
def view_book():
    for index,book in enumerate(books,start=1):
        print(index,book["book"],"-",book["author"])
def search_book():
    search=input("Enter the book name: ")
    author_name=input("Enter the author name: ")
    if search and autho
        print("Book found")
    else:
        print("Book is not available in library")

print("1.Add Books")
print("2.View Books")
print("3.Search Book")
print("4.Issue Book")
print("5.Return Book")
print("6.Delete Book")
print("7.Exit")
