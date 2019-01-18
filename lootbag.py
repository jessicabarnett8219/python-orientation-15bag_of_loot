import sqlite3
import sys

lootbagdb = '/Users/jessicabarnett/workspace/back-end/python/exercises/bag_of_loot/lootbag.db'

def getChildren():
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    for row in cursor.execute('''
      SELECT * FROM Children
    '''
    ):
      print(row)

def addChild(child):
  print("Add child called", child)
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        '''
        INSERT INTO Children
        VALUES (?, ?)
        ''', (None, child["ChildName"])
      )
    except sqlite3.OperationalError as err:
      print("oops", err)


if __name__ == "__main__":
  addChild({
    "ChildName": "Stephanie"
  })
  getChildren()