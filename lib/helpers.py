# lib/helpers.py
from db.models import Band
from db.models import Member


def exit_program():
    print("Goodbye!")
    exit()

def list_bands():
    bands = Band.get_all()
    for band in bands:
        print(band)

def find_band_by_name():
    name = input("Enter the bands name: ")
    band = Band.find_by_name(name)
    print(band) if band else print(f'Band {band} not found in database.')

def find_band_by_id():
    id_ = input("Enter the bands id: ")
    band = Band.find_by_id(id_)
    print(band) if band else print(f'Band {id_} not found')
#########################
def find_band_by_time():
    time = input("Enter the band playing time: ")
    band = Band.find_by_time(time)
    print(band) if band else print(f'Band time slot empty')
##########################
def create_band():
    name = input("Enter band name: ")
    time = input("Enter playing time: ")
    band = Band.find_by_time(time)
    if not band:
        try:
            band = Band.create(name, int(time))
            print(f'Success: {band}')
        except Exception as exc:
            print("error createing Band", exc)
    
    else: 
        print(f'Time slot taken by {band}')
###########################
def update_band():
    id_ = input("Enter the bands id: ")
    if band := Band.find_by_id(id_):
        try:
            name = input("Enter the bands new name: ")
            band.name = name
            time = input("Enter the bands new time: ")
            band.time = int(time)

            band.update()
            print(f'Success: {band}')
        except Exception as exc:
            print("Error updating band: ", exc)
    else:
        print(f'Band {id_} not found')


def delete_band():
    id_ = input("Enter the bands id: ")
    if band := Band.find_by_id(id_):
        band.delete()
        print(f'Band {id_} deleted')
    else:
        print(f'Band {id_} not found')
    
def list_members():
    members = Member.get_all()
    for member in members:
        print(member)

def find_member_by_name():
    name = input("Enter the members name: ")
    member = Member.find_by_name(name)
    print(member) if member else print(f'Member {member} not found')

def find_member_by_id():
    id = input("Enter the members id: ")
    member = Member.find_by_id(id)
    print(member) if member else print(f'Member {member} not found')

def create_member():
    name = input("Enter the members name: ")
    instrument = input("Enter the members instrument: ")
    band = input("Enter the members band id: ")
    try:
        member = Member.create(name, instrument, band)
    except Exception as exc:
        print("Error creating member: ", exc)

def update_member():
    id_ = input("Enter the members name: ")
    if member := Member.find_by_id(id_):
        try: 
            name = input("Enter the members new name: ")
            member.name = name
            instrument = input("Enter the members new instrument: ")
            member.instrument = instrument
            band_id = input("Enter the members new band id: ")
            member.band_id = int(band_id)
            member.update()
            print(f'Success: {member}')
        except Exception as exc:
            print("Error updating memeber: ", exc)
    else:
        print(f'Employee {id_} not found')

def delete_member():
    id_ = input("Enter the members id: ") 
    if member := Member.find_by_id(id_):
        member.delete()
        print(f'Member {id_} deleted')
    else:
        print(f'Member {id_} not found')

def number_of_members():
    id_ = input("Enter the bands id: ")
    band = Band.find_by_id(id_)
    members = len(band.members())
    if band:
        return print(f'The number of artists in {band.name}: {members}')
    else: 
        print(f'cannot find band.')

def list_band_members():
    id_ = input("Enter the bands id: ")
    if band := Band.find_by_id(id_):
        for member in band.members():
            print(member.name)
    else:
        print(f'Band {id_} not found')
