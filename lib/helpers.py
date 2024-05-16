import pdb
from db.models import Band, Member
from tabulate import tabulate 
from colorama import init, Fore, Style
from pyfiglet import figlet_format

def exit_program():
    print("Exiting program")
    exit()

def find_band_by_name():
    name = input("Enter the band's name: ")
    band = Band.find_by_name(name)
    return print(band) if band else print(f'Band "{name}" not found in the database.')
  
def create_band():
    name = input("Enter band name: ")
    Band.create(name) and print(f"{name} created") if not Band.find_by_name(name) else print(f"Band name {name} taken")

def delete_band(band):
    [member.delete() for member in band.members()]
    band.delete() 
    print(Fore.LIGHTRED_EX +f"The band {band.name} and all of its members have been DELETED" + Style.RESET_ALL)

def list_band_members(band):
    table = [[i, member.name, member.instrument] for  i, member in enumerate(band.members(), start = 1)]
    print(tabulate(table, headers=['#', 'Member Name', 'Member Instrument'], tablefmt='fancy_grid'))
    
def create_member(band):
    print(Fore.GREEN + figlet_format(f"{band.name}", font="standard") + Style.RESET_ALL)
    print(Fore.GREEN + f"Adding a new member to {band.name}" + Style.RESET_ALL)
    name = input("Enter the new member's name: ")
    instrument = input("Enter the member's instrument: ")
    Member.create(name, instrument, band.id)
    print(Fore.LIGHTGREEN_EX +f'{name} ADDED to the band {band.name}' + Style.RESET_ALL)

def delete_member(member):
    # pdb.set_trace()
    member.delete()
    print(Fore.LIGHTRED_EX +f"{member.name} DELETED from {Band.find_by_id(member.band_id).name}"+ Style.RESET_ALL)

def find_member_by_name():
    name = input("enter the first or last name of the member. ")
    #find in Member.all
    all_members = Member.get_all()

    #member dict includes names that match the provided name
    ml = [member.name for member in all_members if name.lower() in member.name.lower()]
    # print("\n********************************")
    # print(f"Names that include: {name}")
    # print("********************************")
    # [print(f"{i}. {member}")for i, member in enumerate(md, start=1)]   
    # print("********************************\n")
    print(Fore.GREEN + figlet_format(f"{name.capitalize()}", font="standard") + Style.RESET_ALL)
    table = [[i, member] for i, member in enumerate(ml, start = 1)]
    print(tabulate(table, headers=['#', 'names'], tablefmt='fancy_grid'))

def find_member_by_instrument():
    gear = [member.instrument for member in Member.get_all()]
    gear_list = []
    [gear_list.append(instrument) for instrument in gear if instrument not in gear_list]
  
 
    [print(f"{i}. {instrument}") for i, instrument in enumerate(gear_list, start = 1)]
    
    selection = input("Enter the instruments number: ")

    inst = gear_list[int(selection) - 1]
    
    print("\n*****************************")
    print(f"Instrument: {inst}")
    print("*****************************")
    [print(f"{member.name}") for member in Member.find_by_instrument(inst)]
    print("*****************************\n")

def list_bands():
    table = [[i, band.name] for  i, band in enumerate(Band.get_all(), start = 1)]
    print(tabulate(table, headers=['#', 'Band Name'], tablefmt='fancy_grid'))

def select_band():
    list_bands()
    selection = input(Fore.LIGHTYELLOW_EX + "Select a band number: " + Style.RESET_ALL)
    band = Band.get_all()[int(selection) - 1]
    return band

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

    table = [[band.name, f"{member.name} plays {member.instrument}"]
             for band in Band.get_all()
             for member in band.members()
             if member.instrument == instrument]
    
    print(Fore.GREEN + figlet_format(f"{instrument}", font="standard") + Style.RESET_ALL)
    print(tabulate(table, headers=['Band', 'Member'], tablefmt='fancy_grid'))
    
  
    #add selection
    # list[int(selection)-1]