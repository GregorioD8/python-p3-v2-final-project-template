import sqlite3

CONN = sqlite3.connect('tour.db') #import package and establishes the name of the database
CURSOR = CONN.cursor()
