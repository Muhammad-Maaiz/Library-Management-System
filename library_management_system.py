# LIBRARY MANAGEMENT SYSTEM:
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []
        print("Library Management System Menu:\n".center(80))

    def add_book(self):
        """Add a new book to the library."""
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        year = int(input("Enter the publication year: "))
        self.books.append({"title": title, "author": author, "year": year})
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        """Display all books available in the library."""
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

    def remove_book(self):
        """Remove a book from the library."""
        self.display_books()
        choice = int(input("Enter the number of the book to remove: "))
        if 1 <= choice <= len(self.books):
            removed_book = self.books.pop(choice - 1)
            print(f"Book '{removed_book['title']}' has been removed from the library.")
        else:
            print("Invalid Book Number.")

    def num_of_books(self):
        """Display the total number of books in the library."""
        print(f"Number of books in the library: {len(self.books)}")

    def show_menu(self):
        """Show the menu options to the user."""
        print("\nMenu")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Remove a book")
        print("4. Number of books in the library")
        print("5. Exit")

    def run(self):
        """Run the Library Management System."""
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                self.remove_book()
            elif choice == '4':
                self.num_of_books()
            elif choice == '5':
                print("Exiting the Library Management System. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    my_library = Library()
    my_library.run()