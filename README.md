# Phase 3 CLI+ORM Project 

 ### `What I learned`

- How to create the basic directory structure of a CLI.
- How to build a CLI.
- How to set set up ORM for SQL using Python 
    1. Choose an ORM library: `sqlite3`
    2. Install the ORM library: `pip install sqlite3`
    3. Configure the database connection: `__init__.py --> CONN = sqlite3.connect('label.db')`
    4. Define models/tables/CRUD operations: `Created python classes`
    
# By using an ORM you can interact with your database using Python objects and methods, making your code more readable and easier to maintain for object oriented programming.`  

This is the directory structure:

```console

├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── music: folder to store mp3 song files for playback in the program
    ├── db
    │   ├── __init__.py
    ├── ├── alembic.ini
    │   └── models.py  
    ├── cli.py
    ├── helpers.py
    ├── seed.py
    └── tour.db
```

### `setup`

- Run `cd lib` to cd into the lib folder `/lib` 
- Run `python seed.py` to seed the data
- Run `python cli.py` to start the program  `lib/cli.py` 

### `Running the CLI`

This is the program structure:
```console
└── Main Menu
    ├── Manage Bands
    ├── Find band by instrument
    ├── Find member by name
    └── List all songs    
        
        └── Band Menu
        ├── Back to main menu
        ├── Select band to manage
        └── Create band            
            └── Member Menu (for the selected band)
                ├── Back to band menu
                ├── Song Menu
                ├── Add new member to band
                ├── Delete member of band
                └── Delete band

                    └── Song Menu
                        ├── Back to band menu
                        ├── View all songs by band
                        ├── Upload new song for band
                        └── Play different song
```      

## Prompt, Helper, and Class relation 

These are the helpers

```
    exit_program,
    list_bands,
    create_band, 
    find_band_by_name,
    list_band_members,
    list_all_artists,
    create_performance,
    list_song_library,
    get_songs, 
    select_song,
    upload_song
```

Some of the following methods that print tables. Those tables are presented in tabulated format using pythons `tabulate` library. 

`exit_program` Exits the program. It prints a message that the user is exiting the program and then exits using the `exit()` function.

`list_bands`
This prints out all of the bands that exist in the database. 

`create_band`
Creates an band instance of the band class. The user provides input for the name of the new band.  

`delete_band` 
Deletes a specified band and all of its members.

`find_band_by_name`
Prompts the user to enter a bands name and searches for the band in the database. If the band is found, it prints the band's details; otherwise it notifies the user that the name is taken. It also lists all bands after crating a new one.

`list_band_members`
Lists all members of a band. It retrievs the bands members and displays their details. 

`create_member`
Creates a new member by the provided input of name and instrument.

`delete_member`
Deletes a specified member from the database.

`find_member_by_name`
Prompts the user to enter part of a members name.

`select_band`
Lists all bands and prompts the user to select a band by number. It returns the selected band instance.

`list_instruments`
Lists all unique instruments played by band members in the database. The user selects one of the instruments and the method prints a table displaying all of the bands that have that instrument played in their band.

`upload_song`
Prompts the user to enter a song name and the path to the song file. It copies the song file to the designated music folder and creates a new song record in the database.

`get_songs` 
Retrieves all songs of a specified band.

`select_song`
Prompts the user to select a song from a specified band and plays the selected bands song.

`list_song_library`
Lists all songs in the database along with their associated band.

