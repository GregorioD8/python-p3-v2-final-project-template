import sqlite3

CONN = sqlite3.connect('concert.db')
CURSOR = CONN.cursor()
