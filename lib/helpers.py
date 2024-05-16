from db.models import Band, Member
from tabulate import tabulate #for nice tables
from colorama import init, Fore, Style
from pyfiglet import figlet_format

def exit_program():
    print("Exiting program")
    exit()

def find_band_by_name():
    name = input("Enter the band's name: ")
    band = Band.find_by_name(name)
    return print(band) if band else print(f'Band "{name}" not found in the database.')

#Creates a new band. Just by name. Song attribute None by default. Can be added with setter.  
def create_band():
    name = input("Enter band name: ")
    Band.create(name) and print(f"{name} created") if not Band.find_by_name(name) else print(f"Band name {name} taken")

#Deletes band and all of its members
def delete_band(band):
    [member.delete() for member in band.members()] #Deleting each member of the band
    band.delete() #Deleting the band itself
    print(Fore.LIGHTRED_EX +f"The band {band.name} and all of its members have been DELETED" + Style.RESET_ALL)

def list_band_members(band):
    #Using list comprehension to create a list of band members with their details
    table = [[i, member.name, member.instrument] for  i, member in enumerate(band.members(), start = 1)]
    #Displaying the members in a tabulated format
    print(tabulate(table, headers=['#', 'Member Name', 'Member Instrument'], tablefmt='fancy_grid'))
    
def create_member(band):
    print(Fore.GREEN + figlet_format(f"{band.name}", font="standard") + Style.RESET_ALL)
    print(Fore.GREEN + f"Adding a new member to {band.name}" + Style.RESET_ALL)
    name = input("Enter the new member's name: ")
    instrument = input("Enter the member's instrument: ")
    Member.create(name, instrument, band.id)
    print(Fore.LIGHTGREEN_EX +f'{name} ADDED to the band {band.name}' + Style.RESET_ALL)

def delete_member(member):
    member.delete()
    print(Fore.LIGHTRED_EX +f"{member.name} DELETED from {Band.find_by_id(member.band_id).name}"+ Style.RESET_ALL)

#Function to find a member by any part of their name
def find_member_by_name():
    name = input("enter the first or last name of the member. ")
    all_members = Member.get_all()
    #Using list comprehension to find members whose names contain the input string
    ml = [member.name for member in all_members if name.lower() in member.name.lower()]
    print(Fore.GREEN + figlet_format(f"{name.capitalize()}", font="standard") + Style.RESET_ALL)
    table = [[i, member] for i, member in enumerate(ml, start = 1)]
    print(tabulate(table, headers=['#', 'names'], tablefmt='fancy_grid'))

def list_bands():
    table = [[i, band.name] for  i, band in enumerate(Band.get_all(), start = 1)]
    print(tabulate(table, headers=['#', 'Band Name'], tablefmt='fancy_grid'))

#Lists bands and returns the selected band from user input
def select_band():
    list_bands()
    selection = input(Fore.LIGHTYELLOW_EX + "Select a band number: " + Style.RESET_ALL)
    band = Band.get_all()[int(selection) - 1]
    return band

#Lists all instruments that exist
#Using set() so it doesn't duplicate instruments 
def list_instruments():
    instruments = sorted(set(member.instrument for member in Member.get_all()))
    table = [[i, instrument] for i, instrument in enumerate(instruments, start = 1)]
    print(tabulate(table, headers=['#', 'Instrument'], tablefmt='fancy_grid'))
    return instruments
   
def find_band_by_instrument():
    set = list_instruments() 
    selection = input(Fore.LIGHTYELLOW_EX + "Select an instrument number: " + Style.RESET_ALL)
    print(selection)
    
    instrument = set[int(selection) - 1]
    #Using list comprehension to create a list of bands and members who play the selected instrument
    table = [[band.name, f"{member.name} plays {member.instrument}"]
             for band in Band.get_all()
             for member in band.members()
             if member.instrument == instrument]
    
    print(Fore.GREEN + figlet_format(f"{instrument}", font="standard") + Style.RESET_ALL)
    print(tabulate(table, headers=['Band', 'Member'], tablefmt='fancy_grid'))
    
