# BANK USSD APP

# 1. Store the account details

account_name = "Rosie"
pin = "2424"
balance = 5620

# Welcome the user and ask for PIN
print("welcome to firstbank")
print("Please enter your PIN")
enter_pin = input("PIN: ")

# If PIN is correct, Welcome user and show menu but if PIN is wrong, deny access and stop
if enter_pin == pin:
    print(f"Welcome, {account_name}!")
else: 
    print("access denied")
    exit()

# Menu keeps repeating until user exits
while True:
    print("=== FIRSTBANT MENU ===")
    print("1. Check Balance")
    print("2. Buy Airtime")
    print("3. Transfer Money")
    print("4. Change PIN")
    print("5. Exit")
    choice = input("Enter option: ")

# Option 1 -> Check balance
    if choice == "1":
        print(f"Your balance is N{balance}")

# Option 2 -> Buy airtime
    elif choice == "2":
        amount = float(input("Enter airtime amount: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(f"Airtime of N{amount} purchased successfully")
            print(f"New balance is N{balance}")

    elif choice == "3":
        recipient = input("Enter recipient name: ")
        amount = float(input("Enter amount to transfer: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(f"N{amount} transferred to {recipient} successfully")
            print(f"New balance is N{balance}")


    elif choice == "4":
            old_pin = input("Enter current PIN: ")
            if old_pin == pin:
                new_pin = input("Enter new PIN: ")
                confirm_pin = input("confirm new PIN: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print ("PIN changed successfully!")
                else:
                    print("PINs do not match!")
            else:
                print("Incorrect PIN")


    elif choice == "5":
        print("Goodbye Rosie!")
        break
    else:
        print("Invalid option")




