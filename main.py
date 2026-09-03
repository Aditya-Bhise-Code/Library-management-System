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
    print(Fore.GREEN + f"---{"Book added Sucessfully"}---")

    with open("book_data.txt","a") as file:
        file.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")

def view_book():
    book_data = read_book()
    print("Sr.no , Book_Name , Book_Author , Book_Quantity")
    if len(book_data) == 0:
        print(Fore.RED + "There are no book in Database to view")
    else:
        for i in book_data:
            i = i.replace("\n","")
            i = i.split(",")
            print(Fore.LIGHTYELLOW_EX + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")

# def search_book(param):
#     print(Fore.GREEN + "---Search Book---")
#     book_data = read_book()
#     if len(book_data) == 0:
#             print(Fore.RED + "There are no book in Database to Search")
#     else:
#         for i in book_data:
#             i = i.replace("\n","")
#             i = i.split(",")
#             if param.isdigit():
#                 if i[0] == " " + param + " ":
#                     print("\n\n")
#                     print(Fore.LIGHTYELLOW_EX + f"{i[0]} - {i[1]} - {i[-1]}")
#                     return i
#             else:
#                 print("ok")

def search_book(param):
    book_data = read_book() 
    if len(book_data) == 0:
       print(Fore.RED + "There is no Book in DataBase to Search")
    else:
       for i in book_data:
            i = i.replace("\n", "")
            i = i.split()
            if param.isdigit():
                # print(f"{i[0]} --> {type(i[0])}")
                # print(param, type(param))
                if i[0] == param + ",":
                    print()
                    print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
                    print()
                    return i
            else:
                if i[1].lower() == param.lower() + ",":
                    print("\n\n")
                    print(Fore.CYAN + f"Book Id : {i[0]} Book Name : {i[1]}  Book Author : {i[2]} Book_Quantity : {i[-1]} ")
                    return i





while True:
    menu()
    choice = input("Enter your Choice(1 to 6) : ")
    if choice == "1":
        addbook()
    elif choice == "2":
        view_book()
    elif choice == "3":
        val = input("Enter the book Id  :")
        search_book(val)
    elif choice == "4":
        print("Register Book")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        break
    else:
        print(Fore.RED + "                !!Invalid Choice!!")