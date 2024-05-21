import sqlite3

CONN = sqlite3.connect('label.db') #import package and establishes the name of the database
CURSOR = CONN.cursor()
