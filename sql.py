import sqlite3
class Database:
  def __init__(self, db_directory):
    self.db_directory = db_directory
    self.con = sqlite3.connect(self.db_directory)
    self.cur = self.con.cursor()

  def create_table(self, table, *columns):
    try:
      assert table not in [self.cur.execute(
        f"SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchone()]
      self.cur.execute(
        f"CREATE TABLE {table}{str(tuple([column for column in columns]))}")
    except:
      print("table already exists")

  def add_entries(self, table, *entries):
    for entry in entries:
      self.cur.execute(
          f"""INSERT INTO {table} {tuple(entry.keys())} VALUES{tuple(entry.values())}""")
      self.con.commit()

  def fetch_all_entries(self, table):
    self.allentries = self.cur.execute(f"SELECT * from {table}").fetchall()
    return self.allentries
  def advanced_sql_usage(self, string):
    arg = self.cur.execute(string)
    self.con.commit()
    return arg

if __name__ == "__main__":
  Database().run()
