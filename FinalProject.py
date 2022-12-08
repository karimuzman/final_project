#Vending Machine Program
#By Uzman Karim, Student, DCP-ICS online a22
#Version 1.0

money = 10.00 #This money domination will be used to buy items!
vending_machine = {"Bunties": 1, "Chocolate": 2, "Cola": 3, "Juice": 4, "Water": 5}
bought_product = []
prices = {"Bunties": "1.50", "Chocolate": "2.50", "Cola": "3.00", "Juice": "4.00", "Water": "3.50"}

def purchase(needed_money,product_name): # To cater the money matter to buy one or more products!
    global money
    global bought_product
    if money >= needed_money:
        money -= needed_money
        bought_product.append(product_name)
        print("Can proceed to buy")
    else:
        print("Not enough money")

def transaction(user_input): # To handle the list of wished transactions for our buyer!
    global money
    if user_input == "1":
        purchase(1.50,"Bunties")
    elif user_input == "2":
        purchase(2.50, "Chocolate")
    elif user_input == "3":
        purchase(3.00, "Cola")
    elif user_input == "4":
        purchase(4.00, "Juice")
    elif user_input == "5":
        purchase(3.50, "Water")

    else:
        print("Invalid Input")

def main(): #Main Program that will cater the functionality of VMP by using various selfdeveloped and inbuilt functions!
    item_list = []
    switch = True
    while switch:
        print("Welcome to my Vending Machine Program")
        print("Here is your choices!")
        for item, selection in vending_machine.items():
            item_list.append((item, selection))

        print(item_list[::-1])

        print()
        print("Here are the prices")
        for item, price in prices.items():
            print(item, price)
        print()

        user_switch = True
        while user_switch:
            print("You currently have $" + str(money))
            user_input = input("Please input your choice:").upper()
            transaction(user_input)
            print()

            choice = True
            while choice:
                user_input = input("Are you finished with your buying?(y/n): ").lower()
                if user_input == "y":
                    user_switch = False
                    choice = False
                    switch = False
                elif user_input == "n":
                    user_switch = True
                    choice = False
                else:
                    print("Invalid command")
                    choice = True
        print(" ".join(bought_product))
        print("Thank you for buying with us")
        print("Please take the balance $=", money)

main()

