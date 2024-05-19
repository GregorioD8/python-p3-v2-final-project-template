from db.__init__ import CONN, CURSOR
from db.models import Band, Member, Song
from sounds import *

def get_song(song_name):
    return f"{song_name}"

def seed_database():
    Member.drop_table()
    Band.drop_table()
    Song.drop_table()
    Band.create_table()
    Member.create_table()
    Song.create_table()

    # Create seed data
    ccr = Band.create("Creedence Clearwater Revival")
    led = Band.create("Led Zeppelin")
    jimi = Band.create("Jimi Hendrix")
    aerosmith = Band.create("Aerosmith")
    blink = Band.create("Blink 182")

    Member.create("John Fogerty", "Vocals/Guitar", ccr.id)
    Member.create("Tom Fogerty", "Guitar", ccr.id)
    Member.create("Doug Clifford", "Drums", ccr.id)
    Member.create("Stu Cook", "Bass", ccr.id)

    Member.create("Robert Plant", "Vocals", led.id)
    Member.create("Jimmy Page", "Guitar", led.id)
    Member.create("John Bonham", "Drums", led.id)
    Member.create("John Paul Jones", "Bass", led.id)

    Member.create("Jimi Hendrix", "Vocals/Guitar", jimi.id)
    Member.create("Noel Redding", "Bass", jimi.id)
    Member.create("Mitch Mitchell", "Drums", jimi.id)
   
    Member.create("Steven Tyler", "Vocals", aerosmith.id)
    Member.create("Joe Perry", "Guitar", aerosmith.id)
    Member.create("Joey Kramer", "Drums", aerosmith.id)
    Member.create("Brad Whitford", "Guitar", aerosmith.id)
    Member.create("Tom Hamilton", "Bass", aerosmith.id)
    Member.create("Rick Dufay", "Guitar", aerosmith.id)

    Member.create("Mark Bass", "Vocals/Bass", blink.id)
    Member.create("Tom Delong", "Vocals/Guitar", blink.id)
    Member.create("Travis Barker", "Drums", blink.id)
    
    Song.create("fortunate_son", "../lib/music/ccr.mp3", ccr.id)
    Song.create("immigrant_song", "../lib/music/led_zeppelin.mp3", led.id)
    Song.create("all_along_the_watchtower", "../lib/music/jimi.mp3", jimi.id)
    Song.create("dream_on", "../lib/music/aerosmith.mp3", aerosmith.id)
    Song.create("blink", "../lib/music/blink.mp3", blink.id)



seed_database()
print("Seeded database")