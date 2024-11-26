class Book:

  def __init__(self, id, title, author, price):
    self.id = id
    self.title = title
    self.author = author
    self.price = price
    self.next = None

  def __str__(self):
    return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Price: R${self.price:.2f}"


class BookStore:

  def __init__(self):
    self.head = None
    self.init_bookstore()

  def init_bookstore(self):
    books_initial = [(1, "Harry Potter", "J. K. Rolling", 20.50),
                     (2, "Lord of the Rings", "J. R. R. Tolkien", 15.80),
                     (3, "To Kill a Mockingbird", "Harper Lee", 12.20),
                     (4, "The Great Gatsby", "F. Scott Fitzgerald", 18.00),
                     (5, "1984", "George Orwell", 22.50)]
    previous = None
    for id, title, author, price in books_initial:
      new_book = Book(id, title, author, price)
      if self.head is None:
        self.head = new_book
      else:
        previous.next = new_book
      previous = new_book

  def add_book(self, id, newId, newTitle, newAuthor, newPrice):
    current_book = self.head
    while current_book:
      if current_book.id == newId:
        raise ValueError("Book with this ID already exists.")
      current_book = current_book.next

    new_book = Book(newId, newTitle, newAuthor, newPrice)
    
    if not self.head:
      self.head = new_book
      return
    
    current_book = self.head
    found = False
    while current_book:
      if current_book.id == id:
        found = True
        new_book.next = current_book.next
        current_book.next = new_book
        break
      current_book = current_book.next
    
    if not found:
      raise ValueError("Book with this ID not found.")

  def remove_book(self, id):
    current_book = self.head
    previous_book = None

    while current_book and current_book.id != id:
      previous_book = current_book
      current_book = current_book.next

    if current_book is None:
      raise Exception("Book not found.")
      
    if previous_book is None:
      self.head = current_book.next
    else: 
      previous_book.next = current_book.next

    print(f"Book with ID {id} removed.")

  def list_books(self):
    books = []
    current_book = self.head
    while current_book:
      books.append(current_book)
      current_book = current_book.next
    return books

  def first_book(self):
    return self.head

  def print_bookstore(self):
    current_book = self.head
    while current_book:
      print(current_book)
      current_book = current_book.next

  def search_book_by_id(self, id):
    current_book = self.head
    while current_book:
      if current_book.id == id:
        print("Book found:")
        print(current_book)
        if current_book.next:
          print("Next book in the list:")
          print(current_book.next)
        else:
          print("This is the last book in the list.")
        return
      current_book = current_book.next
    print("Book not found.")


def main():
  book_store = BookStore()

  while True:
    print("\nBook Store Management")
    print("1. List all books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Search for a book by ID")
    print("5. Exit")
  
    choice = int(input("Enter your choice: "))
  
    if choice == 1:
      print("\nList of all books:")
      book_store.print_bookstore()
    elif choice == 2:
      id = int(input("Enter the ID of the book to add after: "))
      newId = int(input("Enter the new ID: "))
      newTitle = input("Enter the new title: ")
      newAuthor = input("Enter the new author: ")
      newPrice = float(input("Enter the new price: "))
      book_store.add_book(id, newId, newTitle, newAuthor, newPrice)
      print("Book added successfully.")
    elif choice == 3:
      id = int(input("Enter the ID of the book to remove: "))
      book_store.remove_book(id)
    elif choice == 4:
      id = int(input("Enter the ID of the book to search: "))
      book_store.search_book_by_id(id)
    elif choice == 5:
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()