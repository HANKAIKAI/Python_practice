dragonLoot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'rudy']
inv = {'gold coin': 42,'rope': 1}

def addToInventory(itemList):
    d = {}
    for item in itemList:
        if item not in d:
            d[item] = 1
        else:
            d[item]+= 1
    return d

def addIninv(inv, countElement):
    for keys in countElement:
        if keys in inv:
            inv[keys] += countElement[keys]
        else:
            inv[keys] = countElement[keys]
    return inv

def displayInventory(inventory):
    print('Inventory:')
    totleItems = 0
    for obj, num in inventory.items():
        print('{} {}'.format(num, obj))
        totleItems += num
    print('Total number of items: {}'.format(totleItems))


countedElement = addToInventory(dragonLoot) #{'gold coin': 3, 'rudy': 1, 'dragger': 1}
finalInv = addIninv(inv, countedElement) #{'gold coin': 45, 'rope': 1, 'dragger': 1, 'rudy': 1}
displayInventory(inv)
