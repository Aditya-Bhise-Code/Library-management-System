import colorama
from colorama import Fore, Back, Style, init

def menu():
    init(autoreset=True)
    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print("1.Add Book")
    print("2.View Book")
    print("3.Search Book")
    print("4.Register Book")
    print("5.Issue Book")
    print("6.Exit")
menu()

def addbook():
    print(Fore.GREEN + "---Add Book---")
    while True:
        book_id = input("Enter Book Id  :").strip()
        if book_id.isdigit():
            break
        else:
            print(Fore.RED + "Invalid Book Id \n Enter only numbers")




while True:
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
