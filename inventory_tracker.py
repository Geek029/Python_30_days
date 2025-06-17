inventory ={
    "Mobilephones" : 50,
    "Laptops" : 40,
    "Smartwatch" : 25,
    "Refrigerator" : 20
}

def add_item(item, quantity) :
    if item not in inventory :
        print(f"New item {item} found. Adding to the inventory")
        inventory[item] = quantity
    else :
        print(f"Item {item} found in inventory. Updating quantity")
        inventory[item] += quantity
    print(inventory)

def remove_item(item, quantity=None) :
    if item not in inventory:
        print(f"{item} not found in inventory")
        return
    if quantity is None :
        del inventory[item]
        print(f"{item} removed from inventory")
    else:
        inventory[item] -= quantity
        print(f"Removed the mentioned quantity {quantity} from {item}")
        if inventory[item] <= 0:
            inventory[item]=0
            print(f"{quantity} is more than the stock present in inventory. Defaulting to 0")
    print(inventory)

def show_inventory(item=None):
    if item is None:
        print(inventory)
    elif item is not None :
        print(inventory[item])

show_inventory()

