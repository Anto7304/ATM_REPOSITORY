#Display at the screen of the user
print("WELCOME TO THE INVENTORY MANAGEMENT SYSTEM\n")

print("What do you want to do? Select the option.\n")

print("  1. Add item")
print("  2. Sell item")
print("  3. View Stock ")
print("  4. Exit")

#initialization of 3 items
bread = 0
milk = 0
sugar = 0

while True:
    choice = input("\nEnter your choice between 1, 2, 3 and 4 : ")
    
    if not choice.isdigit():
        print("Choice must be a number")
        continue

    selection = int(choice)

#addint item to stock
    if selection == 1:

        item = input("Enter an item to add : ").replace(" ","").lower()

        if item != "bread" and item != "milk" and item !="sugar":
            print("Item is not in the stock")
            continue

        quantity_Input = input("Enter the quantity to add : ")
        
        if not quantity_Input.isdigit():
            print("Quantity must be a number ")
            break

        quantity  = int(quantity_Input)

        if quantity < 0 :
            print("Quantity cannot be less than 0")

#
        

        if item == "bread" :
            bread +=quantity
            print(f"Quantity added to bread {quantity:.2f}")
            print(f"Bread Stock : {bread}")
            

        elif item == "milk":
            milk +=quantity
            print(f"Quantity added to milk : {quantity}")
            print(f"Milk Stock : {milk}")


        elif item == "sugar":
            sugar += quantity
            print(f"Quantity added to sugar : {quantity}")
            print(f"Sugar stock : {sugar}")
        
        else:
            print("Item not in the stock")

#Selling an item

    elif selection == 2:
        item=input("Enter Item to buy : ").lower()
        
        if item.isdigit():
            print("Enter the name of the item")
            break

        if item != "bread" and item != "milk" and item !="sugar":
            print("Item is not in the stock")
            continue

        quantity_input= input("Enter quantity to buy : ")

        if not quantity_input.isdigit():
            print("Quantity must be a number")
            break

        quantity = int(quantity_input)

        print(f"Item selected : {item}")
        print(f"Quantity : {quantity}")

        if  item == "bread":
            if bread > 0 and bread >= quantity:
                bread -= quantity
                print(f"Bread sold : {quantity}")
                print(f"Bread remained : {bread}")

            elif bread < quantity:
                bread -= quantity
                print(f"Bread is less in stock by : {bread}")
                

            else:
                print("Bread is out of stockc!! ")
                break
    
        elif item == "milk":

            if milk > 0 and milk >= quantity:
                milk -= quantity
                print(f"Milk sold : {quantity} ")
                print(f"Milk remained : {milk}")

            elif milk < quantity:
                milk -= quantity
                print(f"Milk is less in the stock by : {milk}")

            else:
                print(f"Milk is out of stock")
                break
        elif item == "sugar":
            if sugar > 0 and sugar >= quantity:
                sugar -= quantity
                print(f"Sugar sold : {quantity} ")
                print(f"Sugar remained : {sugar}")

            elif milk < quantity:
                sugar -= quantity
                print(f"Sugar is less in the stock by : {sugar}")

            else:
                print(f"Sugar is out of stock")
                break
        
# Viewing the stock

    elif selection == 3:
        print ("This are the items in the stock : ")

        print(f"Bread in stock : {bread}")
        print(f"Sugar in stock : {sugar}")
        print(f"milk in stock  : {milk}")

    elif selection == 4:
        print("Are You are exiting your inventory system? (y/n) :",end="")

        desicion = input(" ")

        if desicion.isdigit():
            print("input y for yes and n for no")
            break

        if desicion == "y":
            print("Thank you for using the system")
            print("Yuo have exited the system successfull")
            break
        elif desicion == "n":
            print("you have not exited")
        else:
            print("Input your decision")

#default message
    else:
        print("Inavalid choice made")





