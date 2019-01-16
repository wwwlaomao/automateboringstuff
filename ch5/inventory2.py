#!/usr/bin/env python3

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total = total + v
    print('Total number of items: ' + str(total))

def addToInventory(inv, dragonLoot):
    for l in dragonLoot:
        inv.setdefault(l, 0)
        inv[l] = inv[l] + 1
    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
