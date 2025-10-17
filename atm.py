
maxAttempts = 3

#initializing the credentials
correctName = "Anthony Maina"
correctPin = 1234
initialBalance = 1000

attempts =0

#login
login = False

while attempts < maxAttempts:
    print("ATM ACCOUNT\n")
    name = input("Enter your name : ")
    pin = int(input("Enter your pin : "))


    if name == correctName and pin == correctPin:
        print("Login successfull\n")
        login =True
        break
    else:

        attempts +=1
        remainingAttempts = maxAttempts - attempts
        print ("Incorrect name or pin")

        if remainingAttempts > 0 :
            print(f"Try again. Attempts remaining : {remainingAttempts}")
        else:
            print("Account Blocked . Too many trials.")

if not login:
    raise SystemExit(0)

#Menu
#main ATM loop
while True:
    print("ATM MENU\n")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. checkbalance")
    print("4. change pin")
    print("5. exit")

    choice = input("Enter Your Choice : ")

#choice 1 - Deposit
    if choice == "1": 
        print("Welcome To Deposit Money")
        
        amount = float(input("Enter the amount todeposit : "))

        if amount >0:
            balance = initialBalance + amount
            print(f"Amount deposited : {amount:.2f}\n Total balance : {balance:.2f}")
            break
        else:
            print ("Invalid amount")
            break

# choice 2 - withdraw 
    elif choice == "2":
        print(f"Withdrawing money")

        amount = float(input("Enter the amount you want to withdraw : "))

        if amount > 0 and amount <= initialBalance:
            balance = initialBalance - amount
            print(f" Withdrawed : Kes {amount:.2f}\n Balance : Kes {balance:.2f}")
            break
        elif amount < 0:
            print("You cannot withdraw less than kes 0")
            break
        elif amount > initialBalance:
            print (f"Insufficient funds in your ATM.Your balance : {initialBalance:.2f}\n")
            break
        else:
            print("Unable to withdraw money in your ATM")
            break
#choice 3 - check balance
    elif choice == "3":
        print(f"Your Balance is : {initialBalance}")
        break

#choice 4 for changing pin
    elif choice == "4":
        print("Do you want to change pin (y/n) : ",end=" ")
        
        option = input()
        if option == "y":
            old = int(input("Enter your old pin"))

            if old == correctPin:
                newPin = int(input("Enter your new pin"))
                confirm = int(input("Confirm your new pin"))

                if confirm == newPin:
                    newPin = correctPin

                
                    print("You have changed your pin successfully")
                    break
                    
                else:
                    print("New pin does not match with the confirm pin")
                    break

            else:
                print:("Wrong old pin")
                break
            

        elif option == "n":
            print("Pin not Changed")
            break
        else:
            print("Invalid option")
            break

#choice 5 - exiting
    elif choice == "5" :
        print("Are you sure you want to exit? (y/n)",end=" ")

        option = input()

        if option == "y":
            print("Thanks for using our ATM")
            break
        elif option == "n":
            print("Returning to the main Menu")

        else:
            print("invalid option")
            break

#invalid choice  
    else:
        print("Invalid Choice Selected")
    


    





    

        




