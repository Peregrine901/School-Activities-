  print("Grocery Inventory Manager\n2d Grocery List\n1- View an item\n2- Update an item\n3- Add a new item\n4- Remove an Item")

groceries = [
    ["Apple", 25.00, 10],
    ["Bread", 55.00, 5],
    ["Milk", 75.00, 3]
]
for items in groceries:
    print(items)

choice = int(input("Please Chooose What you want to do with your list [1 - 4]: "))

if choice == 1:
    view_item = int(input("Please choose an Item [0-2]: "))
    if view_item == 0:
        print(f'Item = {groceries[0][0]}\nPrice = {groceries[0][1]}\nQuantity = {groceries[0][2]}')
    elif view_item == 1:
        print(f'Item = {groceries[1][0]}\nPrice = {groceries[1][1]}\nQuantity = {groceries[1][2]}')
    elif view_item == 2:
        print(f'Item = {groceries[2][0]}\nPrice = {groceries[2][1]}\nQuantity = {groceries[0][2]}')
    else:
        print("Invalid Option. Try again.")
elif choice == 2:
    updt = int(input("1- Update Item Price\n2- Update Item quantity\nChoose what to update[1 - 2]"))
    if updt == 1:
        print("Update Item")
        item = int(input("Enter Item Number: "))
        new_price = float(input("Enter New Price: "))
        groceries[item][1] = new_price
        print(f'Updated Grocery List:\n{groceries}')
    elif updt == 2:
        print("Update Item Quantity")
        item = int(input("Enter Item Number: "))
        new_quanti = float(input("Enter New Quantity: "))
        groceries[item][2] = new_quanti
        print(f'Updated Grocery List:\n{groceries}')
    else:
        print("Invalid Option. Try Again.")
elif choice == 3:
    new_item = input('Insert the name of the new item to be added: ')
    item_price = float(input("insert the price of the new item: "))
    item_quantity = input("Insert the quantity of the new item: ")
    groceries.append([new_item,item_price,item_quantity])
    print(groceries)
elif choice == 4:
    rem = int(input("Enter Item row you want to remove[0-2]: "))
    spe_item = int(input("Enter the item you want to remove[0-2]: "))
    groceries[rem].pop(spe_item)
    print(f'Item has been removed. Updated List:\n{groceries}')
else:
    print("Invalid Choice. Please Choose again.")
