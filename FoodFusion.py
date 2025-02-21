
import time 
class FoodFusion():
    food_list ={1:"Cake",2:"Pizza",3:"Chinese",4:"Burgers",5:"Italian",6:"South Indian"}

    cake_list={1:"Vanilla Cake",2:"Black Forest Cake",3:"Chocolate Cake",4:"Fruit Cake",5:"Rainbow Cake",6:"Red Velvet Cake"}
    pizza_list={1:"Tandoori Panner",2:"Classic Onion Capsicum",3:"Cheese Spicy Delight",4:"Veggie Feast",5:"Bold BBQ Veggies",6:"Awesome American Cheesy"}
    chinese_list={1:"Veg Manchow Soup",2:"Peri Peri Momo Platter",3:"Spring Roll",4:"Schezwan Rice",5:"Schezwan Noodles",6:"Hakka Noodles"}
    burger_list={1:"Crisp Veg Burger",2:"Mexican Burger",3:"Corn & Cheese Burger",4:"Double Patty Burger",5:"NONG Burger",6:"Spicy Paneer Burger"}
    italian_list={1:"Risotto",2:"Gnocchi",3:"Bruschetta",4:"Parmesian Pasta",5:"Spagetti",6:"Carbonara"}
    southindian_list={1:"Plain Dosa",2:"Masala Dosa",3:"Butter Idli",4:"Curd Rice",5:"Medu Vada",6:"Payasam"}
    quantity=0
    price=0
    foodie={}
    individual_price={}
    mode_app=''
    
class Food_Selection(FoodFusion):
    @classmethod
    def selecting_food(cls):
        
        print(" "*30,"************************************************\n")
        print(" "*30,"             WELCOME TO FOODIE!!!!!            \n")
        print(" "*30,"************************************************\n")
        print("\t\tFoodFusion application provides the users with varieties of delicious foods to order\n\tand brings various food delivery applications at one platform, giving users the opportunity to compare \n\t\t   and select the best option for the delivery out of all the others!!")
        while True:
            for i in cls.food_list:
                print(i,"-->",cls.food_list[i])
            ask_user=input("Do you want to order any food item? (y for Yes/n for No): ")
            if ask_user=="y":
                user_choice=int(input("Enter the number regarding the food items you want to eat:"))
                if user_choice==1:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.cake_list:
                        print(i,"-->",cls.cake_list[i])
                    cake_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_cake=cls.cake_list[cake_selection]
                    print(f"\nYou have selected {user_cake}\n")
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_cake]=ask_quantity
                elif user_choice==2:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.pizza_list:
                        print(i,"-->",cls.pizza_list[i])
                    pizza_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_pizza=cls.pizza_list[pizza_selection]
                    print(f"\nYou have selected {user_pizza}\n")
                    # while True:
                    #     ask_sides=input("Do you want any sides along with your pizza? (y/n): ")
                    #     if ask_sides=="y":
                    #         sides_list={1:"Coke (500ml) & Garlic Bread Sticks (5Pcs)",2:"Diet Coke (500ml) & Garlic Bread Sticks (5 Pcs)",3:"Garlic Bread Sticks (5 Pcs)",4:"Macronni Pasta",5:"Chocolate Lava",6:"Brownie"}
                    #         for i in sides_list:
                    #             print(i,"--> ",sides_list[i])
                    #         sides_selection=int(input(f"Enter the number in respect to the side items displayed:"))
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_pizza]=ask_quantity
                elif user_choice==3:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.chinese_list:
                        print(i,"-->",cls.chinese_list[i])
                    chinese_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_chinese=cls.chinese_list[chinese_selection]
                    print(f"\nYou have selected {user_chinese}\n")
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_chinese]=ask_quantity
                elif user_choice==4:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.burger_list:
                        print(i,"-->",cls.burger_list[i])
                    burger_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_burger=cls.burger_list[burger_selection]
                    print(f"\nYou have selected {user_burger}\n")
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_burger]=ask_quantity
                elif user_choice==5:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.italian_list:
                        print(i,"-->",cls.italian_list[i])
                    italian_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_italian=cls.italian_list[italian_selection]
                    print(f"\nYou have selected {user_italian}\n")
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_italian]=ask_quantity
                elif user_choice==6:
                    print(f"You have selected the food item {cls.food_list[user_choice]}!\nBelow are the varieties of {cls.food_list[user_choice]} available:\n")
                    for i in cls.southindian_list:
                        print(i,"-->",cls.southindian_list[i])
                    southindian_selection=int(input(f"Enter the number in respect to the {cls.food_list[user_choice]} items displayed:"))
                    user_southindian=cls.southindian_list[southindian_selection]
                    print(f"\nYou have selected {user_southindian}\n")
                    ask_quantity=int(input("Enter the quantity of the food items in numbers:"))
                    cls.quantity+=ask_quantity
                    cls.foodie[user_southindian]=ask_quantity
                elif user_choice not in [1,2,3,4,5,6]:
                    print("Invalid USER CHOICE. Try again!!!!")
            elif ask_user not in ["y","n"]:
                print("Invalid input. Try again!!!!!")
            elif ask_user=="n":
                if cls.quantity>0:
                    for i in cls.foodie:
                        print(i,"---->",cls.foodie[i])
                break
class Delivery_Selection(Food_Selection):
    def __init__(self):
        self.cake={"Vanilla Cake":[200,300,250],"Black Forest Cake":[300,350,400],"Chocolate Cake":[400,350,300],"Fruit Cake":[320,300,350],"Rainbow Cake":[340,400,500],"Red Velvet Cake":[400,500,600]}
        self.pizza={"Tandoori Panner":[299,340,330],"Classic Onion Capsicum":[190,179,210],"Cheese Spicy Delight":[309,290,300],"Veggie Feast":[420,389,402],"Bold BBQ Veggies":[425,450,430],"Awesome American Cheesy":[430,450,445]}
        self.chinese={"Veg Manchow Soup":[130,129,135],"Peri Peri Momo Platter":[100,90,112],"Spring Roll":[100,102,98],"Schezwan Rice":[120,127,118],"Schezwan Noodles":[135,130,139],"Hakka Noodles":[130,140,132]}
        self.burger={"Crisp Veg Burger":[90,88,78],"Mexican Burger":[45,40,34],"Corn & Cheese Burger":[109,110,109],"Double Patty Burger":[122,123,133],"NONG Burger":[98,89,91],"Spicy Paneer Burger":[101,100,102]}
        self.italian={"Risotto":[200,220,230],"Gnocchi":[345,350,340],"Bruschetta":[449,440,430],"Parmesian Pasta":[630,640,625],"Spagetti":[330,340,334],"Carbonara":[649,639,644]}
        self.southindian={"Plain Dosa":[40,43,35],"Masala Dosa":[50,55,45],"Butter Idli":[35,30,32],"Curd Rice":[40,35,30],"Medu Vada":[40,35,30],"Payasam":[30,35,36]}
        self.zomato={}
        self.swiggy={}
        self.ondc={}
    
    def del_app(self):
        for i in Food_Selection.foodie:
            if i in self.burger:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.burger[i][0],"\n"," "*10,"Swiggy==>   ",self.burger[i][1],"\n"," "*10,"ONDC==>   ",self.burger[i][2])
                self.zomato[i]=self.burger[i][0]
                self.swiggy[i]=self.burger[i][1]
                self.ondc[i]=self.burger[i][2]
            elif i in self.cake:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.cake[i][0],"\n"," "*10,"Swiggy==>   ",self.cake[i][1],"\n"," "*10,"ONDC==>   ",self.cake[i][2])
                self.zomato[i]=self.cake[i][0]
                self.swiggy[i]=self.cake[i][1]
                self.ondc[i]=self.cake[i][2]
            elif i in self.pizza:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.pizza[i][0],"\n"," "*10,"Swiggy==>   ",self.pizza[i][1],"\n"," "*10,"ONDC==>   ",self.pizza[i][2])
                self.zomato[i]=self.pizza[i][0]
                self.swiggy[i]=self.pizza[i][1]
                self.ondc[i]=self.pizza[i][2]
            elif i in self.chinese:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.chinese[i][0],"\n"," "*10,"Swiggy==>   ",self.chinese[i][1],"\n"," "*10,"ONDC==>   ",self.chinese[i][2])
                self.zomato[i]=self.chinese[i][0]
                self.swiggy[i]=self.chinese[i][1]
                self.ondc[i]=self.chinese[i][2]
            elif i in self.italian:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.italian[i][0],"\n"," "*10,"Swiggy==>   ",self.italian[i][1],"\n"," "*10,"ONDC==>   ",self.italian[i][2])
                self.zomato[i]=self.italian[i][0]
                self.swiggy[i]=self.italian[i][1]
                self.ondc[i]=self.italian[i][2]
            elif i in self.southindian:
                print(i,"----------------->","\n"," "*10,"Zomato==>   ",self.southindian[i][0],"\n"," "*10,"Swiggy==>   ",self.southindian[i][1],"\n"," "*10,"ONDC==>   ",self.southindian[i][2])
                self.zomato[i]=self.southindian[i][0]
                self.swiggy[i]=self.southindian[i][1]
                self.ondc[i]=self.southindian[i][2]
        select_deliv=int(input("Enter the choice of delivery app accordingly in number:\n1. Zomato\n2. Swiggy\n3. ONDC\nYour option--> "))
        if select_deliv==1:
            print("\nYou have selected ZOMATO as your food delivery option!!") 
            for i in self.zomato:
                Food_Selection.individual_price[i]=self.zomato[i]
                Food_Selection.price+=self.zomato[i]*Food_Selection.foodie[i]
            print(f"Your total including the delivery charge is: {Food_Selection.price}")
        elif select_deliv==2:
            print("\nYou have selected SWIGGY as your food delivery option!!") 
            for i in self.swiggy:
                Food_Selection.individual_price[i]=self.swiggy[i]
                Food_Selection.price+=self.swiggy[i]*Food_Selection.foodie[i]
            print(f"Your total including the delivery charge is: {Food_Selection.price}")
        elif select_deliv==3:
            print("\nYou have selected ONDC as your food delivery option!!") 
            for i in self.ondc:
                Food_Selection.individual_price[i]=self.ondc[i]
                Food_Selection.price+=self.ondc[i]*Food_Selection.foodie[i]
            print(f"Your total including the delivery charge is: {Food_Selection.price}")
    @staticmethod
    def login():
        print("To futher your bill & payment please login first.\n")
        i=1
        while i>0:
            username=input("Enter your password:")
            if 'A'<=username<='Z' or 'a'<=username<='z' or '0'<=username<='9':
                print("Username is proper!")
                break
            else:
                if i==3:
                    print("You have exceeded the attempts of typing proper username")
                    print("Wait for 5 seconds to try again")
                    time.sleep(5)
            i+=1
        while i>0:
            phno=input("Enter phone number:")
            if '0'<=phno<='9' and len(phno)==10:
                print("Phone number is proper!")
                break
            else:
                if i==3:
                    print("You have exceeded the attempts of typing proper phone number")
                    print("Wait for 5 seconds to try again")
                    time.sleep(5)
            i+=1
        while i>0:
            location=input("Enter location for delivery:")
            if 'A'<=location<='Z' or 'a'<=location<='z':
                print("Location is added!")
                break
            else:
                if i==3:
                    print("You have exceeded the attempts of typing proper location")
                    print("Wait for 5 seconds to try again")
                    time.sleep(5)
            i+=1
        print(" "*20,"***Your Login Details***")
        print(" "*21,"Username:",username,"\n"," "*20,"Phone No.:",phno,"\n"," "*20,"Location:",location)
    @classmethod
    def mode():
        payment={1:"UPI",2:"COD"}
        print("Mode of payment:\n1.UPI\n2.Cash on Delivery\n")
        i=0
        while i>0:
            m=int(input("Choose your mode of payment:"))
            if m==1:
                print("You have chosen UPI as your mode of payment")
                break
            elif m==2:
                print("You have chosen UPI as your mode of payment")
                break
            else:
                if i==2:
                    print("No other mode of payment available")
                    print("Try again in 5 seconds")
                    time.sleep(5)
            i+=1
        Food_Selection.mode_app=payment[m]
    def bill(self):
        gst=5/100*Food_Selection.price
        tax=18/100*Food_Selection.price
        print("\n")
        print(" "*20,"*"*35,"BILL","*"*35)
        for i in Food_Selection.foodie:
            print(" "*30,i,"-"*2,"Quantity","-"*2,">",Food_Selection.foodie[i],"-"*10,">",Food_Selection.individual_price[i]*Food_Selection.foodie[i])
        print(" "*20,"-"*76)
        print(" "*30,"Total","-"*40,">",Food_Selection.price)
        print(" "*30,"gst","-"*40,">",gst)
        print(" "*30,"tax","-"*40,">",tax)
        print(" "*30,"Net Amt","-"*40,">",Food_Selection.price+gst+tax)
        print(" "*30,"Payment mode","-"*35,">",Food_Selection.mode_app)
        print(" "*20,"-"*76)
        print("~"*110)
        print(" "*30,"Your delivery partner is Ramesh")
        print(" "*30,"Your food will be delivered in 20 minutes")
        print("~"*110)
        print("~"*110)
        print(" "*30,"THANK YOU FOR ORDERING FROM FoodFusion!!!!!") 
        print(" "*30,"ENJOY YOUR MEAL!!!!!")  
        print(" "*30,"PLEASE VISIT US AGAIN!!!!")          
        print("~"*110) 
                       
f=Delivery_Selection()
f.selecting_food()
f.del_app()
f.login()
f.mode()
f.bill()
