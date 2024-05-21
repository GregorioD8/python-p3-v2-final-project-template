# lib/cli.py
from colorama import init, Fore, Style   #text color: print(Fore.GREEN + " " + Style.RESET_ALL)
import pygame
import os
from pyfiglet import figlet_format
from sounds import menu, click
from helpers import *
from db.models import Band, Member, Song
music_playing = True
just_deleted = False

#Initializes colorama for text
init(autoreset = True)
pygame.mixer.init()

#Initialize SDL video driver to avoid opening a window
os.environ["SDL_VIDEODRIVER"] = "dummy"

#clears screen but the not scrollback in terminal 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Toggles music play/pause
def toggle_music():
    print("press m to toggle music on/off")
    global music_playing
    if music_playing:
        pygame.mixer.Channel(0).pause()
        music_playing = False
        print(Fore.LIGHTBLUE_EX + "Music puased" + Style.RESET_ALL)
    else:
        pygame.mixer.Channel(0).unpause()
        music_playing = True
        print(Fore.LIGHTBLUE_EX + "Music playing" + Style.RESET_ALL)

#Plays background song
def play_song(sound):
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound))
#Stops song
def stop_song():
    pygame.mixer.Channel(0).stop()
#Plays sound effect
def play_sound_effect(sound):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound))

#Main menu
def main_menu():
    clear_screen()
    play_song(menu)

    while True:
        print(Fore.LIGHTMAGENTA_EX + figlet_format("Flatiron \nRecords", font="block") + Style.RESET_ALL)
        print(Fore.GREEN + figlet_format("Main Menu", font="standard") + Style.RESET_ALL)
        print("0. Exit the program")
        print("1. Manage Bands")
        print("2. Find band by instrument")
        print("3. Find member by name")
        print("4. Flatiron Records song library")

        choice = input(Fore.LIGHTYELLOW_EX + "> "+ Style.RESET_ALL)
        play_sound_effect(click)

        if choice == "0":
            exit_program()
        elif choice == "1":
            band_menu()
        elif choice == "2":
            clear_screen()
            find_band_by_instrument()
        elif choice == "3":
            clear_screen()
            find_member_by_name()
        elif choice == "4":
            list_song_library()
        else:
            main_menu()

#Menu for managing bands
def band_menu():
    stop_song()
    clear_screen()
    global just_deleted
    if just_deleted:
            list_bands()
            just_deleted = False

    while True:
        print(Fore.GREEN + figlet_format("Band Menu", font="standard") + Style.RESET_ALL)
        print("0. Back to main menu")
        print("1. Select band to manage")
        print("2. Create band\n")

        choice = input(Fore.LIGHTYELLOW_EX + "> "+ Style.RESET_ALL)
        play_sound_effect(click)

        if choice == "0":
            main_menu()
        elif choice == "1":
            clear_screen()
            band = select_band()
            if band:
                member_menu(band)
        elif choice == "2":
            create_band()
            list_bands()
        else:
            print("Invalid choice")

#Menu for managing band members
def member_menu(band):
    clear_screen()
    play_sound_effect(click)
    print("press m to toggle music on/off")
    songs = Song.find_by_id(band.id)
    if songs:
        
        #the first listed song from the band
        song = songs[0]

        #Only play this song if it's not already playing
        if song and not pygame.mixer.Channel(0).get_busy():
            song.play()
        print(f"playing {song.name} by {band.name}")
    else: 
        print(f"No songs found for {band.name}.")

    while True:
        print(Fore.GREEN + figlet_format(f"{band.name}", font="standard") + Style.RESET_ALL)
        list_band_members(band)

        print("\nMember Menu:")
        print("0. Back to band menu")
        print(f"1. Song menu for {band.name}")
        print(f"2. Add new member to {band.name}")
        print(f"3. Delete member of {band.name}")
        print(f"4. Delete the band {band.name}")

        choice = input(Fore.LIGHTYELLOW_EX + "> "+ Style.RESET_ALL)
        play_sound_effect(click)
        
        if choice == "0":
            band_menu()
        elif choice == "1":
            clear_screen()
            song_menu(band)
        elif choice == "2":
            clear_screen()
            create_member(band)
            clear_screen()
            member_menu(band)
        elif choice == "3":
            clear_screen()
            list_band_members(band)
            member = input(Fore.LIGHTYELLOW_EX + f"Delete which member of {band.name}? \nEnter the members number: >"+ Style.RESET_ALL)
            delete_member(band.members()[int(member) - 1])
            member_menu(band)
        elif choice == "4":
            toggle_music()
            delete_band(band)
            global just_deleted
            just_deleted = True
            band_menu()
        elif choice == "m":
            clear_screen()
            toggle_music()
        else:
            member_menu()
            
#Menu for managing bands
def song_menu(band):
    clear_screen()
    print("press m to toggle music on/off")
    while True:
        print(Fore.GREEN + figlet_format("Song Menu", font="standard") + Style.RESET_ALL)
        print("0. Back to main menu")
        print(f"1. See all songs by {band.name}")
        print(f"2. Upload new song for {band.name}")
        print("3. Play different song\n")

        choice = input(Fore.LIGHTYELLOW_EX + "> "+ Style.RESET_ALL)
        play_sound_effect(click)

        if choice == "0":
            main_menu()
        elif choice == "1":
            clear_screen()
            get_songs(band)
        elif choice == "2":
            song_name = input("Enter the name of the song: ").strip()
            song_path = input("Copy and paste the full path of the song file here: ").strip()
            upload_song(band, song_name, song_path)
            clear_screen()    
            print(f"Uploaded song: {song_name} by {band.name}!")
        elif choice == "3":
            get_songs(band)
            song_number = input("Select the song number: ").strip()
            select_song(band, song_number)    
            clear_screen()  
        elif choice == "m":
            clear_screen()
            toggle_music()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()