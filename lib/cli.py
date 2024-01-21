# lib/cli.py

from helpers import (

#see instructions 
    exit_program,
    list_bands,
    create_band, 
    find_band_by_name,
    number_of_members,
    list_band_members,
    list_all_artists,
    list_performances,
    create_performance,


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
        elif choice == "4":
            number_of_members()
        elif choice == "5":
            list_band_members()
        elif choice == "6":
            list_all_artists()
        elif choice == "7":
            list_performances()
        elif choice == "8":
            create_performance()  
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all bands playing at concert")
    print("2. Create band")
    print("3. Find band by name")
    print("4. Find number of band members for band")
    print("5. List all band members in a band")
    print("6. List all band members playing at the concert")
    print("7. List all cities band is performing")
    print("8. create performance")
    
if __name__ == "__main__":
    main()
