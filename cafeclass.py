#Creating a private class.
class cafe():
    def __init__(self):
        # Private varibales or properties.
        self.__customers = 0
        self.__orders = 0
        self.__items = []
        self.__quantity = []
        self.__price = []
        self.__bill = "None"

    #Getter method to get the property using an object.
    @property
    def customers(self):
        return self.__customers
    
    #Setter method to change the value shop_Name using an object. 
    @customers.setter
    def customers(self, amt_cst):
        self.__customers = amt_cst
    
    #Getter method to get the property using an object.
    @property
    def orders(self):
        return self.__orders
    
    #Setter method to change the value shop_Name using an object. 
    @orders.setter
    def orders(self, amt_ord):
        self.__orders = amt_ord
    
    #Getter method to get the property using an object.
    @property
    def tableNum(self):
        return self.__tableNum
    
    #Setter method to change the value shop_Name using an object. 
    @tableNum.setter
    def tableNum(self, table_Num):
        self.__tableNum = table_Num
        
    @property
    def items(self):
        return self.__items
    
    #Setter method to change the value shop_Name using an object. 
    @items.setter
    def items(self, ord_item):
            self.__items.append(ord_item)
    
    @property
    def quantity(self):
        return self.__quantity
    
    #Setter method to change the value shop_Name using an object. 
    @quantity.setter
    def quantity(self, ord_qt):
        self.__quantity.append(ord_qt)
    
    @property
    def price(self):
        return self.__price
    
    #Setter method to change the value shop_Name using an object. 
    @price.setter
    def price(self, ord_pr):
        self.__price.append(ord_pr)
    
    #Getter method to get the property using an object.
    @property
    def bill(self):
        return self.__bill
    
    #Setter method to change the value shop_Name using an object. 
    @bill.setter
    def bill(self, tbl_bill):
        if self.__bill == "None":
            self.__bill = "None"
        else:
            self.__bill = tbl_bill
            

    
    