import colorama
from colorama import Fore, Back, Style, init

def menu():
    init(autoreset=True)
    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║       📚  LIBRARY MANAGEMENT SYSTEM  📚      ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print("1.Add Book")
    print("════"*12)
    print("2.View Added Books")
    print("════"*12)
    # print("3.Search Book")
    # print("════"*12)
    print("3.Register Book")
    print("════"*12)
    print("4.View Registerd Books")
    print("════"*12)
    print("5.Exit")
    print(Fore.CYAN + "════"*12)

book_data = [] #initialization
def read_book():
    try:
        with open("book_data.txt","r") as f:
            book_data = f.readlines()
        return book_data
    except FileNotFoundError:
        book_data = []
        return book_data

def addbook():
    #Dockstring
    """This is book function that contain Bookname , bookid , bookauthor , bookquantity"""
    book_data = read_book()
    print(Fore.GREEN + "---Add Book---")
    book_id = len(book_data) + 1
    print(f"Book Id  : {book_id}")
    book_name = input("Enter Book name  :").strip().title()
    for i in book_data:
        if book_name in i:
            print(Fore.GREEN + "This book already exists")
            print(Fore.RED + "Terminating this Function")
            return False
    book_author = input("Enter the author name  :").strip().title()
    book_quantity = input("Enter Quantity  :").strip()
    while True:
        if book_quantity.isdigit():
            if int(book_quantity) > 0:
                break
            else:
                print(Fore.RED + "Quantity can not be '0'")
                return False
        else:
            print(Fore.RED + "INVALID QUANTITY \nEnter a valid number")
            return False
    print(Fore.GREEN + Style.BRIGHT + f"---{"Book added Sucessfully"}---")

    with open("book_data.txt","a") as file:
        file.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")

def view_book():
    book_data = read_book()
    print(Fore.LIGHTYELLOW_EX + "Book-id , Book-Name , Book-Author , Book-Quantity")
    if len(book_data) == 0:
        print(Fore.RED + "There are no book in Database to view")
    else:
        for i in book_data:
            i = i.replace("\n","")
            i = i.split(",")
            print(Fore.GREEN + f"{i[0]} - {i[1]} - {i[2]} - {i[-1]}")

#The search book function has some bugs
# def search_book(param):
#     book_data = read_book() 
#     if len(book_data) == 0:
#        print(Fore.RED + "There is no Book in DataBase to Search")
#     else:
#        for i in book_data:
#             i = i.replace("\n", "")
#             i = i.split()
#             if param.isdigit():
#                 if i[0] == (param + ","):
#                     print()
#                     print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
#                     print()
#                     return i
#             elif i[1].title() == param.title() + ",":
#                     print("\n\n")
#                     print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
#                     return i

def register_book():
    user_id = input("Enter your user id  :")
    book_name = input("Enter book name  :")
    print(Fore.GREEN + Style.BRIGHT + f"---{"Book Registered Sucessfully"}---")
    with open("registered_books.txt","a") as file:
        file.write(f"User Id --->{user_id} ,registerd Book --->{book_name}\n")
    
book_data_1 = [] #initialization
def view_registerd_books():
    try:
        with open("registered_books.txt","r") as file:
            book_data_1 = file.readlines()
            return book_data_1
    except FileNotFoundError:
        print("No Books are Registered till now")
        return book_data_1


def list_reg_books():
    book_data_1 = view_registerd_books()
    if len(book_data_1) == 0:
        print("No Registerd Books")
    else:
        for i in book_data_1:
            i = i.replace("\n","")
            i = i.split(",")
            print(Fore.GREEN + f"{i[0]} {i[-1]}")


while True:
    menu()
    choice = input("Enter your Choice(1 to 5) : ")
    print(Fore.CYAN + "════"*12)
    if choice == "1":
        addbook()
    elif choice == "2":
        view_book()
    # elif choice == "3":
    #     val = input("Enter the book Id  :")
    #     search_book(val)
    elif choice == "3":
        register_book()
    elif choice == "4":
        list_reg_books()
    elif choice == "5":
        break
    else:
        print(Fore.RED + Style.BRIGHT + "                !!Invalid Choice!!")