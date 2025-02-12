Inventory={}


def add_item():
    item_id=input("Enter item ID:")
    if item_id in Inventory:
        print("Item already exits.Use update")
        return
    name=input("Enter item name:")
    quantity=int(input("Enter quantity:"))
    price=float(input("Enter price per unit:"))
    Inventory[item_id]={
        "name":name,
        "quantity":quantity,
        "price":price,
    }
    print("Item added successfully")

def update_item():
     item_id=input("Enter item Id to update")
     if item_id not in Inventory:
         print("Item not found")
         return
     quantity= int(input("Enter new quantity:"))
     price= float(input("Enter new price per unit:"))

     Inventory[item_id]["quantity"]=quantity
     Inventory[item_id]["price"]=price
     print("Item updated successfully")

def view_item():
    if not Inventory:
        print("nothing is in inventory")

    print("\nCurrent Inventory:")
    for item_id,details in Inventory.items():
        print(f"ID:{item_id},Name:{details['name']},Quantity:{details['quantity']},Price:{details['price']}")

def search_item():
    query=input("Enter item ID or name to search:").lower()
    found=False
    for item_id,details in Inventory.items():
        if query in item_id or query in details["name"].lower():
            print(f"Id:{item_id},Name;{details['name']},Quantity:{details['quantity']},Price:{details['price']}")
            found=True
        if not found:
            print("Item not found")


def main():
    while True:
        print("\nInventory Management system")
        print("1.Add Item")
        print("2.Update Item")
        print("3.View inventory")
        print("4.Search Item")
        print("5.Exit")
        choice=input("Enter your choice:")

        if choice=="1":
            add_item()
        elif choice=="2":
            update_item()
        elif choice=="3":
            view_item()
        elif choice=="4":
            search_item()
        elif choice=="5":
            print("Exiting..Goodbye!")
            break
        else:
            print("Invalid choice.pls select a valid choice")

if __name__=="__main__":
    main()





