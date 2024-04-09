# Phase 3 CLI+ORM Project 

 ### `What I learned`

- How to create the basic directory structure of a CLI.
- How to build a CLI.

---

This is the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── db
    │   ├── __init__.py
    │   ├── alembic.ini
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

These are the prompts 

```console
0. Exit the program
1. List all bands playing at concert
2. Create band
3. Find band by name
4. Find number of band members for band
5. List all band members in a band
6. List all band members playing at the concert
7. List all cities band is performing
8. create performance
```

## Prompt, Helper, and Class relation 

These are the helpers

```
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
```

The prompt `1. List all bands playing at concert`
uses the helper function `exit_program`. This prints out all of the bands that exist in the "all" dict in the Band class created from the seeded data. 

The prompt `2. Create band`
uses the helper function `create_band`. This helper takes two inputs: the name and the time. I use the time to check if any other bands are playing at that time. If there are no other bands playing at this time then it successfully creates the band. If not an error is printed to the cli stating that the time slot is taken by the specified band.  

The prompt `3. Find band by name`
uses the helper function `find_band_by_name`. this takes the input of the band name. The name is then sent to the Band class and checks if it is contained in the "all" dict. if it is not then the cli prints out that the band was not found. 

The prompt `4. Find number of band members for band`
uses the helper function `number_of_members`. This takes in the input of the bands id. The id is used to find the band in Band class. if the band exists in the Band class i use `len(band.members())` to get the number of members. if it doesnt exist. i print out `cannot find band.`

The prompt `5. List all band members in a band`
uses the helper function `list_band_member`. This takes in the input of the bands id. The id is used to find the band in Band class. if the band exists in the Band class i use a for loop to print out each members name.

The prompt `6. List all band members playing at the concert`
uses the helper function `list_all_artists`. This prints all members that exist in the Member class using a for loop with `Member.get_all()`.

The prompt `7. List all cities band is performing`
uses the helper function `list_performances`. This takes the input of the band id from the user. it prints out each city the band is performing in. it uses the Band class to find the band and a for loop to print out each city the band plays in. 

The prompt `8. create performance`
uses the helper function `create_performance`. This takes in the input of city and id. If the id is not taken already the band is created using the create function from the Band class. 
