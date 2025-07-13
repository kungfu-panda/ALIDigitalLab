import sqlite3


def create_group_table():
  db = sqlite3.connect("groups.db")
  cursor = db.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups(
      group_id INTEGER PRIMARY KEY AUTOINCREMENT,      
      group_name TEXT NOT NULL,
      group_owner TEXT NOT NULL,
      
    )
  """)
  pass



