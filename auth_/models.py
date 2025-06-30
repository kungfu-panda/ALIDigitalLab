import sqlite3


class AuthUtils:

  def __init__(self) -> None:
    self.sqlite = sqlite3

  def get_cur(self):
    db = self.sqlite.connect('auth.db')
    return db, db.cursor()

  def shut(self, db):
    db.commit()
    db.close()

  def create_user_table(self):
    db, cursor = self.get_cur()
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        acctype TEXT NOT NULL
      )
    ''')
    self.shut(db)

  def user_exists(self, username) -> bool:
    db, cursor = self.get_cur()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username, ))
    user = cursor.fetchone()
    if user is None:
      return False
    else:
      return True

  def add_demo_accounts(self):
    db, cursor = self.get_cur()
    cursor.execute(
        'INSERT INTO users (username, password, acctype) VALUES (?, ?)',
        ('admin', 'admin', 'admin'))
    self.shut(db)

  def verify_user(self, username, password) -> bool:
    db, cursor = self.get_cur()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                   (username, password))
    user = cursor.fetchone()
    return (user is not None)

  def add_user(self, username, password, acctype):
    db, cursor = self.get_cur()
    cursor.execute(
        'INSERT INTO users (username, password, acctype) VALUES (?, ?, ?)',
        (username, password, acctype))
    self.shut(db)

  def del_user(self, username, passwrod):
    db, cursor = self.get_cur()
    if self.verify_user(username, passwrod):
      cursor.execute('DELETE FROM users WHERE username = ? AND password = ?',
                     (username, passwrod))
      self.shut(db)
      return True
    else:
      return False
