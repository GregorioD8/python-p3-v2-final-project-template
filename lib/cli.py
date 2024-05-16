# lib/cli.py
from colorama import init, Fore, Style   #text color: print(Fore.GREEN + " " + Style.RESET_ALL)
import pygame
import os
from pyfiglet import figlet_format
from sounds import *

music_playing = True

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

#Methods from helpers.py
from helpers import (

    list_bands,
    select_band,
    create_band, 
    delete_band,
    list_band_members,
    create_member,
    delete_member,
    find_member_by_name,
    exit_program,
    find_band_by_instrument
)
#Main menu
def main_menu():
    clear_screen()
    play_song(menu)

    while True:
        print(Fore.GREEN + figlet_format("Main Menu", font="standard") + Style.RESET_ALL)
        print("0. Exit the program")
        print("1. Manage Bands")
        print("2. Find band by instrument")
        print("3. Find member by name")

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
        else:
            main_menu()

#Menu for managing bands
def band_menu():
    stop_song()
    clear_screen()
    
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
            band = select_band()
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

    #Only play the bands song if it's not already playing
    if band.song and not pygame.mixer.Channel(0).get_busy():
        band.play()

    while True:
        print(Fore.GREEN + figlet_format(f"{band.name}", font="standard") + Style.RESET_ALL)
        list_band_members(band)

        print("\nMember Menu:")
        print("0. Back to band menu")
        print(f"1. To toggle music on/off")
        print(f"2. Add new member to {band.name}")
        print(f"3. Delete member of {band.name}")
        print(f"4. Delete the band {band.name}")
  
        choice = input(Fore.LIGHTYELLOW_EX + "> "+ Style.RESET_ALL)
        play_sound_effect(click)
        
        if choice == "0":
            band_menu()
        elif choice == "1":
            clear_screen()
            toggle_music()
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
            band_menu()
        else:
            member_menu(band)
            
if __name__ == "__main__":
    main_menu()