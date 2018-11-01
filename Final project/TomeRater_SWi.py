class User:
    def __init__(self, name, email):
        self.books = {}
        self.name = name
        self.email = email

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", number of books read: " + str(len(self.books))
        
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
    
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(self.name + "'s email has been updated!")

    def read_book(self, book, rating="None"):
        self.books[book] = rating
    
    def get_average_rating(self):
    # Improvement! Handling of "None" as a string
        total = 0
        none_count = 0
        for rating in self.books.values():
            if rating != "None":
                total += rating
            else:
                none_count += 1
        return total / (len(self.books) - none_count)
    
    def get_books(self):
        return self.books

class Book:
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price 

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    # Improvement!  Missing string representation     
    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    #Additional method to get price
    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book titled " + self.title + " updated isbn to " + str(self.isbn))

    #Improvement! Additional method - prices can change
    def set_price(self, new_price):
        self.price = new_price
        print("The book titled " + self.title + " updated price to " + str(self.price))
    
    def add_rating(self, rating):
        if rating >= 0 and rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid Rating, rating should be from 0 to 4")

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        return total / len(self.ratings)
      
class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        Book.__init__(self, title, isbn, price)
        self.author = author

    def __repr__(self):
        return self.title + " by " + self.author

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        Book.__init__(self, title, isbn, price)
        self.subject = subject
        self.level = level
    
    def __repr__(self):
        return self.title + " a " + self.level + " manual on " + self.subject
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn, price):
        new_book = Book(title, isbn, price)
        return new_book

    def create_novel(self, title, author, isbn, price):
        new_Fiction = Fiction(title, author, isbn, price)
        return new_Fiction

    def create_non_fiction(self, title, subject, level, isbn, price):
        new_Non_Fiction = Non_Fiction(title, subject, level, isbn, price)
        return new_Non_Fiction

    def add_book_to_user(self, book, email, rating="None"):
        if email in self.users.keys():
            user = self.users[email]
            user.read_book(book, rating)
            if rating != "None":
                book.add_rating(rating)
            
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + email)  

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read_number = 0

        for book in self.books.keys():
            if self.books[book] > most_read_number:
                most_read_number = self.books[book]
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_book = book
                highest_rating = rating
        return highest_book

    def most_positive_user(self):
        highest_rating = 0
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > highest_rating:
                highest_user = user
                highest_rating = rating
        return highest_user   

    def add_user(self, name, email, user_books="None"): 
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books != "None":
            for book in user_books:
                self.add_book_to_user(book, email)

    # Additional methods
    def get_n_most_expensive_books(self, n):
        highest_price_books = []
        books_tmp = {}

        for book in self.books:
            books_tmp[book.get_price()] = book

        sorted_keys = sorted(books_tmp.keys(), reverse=True)

        for key in sorted_keys:
            if len(highest_price_books) < n:
                highest_price_books.append(books_tmp[key])
            else:
                break
        return highest_price_books
        
    def get_worth_of_user(self, user_email):
        total_cost = 0
        user = self.users[user_email]

        for book in user.get_books():
            total_cost += book.get_price()
            #Improvement! round 2 decimal places
        return round(total_cost, 2)

#Additional improvement for TomeRater would be to introduce validity checking for parameters passed to methods example: price can't be a negative number