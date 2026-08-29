import colorama
from colorama import Fore, Back, Style, init

def menu():
    init(autoreset=True)
    print(Fore.CYAN + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print("1.  ")
    print("2.  ")
    print("3.  ")
    print("4.  ")
    print("5.  ")
menu()
choice = input("Enter your choice here : ")
if choice == "1":
    print("1")
elif choice == "2":
    print("2")
elif choice == "3":
    print("3")
elif choice == "4":
    print("4")
elif choice == "5":
    print("5")
else:
    print("6")