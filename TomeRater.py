class User():
#Constructor
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.books = {} # maps {{book object : Rating}, ...}

#get_email method: returns user's email
    def get_email(self):
        return self.email

#change_email method: change user's email
    def change_email(self, address):
        email_domain = [".com", ".edu", ".org"]
        valid_email = False
        if '@' in address:
            for dom in email_domain:
                if dom in address:
                    self.email = address
                    print("{}'s new email: {}".format(self.name, self.email))
                    valid_email = True
                    break

        if not valid_email:
            print("Invalid email. {}'s email has not been changed".format(self.name))

#__repr__ dunder method: prins User: name email: email Read books: books
    def __repr__(self):
        return "User: " + self.name + "\nEmail: " + str(self.email) + "\nNumber of read books: " + str(len(self.books.keys()))

#__eq__ dunder mcethod: returns true if name and email are equal when comparing two users instances
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

# read book method: adds book and rating(optional) to self.books dict
    def read_books(self, book, rating=None):
        if book.isbn_diff(self.books.keys()):
            if book in self.books.keys():
                print("The book is already in {user}'s list. Rating will be updated (if provided)".format(user=self.name))
                if rating != None:
                    self.books[book] = rating
            else:
                print("{} has been added to {}'s read books".format(book, self.name))
                self.books[book] = rating
        else:
            print("Error. There is another book with the same ISBN in your list of books.")

# get_average_rating method: calculate the average rating of all books and return this average
    def get_average_rating(self):
        count = 0
        total_sum = 0

        for rating in self.books.values():        # iterates through rating of each book
            if rating != None:
                total_sum += rating
                count += 1
        return total_sum / count

#class Book
class Book():
# Contructor
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

# get title method: returns book's title
    def get_title(self):
        return self.title

# get isbn method: returns book's isbn
    def get_isbn(self):
        return self.isbn

# set_isbn: changes the isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{}'s new ISBN: {}".format(self.title, self.isbn))

# add_rating method: appends rating to list: ratings if it is a valid entry
    def add_rating(self, rating):
        if 0 <= rating <= 4 :
            self.rating.append(rating)
        else:
            print("Invalid rating. Please rate from 0 and 4")

# __eq__ dunder method: compares two instances of class Book and return true if title and isbn are equal
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
# __repr__ dunder method: returns title and ISBN.
    def __repr__(self):
        return self.title

# get_average_rating method: return the average of all the book's ratings
    def get_average_rating(self):
        rating_len = len(self.rating)
        total_sum = 0

        for rating in self.rating:
            total_sum += rating
        try:
            rating = total_sum / rating_len
        except ZeroDivisionError:
            #print("{} has not been rated yet.".format(self.title))
            rating = -1
        return rating

# __hash__ dunder method: it makes title and isbn hashable obcjets
    def __hash__(self):
        return hash((self.title, self.isbn))

# isbn_diff method: Checks that the isbn of the book is not already in a list of books
    def isbn_diff(self,lst_books):
        for book in lst_books:
            if self.isbn == book.isbn and self.title != book.title:
                return False
        return True


# Fiction class: a subclass of Book
class Fiction(Book):
# Constructor
    def __init__(self, title, author, isbn):

        super().__init__(title, isbn)
        self.author = author

# __repr__ dunder method: returns title by author.
    def __repr__(self):
        return self.title + " by " + self.author


# Non-Fiction class: a subclass of Book
class NonFiction(Book):
#Constructor
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

# get_subject method: returns book's subject
    def get_subject(self):
        return self.subject

# get_level method: returns level of book
    def level(self):
        return self.level

# __repr__ dunder method: returns title, a level manual on subject
    def __repr__(self):
        return self.title + ", " + str(self.level) + " manual on " + self.subject

# class TomeRater
class TomeRater():
#Constructor
    def __init__(self):
        self.users = {} # {{email: user object, },...}
        self.books = {} # {{Book object: number of users who have read it}, }

# create_book method: creates an instance of Book class
    def create_book(self, title, isbn):
        return Book(title, isbn)

# create_novel method: creates an instance of Fiction class
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

# create_non_fiction method: creates an instance of NonFiction class
    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

# add_book_to_user method: adds book and rating to an user. If book has unique ISBN, it is added to self.books
    def add_book_to_user(self, book, email, rating=None):
        if book.isbn_diff(self.books.keys()):
            if self.users.get(email):
                self.users[email].read_books(book, rating)
                if self.books.get(book):
                    self.books[book] += 1
                else:
                    self.books[book] = 1
            else:
                print("Not user with email: " + str(email))
            if rating != None:
                book.add_rating(rating)
        else:
            print("Error. Duplicated ISBN. A book with the same ISBN already exists")

# add_user method: creates an instance of user and add list of books to user(optional).
#                  Method checks if the user already exist and if it is valid.
    def add_user(self, name, email, user_books = None):
        email_domain = [".com", ".edu", ".org"]
        valid_email = False
        if not self.users.get(email):
            if '@' in email:
                for dom in email_domain:
                    if dom in email:
                        self.users[email] = User(name, email)
                        print("User {} has been added".format(name))
                        valid_email = True
                        break

            if not valid_email:
                print ("Invalid email: {email}. {user} user has not been added.". format(email=email, user=name))

        else:
            print("User with email {} already exists. Pleas check email.".format(email))
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

# Analysis methods
# print_catalog method: prints all books
    def print_catalog(self):
        print("Book Catalog: \n")
        for book in self.books.keys():
            print(book)

# print_user: prints all users
    def print_users(self):
        print("\nUsers List: \n")
        for user in self.users.values():
            print(user)

# most_read_books method: returns the most read book
    def most_read_book(self):
        most_read = None
        max_number =0
        for book, number in self.books.items():
            if number > max_number:
                max_number = number
                most_read = book
        return most_read

# highest_rated_book method: returns book with highest average rating
    def highest_rated_book(self):
        best_rated = None
        highest_rating = 0

        for book in self.books.keys():
            book_avg_rating = book.get_average_rating()
            if book_avg_rating > highest_rating :
                highest_rating = book_avg_rating
                best_rated = book
        return best_rated

# most_positive_user method: returns the user who has given the highest average rating
    def most_positive_user(self):
        most_pos_user = None
        best_avg = 0

        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating > best_avg:
                best_avg = avg_rating
                most_pos_user = user
        return most_pos_user.name


















