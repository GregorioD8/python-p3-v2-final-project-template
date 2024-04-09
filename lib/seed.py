from db.__init__ import CONN, CURSOR
from db.models import Member
from db.models import Band
from db.models import City

def seed_database():
    Member.drop_table()
    Band.drop_table()
    City.drop_table()
    Band.create_table()
    Member.create_table()
    City.create_table()

    # Create seed data
    ccr = Band.create("Creedence Clearwater Revival", 8)
    led = Band.create("Led Zeppelin", 9)
    jimi = Band.create("Jimi Hendrix", 10)
    aerosmith = Band.create("Aerosmith", 7)

    Member.create("John Fogerty", "Vocals and Guitar", ccr.id)
    Member.create("Tom Fogerty", "Guitar", ccr.id)
    Member.create("Doug Clifford", "Drums", ccr.id)
    Member.create("Stu Cook", "Bass", ccr.id)

    Member.create("Robert Plant", "Vocals", led.id)
    Member.create("Jimmy Page", "Guitar", led.id)
    Member.create("John Bonham", "Drums", led.id)
    Member.create("John Paul Jones", "Bass", led.id)

    Member.create("Jimi Hendrix", "Guitar/Vocals", jimi.id)
    Member.create("Noel Redding", "Bass", jimi.id)
    Member.create("Mitch Mitchell", "Drums", jimi.id)
   
    Member.create("Steven Tyler", "Vocals", aerosmith.id)
    Member.create("Joe Perry", "Lead Guitar", aerosmith.id)
    Member.create("Joey Kramer", "Drums", aerosmith.id)
    Member.create("Brad Whitford", "Guitar", aerosmith.id)
    Member.create("Tom Hamilton", "Bass", aerosmith.id)
    Member.create("Rick Dufay", "Guitar", aerosmith.id)

    City.create("SLC", jimi.id)
    City.create("NYC", jimi.id)
    City.create("PHX", jimi.id)

    City.create("LA", ccr.id)
    City.create("PA", ccr.id)
    City.create("SLC", ccr.id)
    City.create("NYC", ccr.id)
    City.create("PHX", ccr.id)

    City.create("CO", aerosmith.id)
    City.create("LA", aerosmith.id)
    City.create("PA", aerosmith.id)
    City.create("SLC", aerosmith.id)
    City.create("NYC", aerosmith.id)
    City.create("PHX", aerosmith.id)

    City.create("PHX", led.id)    
    City.create("SLC", led.id)
    City.create("LA", led.id)

seed_database()
print("Seeded database")