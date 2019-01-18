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

def getAllGifts():
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    for row in cursor.execute('''
      SELECT * FROM Gifts
    '''
    ):
      print(row)


def addChild(child):
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

def getChildId(name):
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        f'''
        SELECT Children.ChildId
        FROM Children
        WHERE Children.ChildName = '{name}';
        '''
      )
    except sqlite3.OperationalError as err:
      print("oops", err)

    child_id = cursor.fetchone()
    print(child_id[0])
    return child_id[0]


def addGift(gift_name, child_name):
  child_id = getChildId(child_name)
  print(child_id)

  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        '''
        INSERT INTO Gifts
        VALUES (?, ?, ?, ?)
        ''', (None, gift_name, 0, child_id)
      )
    except sqlite3.OperationalError as err:
      print("oops", err)


if __name__ == "__main__":
  # getChildren()
  getAllGifts()