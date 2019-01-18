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
    print(child_id)
    return child_id


def addGift(gift):
  print("Add gift called", gift)
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        '''
        INSERT INTO Gifts
        VALUES (?, ?, ?, ?)
        ''', (None, gift["GiftName"], gift["Delivered"], gift["ChildId"])
      )
    except sqlite3.OperationalError as err:
      print("oops", err)




if __name__ == "__main__":
  # addGift({
  #   "GiftName": "Dinosaur",
  #   "Delivered": 0,
  #   "ChildId": 1
  # })
  # getChildren()
  # getAllGifts()
  getChildId("Wally")