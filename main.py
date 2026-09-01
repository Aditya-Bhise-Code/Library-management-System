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
    print("2.View Book")
    print("3.Search Book")
    print("4.Register Book")
    print("5.Issue Book")
    print("6.Exit")


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
    book_name = input("Enter Book name  :").strip()
    for i in book_data:
        if book_name in i:
            print(Fore.GREEN + "This book already exists")
            print(Fore.RED + "Terminating this Function")
            return False
    book_author = input("Enter the author name  :").strip()
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

    










while True:
    menu()
    choice = input("Enter your Choice(1 to 6) : ")
    if choice == "1":
        addbook()
    elif choice == "2":
        print("View book")
    elif choice == "3":
        print("Search Book")
    elif choice == "4":
        print("Register Book")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        break
    else:
        print("!!Invalid Choice!!")
