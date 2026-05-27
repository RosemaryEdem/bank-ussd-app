# BANK USSD APP

# 1. Store the account details

account_name = "Rosie"
pin = "2424"
balance = 5620

# 2. def functions

def check_balance(balance):
    print(f"Your balance is N{balance}")


def buy_airtime(balance):
    amount = float(input("Enter airtime amount: "))
    if amount > balance:
            print("Insufficient funds")
    else:
            balance = balance - amount
            print(f"Airtime of N{amount} purchased successfully")
            print(f"New balance is N{balance}")
    return balance


def transfer_money(balance):
    recipient = input("Enter recipient name: ")
    amount = float(input("Enter amount to transfer: "))
    if amount > balance:
            print("Insufficient funds")
    else:
            balance = balance - amount
            print(f"N{amount} transferred to {recipient} successfully")
            print(f"New balance is N{balance}")
    return balance


def change_pin(pin):
    old_pin = input("Enter current pin: ")
    if old_pin == pin:
                new_pin = input("Enter new pin: ")
                confirm_pin = input("confirm new pin: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print ("pin changed successfully!")
                else:
                    print("pins do not match!")
    else:
                print("Incorrect pin")
    return pin


def show_menu():
    menu_items = [
    "=== FIRSTBANK MENU ===",
    "1. Check Balance",
    "2. Buy Airtime",
    "3. Transfer Money",
    "4. Change PIN",
    "5. Exit"
    ]
    for item in menu_items:
          print(item)


# 3. Welcome the user and ask for PIN

print("welcome to firstbank")
print("Please enter your PIN")
enter_pin = input("PIN: ")

# 4. If PIN is correct, Welcome user and show menu but if PIN is wrong, deny access and stop
if enter_pin == pin:
    print(f"Welcome, {account_name}!")
else: 
    print("access denied")
    exit()

# 5. Menu keeps repeating until user exits
while True:
    show_menu()
    choice = input("Enter option: ")
    
    if choice == "1":
          check_balance(balance)
    elif choice == "2":
          balance = buy_airtime(balance)
    elif choice == "3":
          balance = transfer_money(balance)
    elif choice == "4":
          pin = change_pin(pin)
    elif choice == "5":
          print("Goodbye Rosie!")
          break
    else:
          print("invalid option")
