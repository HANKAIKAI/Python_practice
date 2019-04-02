stuff = {'rope': 1,'torch': 6,'gold coin': 42,'dagger': 1,'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    totleItems = 0
    for obj, num in inventory.items():
        print('{} {}'.format(num, obj))
        totleItems += num
    print('Total number of items: {}'.format(totleItems))
displayInventory(stuff)    
