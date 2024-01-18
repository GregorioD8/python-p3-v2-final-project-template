# lib/cli.py

from helpers import (

#see instructions 
    exit_program,
    list_bands,
    create_band, 
    find_band_by_name

)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_bands()
        elif choice == "2":
            create_band()
        elif choice == "3":
            find_band_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all bands playing at concert")
    print("2. Create band")
    print("3. Find band by name")
    


if __name__ == "__main__":
    main()
