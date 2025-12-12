"""
Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].
"""

def update_inventory(inventory, shipment):
    new = {}

    for i in inventory:
        if i[1] in new:
            new[i[1]] += i[0]
        else:
            new.update({i[1]:i[0]})

    for i in shipment:
        if i[1] in new:
            new[i[1]] += i[0]
        else:
            new.update({i[1]:i[0]})
        
    
    return [[y,f"{x}"] for x,y in new.items()]


# print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))


print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]))


"""
1. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) should return [[3, "apples"], [8, "bananas"]].
Passed:2. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
Passed:3. update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
Passed:4. update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].
"""