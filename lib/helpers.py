from db.models import Band, Member, Song 
from tabulate import tabulate #for nice tables eg. print(tabulate(xyz_table, headers=["x_column","y_column", "z_column"], tablefmt="fancy_grid"))
from colorama import init, Fore, Style
from pyfiglet import figlet_format
import os #https://docs.python.org/3/library/os.html
import shutil #https://docs.python.org/3/library/shutil.html#module-shutil


def exit_program():
    print("Exiting program")
    exit()

#Creates a new band.  
def create_band():
    name = input("Enter band name: ")
    Band.create(name) and print(f"{name} created") if not Band.find_by_name(name) else print(f"Band name {name} taken")
    print(Band.get_all())

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

#Upload song for the band
def upload_song(band, song_name, song_path):
    #makes a copy of the song and places it in the music folder using pythons shutil module
    music_folder = '../lib/music'
    os.makedirs(music_folder, exist_ok=True)
    song_filename = f"{song_name}.mp3"
    destination_path = os.path.join(music_folder, song_filename)
    shutil.copy(song_path, destination_path) 
   
    Song.create(song_name, destination_path, band.id) 
    

#Gets all of the bands songs
def get_songs(band):
    songs = Song.get_all()
    bands_songs = [song for song in songs if song._band_id == band.id]
    table = [[i, song.name] for i, song in enumerate(bands_songs, start = 1)]
    print(tabulate(table, headers=['#', 'Song'], tablefmt='fancy_grid'))
    # print(bands_songs)
    return bands_songs

#Plays the selected song
def select_song(band, song_number):
    songs = get_songs(band)
    songs[int(song_number) - 1].play()

def list_song_library():
    #Getting all songs and the associated band
    songs = [song for song in Song.get_all() if song.band_id]
    table = [[i, Band.find_by_id(song.band_id).name, song.name] for i, song in enumerate(songs, start=1)]
    print(tabulate(table, headers=['Band', 'Song'], tablefmt='fancy_grid'))

    