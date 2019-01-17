import sqlite3
import sys

lootbag_db = '/Users/jessicabarnett/workspace/back-end/python/exercises/bag_of_loot/lootbag.db'

# def getSupers():
#   with sqlite3.connect(super_db) as conn:
#     cursor = conn.cursor()
#     # a way for us to have a python-readable version of our db

#     # Run SQL inside the parens
#   for row in cursor.execute('SELECT * FROM Superhero'):
#     print(row)

def getChildren():
  with sqlite3.connect(lootbag_db) as conn:
    cursor = conn.cursor()

    for row in cursor.execute('''
      SELECT * FROM Children
    '''
    ):
      print(row)

if __name__ == "__main__":

  getChildren()