import sqlite3
import sys

lootbagdb = '/Users/jessicabarnett/workspace/back-end/python/exercises/bag_of_loot/lootbag.db'

# Get all children in the database who are getting a gift
def getChildren():
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    for row in cursor.execute('''
      SELECT DISTINCT Children.ChildName
      FROM Children
      JOIN Gifts
      WHERE Children.ChildId = Gifts.ChildId;
    '''
    ):
      print(row)


# Lists all the gifts a child is getting
def getChildGifts(child_name):
  child_id = _getChildId(child_name)
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

  for row in cursor.execute(f'''
    SELECT Gifts.GiftName
    FROM Gifts
    WHERE Gifts.ChildId = {child_id};
    '''
    ):
      print(row)

def _addChild(child_name):
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        '''
        INSERT INTO Children
        VALUES (?, ?)
        ''', (None, child_name)
      )
      return cursor.lastrowid

    except sqlite3.OperationalError as err:
      print("oops", err)


def _getChildId(child_name):
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    cursor.execute(
      f'''
      SELECT Children.ChildId
      FROM Children
      WHERE Children.ChildName = '{child_name}';
      '''
      )

    child_id = cursor.fetchone()
    return child_id[0]


def addGift(gift_name, child_name):
  try:
    print("getchildid called")
    child_id = _getChildId(child_name)
  except TypeError:
    print("add child called")
    child_id = _addChild(child_name)

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

def deleteGift(gift_name, child_name):
  child_id = _getChildId(child_name)

  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        f'''
        DELETE FROM Gifts
        WHERE Gifts.ChildId = {child_id}
        AND Gifts.GiftName = '{gift_name}';
        '''
      )
    except sqlite3.OperationalError as err:
      print("oops", err)

def deliverGifts(child_name):
  child_id = _getChildId(child_name)
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        f'''
        UPDATE Gifts
        SET Delivered = 1
        WHERE Gifts.ChildId = {child_id};
        '''
      )
    except sqlite3.OperationalError as err:
      print("oops", err)


if __name__ == "__main__":
  addGift("tennis ball", "Andy")