import pdb
from db.models import Band, Member


def exit_to_main():
    print("Exiting to main menu")
    exit()


def find_band_by_name():
    name = input("Enter the band's name: ")
    band = Band.find_by_name(name)
    return print(band) if band else print(f'Band "{name}" not found in the database.')
  

def find_band_by_id():
    id_ = input("Enter the band's ID: ")
    band = Band.find_by_id(id_)
    return print(band) if band else print(f'Band with ID "{id_}" not found')


def create_band():
    name = input("Enter band name: ")
    Band.create(name) and print(f"{name} created") if not Band.find_by_name(name) else print(f"Band name {name} taken")

    

def delete_band():
    print("Which band would you like to delete?")
    list_bands()

    selection = input("Which band would you like to delete? \nEnter the members number: ")
    
    index = int(selection)
    print(index)
    bands = Band.get_all()
    #check if selection falls in the range of existing indexes
    if 1 <= index <= len(bands):
       
        selected_band = bands[index - 1]
        
        print(f"{selected_band.name} Deleted.")
        selected_band.delete()
    else:
        print("invalid selection: please try again.")

#########################################################
def list_bands():
    print("\n################################")
    print("All Bands")
    print("################################")
    [print(f"{i}. {band.name}") for i, band in enumerate(Band.get_all(), start = 1)]
    print("################################\n")
    
def list_band_members():
    print(f"\nWhat band would you like to see the members of?")
    list_bands()
    selection = input("Select a band number: ")
    band = Band.get_all()[int(selection) - 1]

    print("\n******************************************")
    print(f"Members of {band.name}")
    print("******************************************")
    [print(f"{i}. {member.name}") for i, member in enumerate(band.members(), start = 1)]
    print("*****************************************\n")

    
def create_member():
    name = input("Enter the member's name: ")
    instrument = input("Enter the member's instrument: ")
    
    list_bands()

    band_selection = input(f"Add {name} to which band? \nEnter the band number: ")
    index = int(band_selection)

    bands = Band.get_all()
    band = bands[index - 1]

   
    try:
        member = Member.create(name, instrument, band.id)
        print("\n****************************************************")
        print(f'Success: {member.name} added to the band {band.name}')
        print("******************************************************")
    except Exception as exc:
        print("Error creating member:", exc)

def delete_member():

    list_bands()

    band_selection = input("Delete member of what band \nEnter the band number: ")
    index = int(band_selection)

    bands = Band.get_all()
    band = bands[index - 1].members()

    [print(f"{i}. {member.name}") for i, member in enumerate(band, start= 1)]
    
    # i = 1
    print("\n********************************")
    print(f"{member.name}" for member in band)
    print("********************************")
    pdb.set_trace()
    # for member in band:
        
    #     print(f"{i}. {member.name}" )
    #     i +=1
    # print("********************************\n")
          
    member_index = int(input("Which member would you like to delete? \nEnter the members number: "))
    soloist = band[member_index-1]
    print("\n--------------------------------------------------------------------------")
    print(f"ARE YOU SURE YOU WANT TO DELETE {soloist.name} FROM {bands[index - 1].name}? ")
    print("----------------------------------------------------------------------------")
    permission = input("\nEnter y to delete and n to cancel: ")
    granted = "y"
    if permission.casefold() == granted.casefold():
        soloist.delete()
        print("\n---------------------------------------")
        print(f"{soloist.name} DELETED FROM {bands[index - 1].name}")
        print("-----------------------------------------")
    else:
        print("\n------------------")
        print(f"Deletion cancelled")
        print("--------------------")

def find_member_by_name():
    name = input("enter the first or last name of the member. ")
    
    
    #find in Member.all
    all_members = Member.get_all()

    #member dict includes names that match the provided name
    md = [member.name for member in all_members if name.lower() in member.name.lower()]
    print("\n********************************")
    print(f"Names that include: {name}")
    print("********************************")
    [print(f"{i}. {member}")for i, member in enumerate(md, start=1)]   
    print("********************************\n")

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

    pdb.set_trace()