#Importing my file named cafeclass to able to use the private class.
import cafeclass
cafe_tbs = cafeclass.cafe()

#A list that contains all the tables that are available.
CafeTB_list = {1:"1. Table 1", 2:"2. Table 2", 3:"3. Table 3", 4:"4. Table 4", 5:"5. Table 5", 6:"6. Table 6"}
#Lists that contains all the waiters
waiter_Sarah = []
TBkeys_Sarah = []
waiter_Thabang = []
TBkeys_Thabang = []
waiter_Lucy = []
TBkeys_Lucy = []
waiter_Pieter = []
TBkeys_Pieter = []
waiter_Motseki = []
TBkeys_Motseki = []
waiter_Sharon = []
TBkeys_Sharon = []
#A list to add the amount of customers to each table.
tableCS_list = [cafe_tbs.customers, cafe_tbs.customers, cafe_tbs.customers, cafe_tbs.customers, cafe_tbs.customers, cafe_tbs.customers]
#A list that contains the total prices for each table.
Totalprice = [cafe_tbs.orders, cafe_tbs.orders, cafe_tbs.orders, cafe_tbs.orders, cafe_tbs.orders, cafe_tbs.orders]
#A list that shows if the tables prepared a bill.
table_bill = [cafe_tbs.bill, cafe_tbs.bill, cafe_tbs.bill, cafe_tbs.bill, cafe_tbs.bill, cafe_tbs.bill,]
#A list that contains each item that was ordered by the tables. 
table_items = ["None", "None", "None", "None", "None", "None",]
#A list that contains quantities for the items that was ordered by the tables. 
table_quantity = [0, 0, 0, 0, 0, 0]
#A list that contains prices for the items that was ordered by the tables. 
table_price = [0, 0, 0, 0, 0, 0]
#A list that contains the items from the menu.
order_items = ['Coke', 'Fanta', 'Sprite', 'Garlic Snails', 'Calamari', 'Wings', 'Steak', 'Chicken', 'Pork', 'Ice-cream', 'Waffle', 'Cake']
#A list that contains the prices from the menu.
order_price = [25, 25, 25, 55, 70, 65, 120, 109, 110, 56, 73, 45]
#Lists used for the save bill in txt file
Bill_item = []
Bill_quantity = []
Bill_price = []
Main_bill = []

#Defining a function/creating a function that display the start menu/main menu of the application.
def main_menu():
   print("\033[32m" + "What would you like to do today?"+ "\033[0m""\n\n""\033[36m" + "1. Assign Table" +"\033[0m""\n""\033[36m" + "2. Change customres" + "\033[0m""\n""\033[36m" + "3. Add to Order" + "\033[0m""\n""\033[36m" + "4. Prepare bill" + "\033[0m""\n""\033[36m" + "5. Complete Sale" + "\033[0m""\n""\033[36m" + "6. Cashup" + "\033[0m""\n""\033[31m" + "0. Log Out"+ "\033[0m")
#Defining a function/creating a function that display the order menu of the application.
def order_menu():
    NM_order = 0
    print("Select an item from the list to add to order\n")
    with open('Stock.txt','r') as file:
        for line in file:
            NM_order += 1
            item = line.split(',')[0]
            price = (line.split(',')[1])[:-1]
            print(f"{NM_order}. {item} R{price}")
#Defining a function/creating a function that will be the main code for the application to be able to run.
def main_code():
    Totale_sale = 0
    while True:
        #Checking the login for the application.
        login_choice = input("\033[35m" + "Welcome to Highlands Cafe" + "\033[0m""\n""\033[32m" + "1. Login" + "\033[0m""\n""\033[31m" + "2. Exit"+ "\033[0m""\n")
        if login_choice == "1":
            print("User login\n")
            while True:
                waiter_username = input("Please enter username: ")
                with open('Login.txt','r') as file:
                    for line in file:
                        w_username = line.split(',')[0]
                        if w_username == waiter_username:
                            valid = True
                            w_password = (line.split(',')[1])[:-1]
                            waiter_password = input("Please enter password: ")
                            if waiter_password == w_password:
                                valid = True
                                file.close()
                                break
                            else:
                                valid = False
                                file.close()
                                print("Invalid username or password, try again!")
                                print(" ")
                                break
                        else:
                            valid = False
                if valid == True:
                    while True:
                        print("\033[34m" + f"\nWelcome {waiter_username}" + "\033[0m")
                        main_menu()
                        #Defining a function/creating a function that display the tables assign to the waiters.
                        def display_wtTB():
                            if waiter_username == "Sarah":
                                    for i in range(len(waiter_Sarah)):
                                        print(waiter_Sarah[i])
                            elif waiter_username == "Thabang":
                                    for i in range(len(waiter_Thabang)):
                                        print(waiter_Thabang[i])
                            elif waiter_username == "Lucy":
                                    for i in range(len(waiter_Lucy)):
                                        print(waiter_Lucy[i])
                            elif waiter_username == "Pieter":
                                    for i in range(len(waiter_Pieter)):
                                        print(waiter_Pieter[i])
                            elif waiter_username == "Motseki":
                                    for i in range(len(waiter_Motseki)):
                                        print(waiter_Motseki[i])
                            elif waiter_username == "Sharon":
                                    for i in range(len(waiter_Sharon)):
                                        print(waiter_Sharon[i])

                        #When the waiter input 1 to select/assign to a table.
                        waiter_choice = input("")
                        if waiter_choice == "1":
                            while True:
                                print(" ")
                                print("Please select one of the available tables or press 0 to exit")
                                print(" ")
                                for i in CafeTB_list.values():
                                    print(i)
                                try:
                                    table_option = int(input(""))
                                except ValueError:
                                    print("Invalid input, try agian!")
                                    break
                                if table_option == 0:
                                    break
                                elif table_option > 0 and table_option <= 6:
                                    if waiter_username == "Sarah":
                                        table_NM1 = CafeTB_list.pop(table_option)
                                        waiter_Sarah.append(table_NM1)
                                        TBkeys_Sarah.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Sarah)):
                                                print(waiter_Sarah[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ")
                                    elif waiter_username == "Thabang":
                                        table_NM2 = CafeTB_list.pop(table_option)
                                        waiter_Thabang.append(table_NM2)
                                        TBkeys_Thabang.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Thabang)):
                                                print(waiter_Thabang[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ")
                                    elif waiter_username == "Lucy":
                                        table_NM3 = CafeTB_list.pop(table_option)
                                        waiter_Lucy.append(table_NM3)
                                        TBkeys_Lucy.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Lucy)):
                                                print(waiter_Lucy[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ")
                                    elif waiter_username == "Pieter":
                                        table_NM4 = CafeTB_list.pop(table_option)
                                        waiter_Pieter.append(table_NM4)
                                        TBkeys_Pieter.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Pieter)):
                                                print(waiter_Pieter[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ")
                                    elif waiter_username == "Motseki":
                                        table_NM5 = CafeTB_list.pop(table_option)
                                        waiter_Motseki.append(table_NM5)
                                        TBkeys_Motseki.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Motseki)):
                                                print(waiter_Motseki[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ")
                                    elif waiter_username == "Sharon":
                                        table_NM6 = CafeTB_list.pop(table_option)
                                        waiter_Sharon.append(table_NM6)
                                        TBkeys_Sharon.append(table_option)
                                        print(f"Table {table_option} successfully assigned to {waiter_username}.")
                                        add_cst = input("Do you want to add customers to the table? y/n: ").lower()
                                        if add_cst == "y":
                                            for i in range(len(waiter_Sharon)):
                                                print(waiter_Sharon[i])
                                            select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                            if select_tbl == 0:
                                                break
                                            amount_cst = int(input("How many customers are seated at the table?: "))
                                            tableCS_list[select_tbl-1] = amount_cst
                                            break
                                        elif add_cst == "n":
                                            break
                                        else:
                                            print("Invalid input! Try agian.")
                                            print(" ") 
                                else:
                                    print("Invalid input, try again!")
                                    break

                        #When the waiter input 2 to add customers to the tables.
                        elif waiter_choice == "2":
                            while True:
                                print(" ")
                                if waiter_username == "Sarah":
                                    for i in range(len(waiter_Sarah)):
                                        print(waiter_Sarah[i])
                                elif waiter_username == "Thabang":
                                    for i in range(len(waiter_Thabang)):
                                        print(waiter_Thabang[i])
                                elif waiter_username == "Lucy":
                                    for i in range(len(waiter_Lucy)):
                                        print(waiter_Lucy[i])
                                elif waiter_username == "Pieter":
                                    for i in range(len(waiter_Pieter)):
                                        print(waiter_Pieter[i])
                                elif waiter_username == "Motseki":
                                    for i in range(len(waiter_Motseki)):
                                        print(waiter_Motseki[i])
                                elif waiter_username == "Sharon":
                                    for i in range(len(waiter_Sharon)):
                                        print(waiter_Sharon[i])
                                try:
                                    select_tbl = int(input("Select table to assign customers or 0 to exit: "))
                                except ValueError:
                                    print("Invalid input, try agian!")
                                    break
                                if select_tbl == 0:
                                    break
                                elif select_tbl > 0 and select_tbl <= 6:
                                    try:
                                        amount_cst = int(input("How many customers are seated at the table?: "))
                                    except ValueError:
                                        input("Invalid input, try again!")
                                        break
                                    tableCS_list[select_tbl-1] = amount_cst
                                    break
                                else:
                                    print("Invalid input ,try again!")
                                    break
                        
                        #When the waiter input 3 to add a order.
                        elif waiter_choice == "3":
                            while True:
                                print("Select a table to add orders to:\n")
                                display_wtTB()
                                try:
                                    select_tbl = int(input("Please select a table or 0 to exit: "))
                                except ValueError:
                                    input("Invalid input, try again!")
                                    break
                                if select_tbl == 0:
                                        break
                                elif select_tbl > 0 and select_tbl <= 6:
                                    while True:
                                        order_menu()
                                        try:
                                            waiter_ord = int(input("Choose item to add: "))
                                            amount_ord = int(input("How many items do you want to add?: "))
                                        except ValueError:
                                            print("Invalid input, try agian!")
                                            break
                                        item_price = order_price[waiter_ord-1]
                                        total_order = amount_ord * item_price
                                        Totalprice[select_tbl-1] += total_order
                                        Totale_sale += total_order
                                        cafe_tbs.items = order_items[waiter_ord-1]
                                        table_items[select_tbl-1] = cafe_tbs.items
                                        cafe_tbs.quantity = amount_ord
                                        table_quantity[select_tbl-1] = cafe_tbs.quantity
                                        cafe_tbs.price = total_order
                                        table_price[select_tbl-1] = cafe_tbs.price
                                        add_order = input("Add another item? y/n: ").lower()
                                        if add_order == "n":
                                            break          
                                    if add_order == "n":
                                            break
                                else:
                                    print("Invalid input ,try again!")
                                    break

                        #When the waiter input 4 to prepare the bill.       
                        elif waiter_choice == "4":
                            item = "Item"
                            quantity = "Quantity"
                            price = "Price"
                            while True:
                                print("Please select a table:\n")
                                display_wtTB()
                                try:
                                    select_tbl = int(input("Please select a table or 0 to exit: "))
                                except ValueError:
                                    print("Invalid input ,try again!")
                                    break
                                if select_tbl == 0:
                                    break
                                elif select_tbl > 0 and select_tbl <= 6:
                                    if table_items[select_tbl-1] == "None":
                                        print("You need to order first, to be able to print the bill.")
                                        break
                                    else:
                                        print(f"--------------------------------------------------------------------\nThe bill for table {select_tbl}")
                                        print(f"{item:>20} {quantity:>20}\t\t{price:>10}")
                                        print(" ")
                                        for i in range(len(table_items[select_tbl-1])):
                                            print(f"{table_items[select_tbl-1][i]:>20} {table_quantity[select_tbl-1][i]:>20}\t\tR{table_price[select_tbl-1][i]:>9}")
                                            Bill_item.append(table_items[select_tbl-1][i])
                                            Bill_quantity.append(table_quantity[select_tbl-1][i])
                                            Bill_price.append(table_price[select_tbl-1][i])
                                        print(f"The total of your order was R {Totalprice[select_tbl-1]}\n\nYou were helped by {waiter_username}\n\n--------------------------------------------------------------------")
                                        table_bill[select_tbl-1] = "Bill"
                                        Main_bill.append(Bill_item)
                                        Main_bill.append(Bill_quantity)
                                        Main_bill.append(Bill_price)
                                        break
                                else:
                                    print("Invalid input ,try again!")
                                    break
                        
                        #When the waiter input 5 to complete the sale.
                        elif waiter_choice == "5":
                            while True:
                                print("Please select a table:\n")
                                display_wtTB()
                                try:
                                    select_tbl = int(input("Please select a table or 0 to exit: "))
                                except ValueError:
                                    print("Invalid input ,try again!")
                                    break
                                if select_tbl == 0:
                                        break
                                elif select_tbl > 0 and select_tbl <= 6:
                                    if table_bill[select_tbl-1] == "None":
                                        print("Please prepare bill before completing sale.")
                                        print(" ")
                                        break
                                    else:
                                        bill_file = input("Enter a filename: ") + ".txt"
                                        file = open(bill_file,'+w')
                                        file.write(str(Main_bill))
                                        file.close()
                                        print(" ")
                                        if waiter_username == "Sarah":
                                            table_index = TBkeys_Sarah.index(select_tbl)
                                            clear_table = waiter_Sarah.pop(table_index)
                                            clear_key = TBkeys_Sarah.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0

                                        elif waiter_username == "Thabang":
                                            table_index = TBkeys_Thabang.index(select_tbl)
                                            clear_table = waiter_Thabang.pop(table_index)
                                            clear_key = TBkeys_Thabang.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0

                                        elif waiter_username == "Lucy":
                                            table_index = TBkeys_Lucy.index(select_tbl)
                                            clear_table = waiter_Lucy.pop(table_index)
                                            clear_key = TBkeys_Lucy.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0

                                        elif waiter_username == "Pieter":
                                            table_index = TBkeys_Pieter.index(select_tbl)
                                            clear_table = waiter_Pieter.pop(table_index)
                                            clear_key = TBkeys_Pieter.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0

                                        elif waiter_username == "Motseki":
                                            table_index = TBkeys_Motseki.index(select_tbl)
                                            clear_table = waiter_Motseki.pop(table_index)
                                            clear_key = TBkeys_Motseki.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0
                                            
                                        elif waiter_username == "Sharon":
                                            table_index = TBkeys_Sharon.index(select_tbl)
                                            clear_table = waiter_Sharon.pop(table_index)
                                            clear_key = TBkeys_Sharon.pop(table_index)
                                            CafeTB_list[clear_key] = clear_table
                                            Totalprice[select_tbl-1] = 0
                                            table_bill[select_tbl-1] = "None"
                                            table_items[select_tbl-1] = "None"
                                            table_quantity[select_tbl-1] = 0
                                            table_price[select_tbl-1] = 0
                                    break
                                else:
                                    print("Invalid input ,try again!")
                                    break
                        
                        #When the waiter input 6 to cashup.
                        elif waiter_choice == "6":
                            print(f"Today we made R {Totale_sale}\n")
                            clear_total = input("Do you wish to clear the daily total? y/n: ").lower()
                            if clear_total == "y":
                                Totale_sale = 0

                        #When the waiter input 0 to logout.
                        elif waiter_choice == "0":
                            print(" ")
                            break
                        else:
                            print("Invalid input, try again!")
                    if waiter_choice == "0":
                        break
                elif valid == False:
                    break
        #When the waiter input 2 to exit the application.
        elif login_choice == "2":
            print("\033[33m" + "Good bye." + "\033[0m")
            break
        else:
            print("Invalid input, try again!")
            print(" ")
#Calling the main_Code function.          
main_code()
