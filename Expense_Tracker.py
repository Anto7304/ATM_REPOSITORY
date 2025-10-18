print("Welcome to your  expense tracker\n")

#initialization 
vegetables = 0
fruits = 0
cereals = 0
food = 0
rent = 0
transport = 0
others = 0

while True:
    print("Enter you selection : \n 1.vegetable\n 2.fruits\n 3.cereals\n 4.food\n 5.rent\n 6.transport\n 7.others\n 8.exit")

    selection = input(" \n")

    if selection == "8":
        print("you have exit your selction")
        break

    amount = input("\nEnter the amount spent : ")

    if not amount.isdigit():
        print("Amount must be a number ")
        break
    else:
        
        spent = float(amount)
        print(f"amount : {spent:.2f}\n")

    if selection == "1":
        vegetables += spent
        print("The amount was added to vegetable")
    elif selection == "2":
        fruits += spent
        print("The amount have been added to the fruits")
    
    elif selection == "3":
        cereals += spent
        print("The amount have been added to the cereals")

    elif selection == "4":
        food += spent
        print("The amount have been added to the food")

    elif selection == "5":
        rent += spent
        print("The amount have been added to the rent")
    
    elif selection == "6":
        transport += spent
        print("The amount have been added to the transport")
    
    elif selection == "7":
        others += spent
        print("The amount have been added to the others")

    else:
        print("invalid option\n")
        break
    

print("\nThis are your expenses\n")

print(f" 1.Vegetables : {vegetables:.2f}")
print(f" 2.Fruits : {fruits:.2f}")
print(f" 3.Cereals : {cereals:.2f}")
print(f" 4.Food : {food:.2f}")
print(f" 5.Rent : {rent}")
print(f" 6.Transport : {transport}")
print(f" 7.Other : {others}\n")

total = vegetables + food + fruits + cereals + rent + transport + others

print("---------------------------------\n\n")
print(f"Total expenses : {total}")
print("---------------------------------\n\n")

