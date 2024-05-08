# lib/cli.py

from helpers import (

    list_bands,
    create_band, 
    find_band_by_name,
    delete_band,
    list_band_members,
    create_member,
    delete_member,
    find_member_by_name,
    find_member_by_instrument
)


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Band Menu")
        print("2. Member Menu")
        print("0. Exit the program")

        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            band_menu()
        elif choice == "2":
            member_menu()
        else:
            print("Invalid choice")

def band_menu():
    while True:

        print("\nBand Menu:")
        print("1. List all bands")
        print("2. Create band")
        print("3. Delete band")
        print("4. Find band by name")
        print("5. List all band members")
        print("0. Back to main menu")

        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            list_bands()
        elif choice == "2":
            create_band()
        elif choice == "3":
            delete_band()
        elif choice == "4":
            find_band_by_name()
        elif choice == "5":
            list_band_members()
        else:
            print("Invalid choice")

def member_menu():
    #add find by name
    while True:
        print("\nMember Menu:")
        print("1. List all members")
        print("2. Create member")
        print("3. Delete member")
        print("4. Find member by name")
        print("5. Find member by instrument")
        print("0. Back to main menu")

        choice = input("> ")

        if choice == "0":
            break
        elif choice == "1":
            list_band_members()
        elif choice == "2":
            create_member()
        elif choice == "3":
            delete_member()
        elif choice == "4":
            ########### working on this method
            find_member_by_name(),
        elif choice == "5":
            find_member_by_instrument(),
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main_menu()


#member by name 
#case insensitive
#if another member has the same name show all 
#first or last name #python docs .includes?

#comfort level
#problem solving process


#find by name 

#add to cli
#add to helpers

#how to "change" in sql

