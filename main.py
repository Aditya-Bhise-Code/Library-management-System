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
    print()
    print("2.View Book")
    print()
    print("3.Search Book")
    print()
    print("4.Register Book")
    print()
    print("5.Issue Book")
    print()
    print("6.Exit")
    print()


def read_book():
    with open("book_data.txt","r") as f:
        book_data = f.readlines()
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
        else:
            print(Fore.RED + "INVALID QUANTITY \nEnter a valid number")
    print(Fore.GREEN + f"---{"Book added Sucessfully"}---")

    with open("book_data.txt","a") as file:
        file.write(f" {book_id} , {book_name} , {book_author} , {book_quantity}\n")

def view_book():
    book_data = read_book()
    print("Sr.no , Book_Name , Book_Author , Book_Quantity")
    for i in book_data:
        print(Fore.GREEN + i)
        print()







def search_book():     #Doubt
    print(Fore.GREEN + "---Search Book---")
    book_name = input("Enter book name  :").title()
    book_data = read_book()
    for i in book_data:
        if book_name in i:
            print(Fore.GREEN + "Yes we have that book")
            break
        else:
            print(Fore.LIGHTRED_EX + "Sorry we don't have the book")








while True:
    menu()
    choice = input("Enter your Choice(1 to 6) : ")
    if choice == "1":
        addbook()
    elif choice == "2":
        view_book()
    elif choice == "3":
        print("Search Book")
    elif choice == "4":
        print("Register Book")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        break
    else:
        print(Fore.RED + "                !!Invalid Choice!!")