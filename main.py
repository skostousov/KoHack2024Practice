from sql import Database
import menu
import matplotlib.pyplot as plt
from PIL import Image
import time
import numpy as np

image = np.asarray(Image.open("spider.png"))
imgplot = plt.imshow(image)
database = Database("database.db")
database.create_table("houses", "name", "price", "size")
database.add_entries("houses", {
    "name": "Bob's house",
    "price": "1500 dollars",
    "size": "5 square feet"
}, {
    "name": "Jim's cottage",
    "price": "6 dollars"
})
print(database.fetch_all_entries("houses"))
menu = menu.Menu()
menu.run()
print("hello")
