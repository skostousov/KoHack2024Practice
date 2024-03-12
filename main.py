from sql import Database
import menu
database = Database("database.db")
database.create_table("houses", "name", "price", "size")
database.add_entries("houses", {"name":"Bob's house", "price":"1500 dollars", "size":"5 square feet"}, {"name": "Jim's cottage", "price":"6 dollars"})
print(database.fetch_all_entries("houses"))