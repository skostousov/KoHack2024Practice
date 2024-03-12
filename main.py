from sql import Database

database = Database("database.db")
database.create_table("houses", "name", "price", "size")
database.add_entries("houses", {"name":"Bob's house", "price":"1500 dollars", "size":"5 square feet"}, {"name": "Jim's cottage", "price":"6 dollars"})
print(database.fetch_all_entries("houses"))
#blah blah blah #making a change as a test Aharon hello
#there is a built in AI on this Replit
#someone once came over to me and asked me what its like to be a 
#AAron try commiting a change. click git in the bottom left
print("helloworld")