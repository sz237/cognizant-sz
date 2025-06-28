# Project 4: Implement Your own Data Structures

import random

inventory = {"apple": (10, 2.5),
             "banana": (20, 1.2),
             "peaches": (5, 3.0)}


print("Welcome to the Inventory Manager!")
print("Current inventory: ")

for item, info in inventory.items():
    print("Item:", item, "Quantity:", info[0], "Price", info[1])


addItem = str(input("Would you like to add an item? If so, input the name. Otherwise input 'n'."))
if addItem != 'n':
    if addItem in inventory.keys():
        inventory[addItem] = (inventory[addItem][0] + 1, inventory[addItem][1])
    else:
        inventory[addItem] = (1, random.randint(1,10))
    
    print("Updated inventory: ")
    for item, info in inventory.items():
        print("Item:", item, "Quantity:", info[0], "Price", info[1])

else:
    print("Current inventory: ")
    for item, info in inventory.items():
        print("Item:", item, "Quantity:", info[0], "Price", info[1])


removeItem = str(input("Would you like to remove an item? If so, input the name. Otherwise input 'n'."))
if removeItem != 'n' and removeItem in inventory.keys():
    del inventory[removeItem]

    print("Updated inventory: ")
    for item, info in inventory.items():
        print("Item:", item, "Quantity:", info[0], "Price", info[1])
    
else:
    print("Current inventory: ")
    for item, info in inventory.items():
        print("Item:", item, "Quantity:", info[0], "Price", info[1])



