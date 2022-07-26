import pandas as pd


admin_details = {"Aniket": "Aniket@30"}

inventory = {1: {'Name': 'Tandoori Chicken', 'FoodID': 1, 'Price': 240, 'Quantity': '4 pieces','Discount':'30%',"Stock":100},
        2: {'Name':  'Vegan Burger', 'FoodID': 2 , 'Price': 320, 'Quantity': 1, 'Discount':'10%',"Stock":50},
        3: {'Name': 'Truffle Cake', 'FoodID': 3, 'Price': 900, 'Quantity': '500 gm','Discount':'15%',"Stock":30}}

def add_new_items():
    Name= input("Enter the Name: ")
    Foodid= max(inventory.keys())+1
    Price= int(input("Enter the price of the item: "))
    Quantity= int(input("Enter the quantity of item: "))
    Discount=int(input("Enter the discount value: "))
    Stock=int(input("Enter the stock available: "))
    inventory[Foodid] = {
        "Name": Name ,
        "FoodID": Foodid,
        "Price": Price,
        "Quantity": Quantity,
        "Discount": Discount,
        "Stock":Stock
    }
    print("The Item" +Name+  "is added successfully") 
    return inventory

def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    c = int(input("Enter the stock of the item"))
    d= int(input("Enter the discount of the item "))
    e=int(input("Enter the stock available"))
    inventory[item]["Name"] = a
    inventory[item]["Price"] = b
    inventory[item]["Stock"] = c
    inventory[item]["Discount"]=d
    inventory[item]["Stock"]=e
    print("*****item are Edited  successfully*****")
    return inventory   

def show_inventory():
    print("*****The inventory includes*****")
    inv=pd.DataFrame(inventory)
    print(inv) 

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inventory.pop(d)
    print("Remove item successfully ")
    return inventory                                        