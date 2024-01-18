from db.__init__ import CONN, CURSOR
from db.models import Member
from db.models import Band

def seed_database():
    Member.drop_table()
    Band.drop_table()
    Band.create_table()
    Member.create_table()


    # Create seed dat
    ccr = Band.create("Creedence Clearwater Revival", 8)
    led = Band.create("Led Zeppelin", 9)
    Member.create("John Fogerty", "Vocals and Guitar", ccr.id)
    Member.create("Tom Fogerty", "Guitar", ccr.id)
    Member.create("Doug Clifford", "Drums", ccr.id)
    Member.create("Stu Cook", "Bass", ccr.id)
    Member.create("Robert Plant", "Vocals", led.id)
    Member.create("Jimmy Page", "Guitar", led.id)
    Member.create("John Bonham", "Drums", led.id)
    Member.create("John Paul Jones", "Bass", led.id)


seed_database()
print("Seeded database")