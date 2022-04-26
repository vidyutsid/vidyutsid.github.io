def addtocart(nameofphone, Quantityofphone, unitprice, stock):
                total = 0;
                updateditemstock = stock - quantityofitem;
                item.update({"Stock" : updateditemstock})
                cartitem = {"name" : nameofitem,"unitprice" : unitprice,"Quantity" : quantityofitem}
                Shoppingcart.append(cartitem)
                cont = input("Do you want to contunue shopping?[Y/N]")
                if (cont == "N"):
                    print("Go to cart in the main menu to complete overall billing")
def decipher(cipheredtext,shift):
    result = ""
    for thing in range(len(cipheredtext)):
        character = cipheredtext[thing];
        variable = chr(ord(character) - shift);
        for c in variable:
            result += c;
    return result
item1 = {
    "name" : "iphone 13",
    "unitprice" : 69999,
    "Stock" : 20
}
item2 = {
    "name" : "Mi 4i",
    "unitprice" : 2300,
    "Stock" : 20
}
smartphones = [item1,item2]
item3 = {
    "name" : "Samsung",
    "unitprice" : 41000,
    "Stock" : 20
}
item4 = {
    "name" : "LG",
    "unitprice" : 60000,
    "Stock" : 49
}
Televisions = [item3,item4]
Shoppingcart = []
catagory = [smartphones, Televisions]
closemainmenu = False;
while (closemainmenu == False):
    pick = int(input("Main menu:\n1.Shopping\n2.Cart\n3.Management\n4.Quit\n"))
    if (pick == 1):
        quitsale = False;
        while (quitsale == False):
            print("Welcome to shopping, browse through the menu, and select which category of items you need")
            shoppingcategory = int(input("1.Smartphones\n2.Televisions\n3.Quit\n"))
            if (shoppingcategory == 1):
                print("The list of smartphones are:")
                for x in smartphones:
                    list = "Name :", x["name"],"Unitprice :", x["unitprice"],"Stock :", x["Stock"];
                    print(list)
                    Quantityofphone = int(input("Quantity of the item:"))
                nameofphone = input("\nName of the smartphone:");
                for item in smartphones:
                    if (item["name"] == nameofphone):
                        if (item["Stock"] >= Quantityofphone):
                            unitprice = item["unitprice"];
                            Stock = item["Stock"];
                            phonecartadd(nameofphone, Quantityofphone, unitprice, Stock)
            elif(shoppingcategory == 2):
                print("The list of televisions are:")
                for stuff in Televisions:
                    list = "Name :", stuff["name"],"Unitprice :", stuff["unitprice"],"Stock :", stuff["Stock"];
                    print(list)
                nameoftv = input("\nName of television:")
                Quantityoftv = int(input("Quantity of the product:"))
                for tv in Televisions:
                    if (tv["name"] == nameoftv):
                        if (tv["Stock"] >= Quantityoftv):

                            addtocart
                        else:
                            print("Out of stock!")
            else:
                quitsale = True;
    elif (pick == 2):
        print("Your shopping cart is:\n", Shoppingcart)
        editshoppingcart = input("If you'd like to add an item to your shopping cart enter 'Add', if you want to remove an item, enter 'Remove', for billing press any key, and enter")
        if (editshoppingcart == "Add"):
            category = input("What category does this item belong to?")
            if (category == "Phone"):
                print("The list of smartphones are:")
                for x in smartphones:
                    list = "Name :", x["name"],"Unitprice :", x["unitprice"];
                    print(list)
                nameofphone = input("\nName of the smartphone:");
                Quantityofphone = int(input("Quantity of the item:"))
                for item in smartphones:
                    if (item["name"] == nameofphone):
                        if (item["Stock"] >= Quantityofphone):
                            unitprice = item["unitprice"];
                            Stock = item["Stock"];
                            phonecartadd(nameofphone, Quantityofphone, unitprice, Stock)
                        else:
                            print("Out of stock!")
            if (category == "Television"):
                print("The list of televisions are:")
                for stuff in Televisions:
                    list = "Name :", stuff["name"],"Unitprice :", stuff["unitprice"]
                    print(list)
                nameoftv = input("\nName of television:")
                Quantityoftv = int(input("Quantity of the product:"))
                for tv in Televisions:
                    if (tv["name"] == nameoftv):
                        if (tv["Stock"] >= Quantityoftv):
                            tvstock = tv["Stock"];
                            tvUnitprice = tv["unitprice"]
                            tvcartadd(nameoftv, Quantityoftv, tvUnitprice, tvstock, closemainmenu)
                        else:
                            print("Out of stock!")
        elif (editshoppingcart == "Remove"):
            itemname = input("What is the name of the item you want to remove?")
            for v in Shoppingcart:
                if (v["name"] == itemname):
                    Shoppingcart.remove(v);
                    print("Item has been removed")
                    print(Shoppingcart)
        else:
            total = 0;
            for n in Shoppingcart:
                total += n["unitprice"] * n["Quantity"];
            print("Your shopping cart is:", Shoppingcart)
            print("Total =", total)
            payment = input("Pay?[Y/N]")
            if (payment == "Y"):
                print("Thank you for purchasing, hope to see you again!")
                quit()
            else:
                print("Payment cancelled")
                quit()
    elif(pick == 3):
        print("Welcome to the management section, to continue please enter the pasword to access this section")
        print("Hint: Shift = 4, PASSSORD")
        cipheredtext = input("Enter password here:")
        shift = 4;
        cipher = decipher(cipheredtext, shift);
        if (cipher == "PASSSORD"):
            print("Welcome to the management section!")
            print("1.Add item\n2.Remove an item\n3.Update stock\n4.Quit")
            managementchoice = int(input("Input your choice:"))
            if (managementchoice == 1):
                print("Welcome to add item, here you have to select which category you want to add an item to, and then input the item's details")
                whatcategory = input("What category does it belong to? [smartphones/Televisions]?")
                if (whatcategory == "smartphones"):
                    whatcategory = smartphones;
                elif (whatcategory == "Televisions"):
                    whatcategory = Televisions;
                whatname = input("What is to name of this item supposed to be?")
                whatunitprice = int(input("What is the unit price of this item?"))
                whatstock = int(input("What is the current stock of this item?"))
                newitem = {"name" : whatname,"unitprice" : whatunitprice,"Stock" : whatstock};
                whatcategory.append(newitem)
            elif (managementchoice == 2):
                print("Welcome to remove item, here you have to input the catgory the item belongs to, and the name of item that has to be removed")
                whatcategory = input("What category does the item belong to? [smartphones/Televisions]?")
                itemid = input("What is the name of the item you wish to remove?")
                if (whatcategory == "smartphones"):
                    whatcategory = smartphones;
                elif (whatcategory == "Televisions"):
                    whatcategory = Televisions;
                for product in whatcategory:
                    if (product["name"] == itemid):
                        whatcategory.remove(product)
                    else:
                        print("That item does not exist!")
            elif (managementchoice == 3):
                print("Welcome to update stock, here you have to input the category of the item, the name of the item, and the updates stock of that item")
                whatcategory = input("What catgory does the item belong to?[smartphones/Televisions]")
                if (whatcategory == "smartphones"):
                    whatcategory = smartphones;
                elif (whatcategory == "Televisions"):
                    whatcategory = Televisions;
                stockitemname = input("What is the name of the item?")
                stockupdate = int(input("What is the updated stock(+/-)"))
                for prod in whatcategory:
                    if (prod["name"] == stockitemname):
                        updatestock = prod["Stock"] + stockupdate;
                        prod.update({"Stock" : updatestock})
        else:
            print("Wrong password!")
    else:
        closemainmenu = True;
