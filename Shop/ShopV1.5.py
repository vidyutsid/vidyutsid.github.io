def addtocart(nameofitem, Quantityofitem, unitprice, stock, item):
                updateditemstock = stock - Quantityofitem;
                item.update({"Stock" : updateditemstock})
                cartitem = {"name" : nameofitem,"unitprice" : unitprice,"Quantity" : Quantityofitem}
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
def itemscanning(nameofitem, Quantityofitem, typeofproduct, item):
    item = "";
    for item in typeofproduct:
        if (item["name"] == nameofitem):
            if (item["Stock"] >= Quantityofitem):
                unitprice = item["unitprice"];
                stock = item["Stock"];
                addtocart(nameofitem, Quantityofitem, unitprice, stock, item)
            else:
                print("Out of stock!")
def shopping(catag):
    print("The list of items are:")
    for stuff in catag:
        list = "Name :", stuff["name"],"Unitprice :", stuff["unitprice"],"Stock :", stuff["Stock"];
        print(list)
    nameofitem = input("\nName of the item:")
    Quantityofitem = int(input("Quantity of the product:"))
    item = "";
    itemscanning(nameofitem, Quantityofitem, catag, item)
def list(whatcategory):
    print("The list of items are:")
    for stuffs in whatcategory:
        list = "Name :", stuffs["name"],"Unitprice :", stuffs["unitprice"],"Stock :", stuffs["Stock"];
        print(list)
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
            unitprice = 0;
            stock = 0;
            Quantityofitem = 0;
            nameofitem = "";
            print("Welcome to shopping, browse through the menu, and select which category of items you need")
            shoppingcategory = int(input("1.Smartphones\n2.Televisions\n3.Quit\n"))
            if (shoppingcategory == 1):
                catag = smartphones;
                shopping(catag)
            elif(shoppingcategory == 2):
                catag = Televisions
                shopping(catag)
            else:
                quitsale = True;
    elif (pick == 2):
        catag = "";
        print("Your shopping cart is:\n", Shoppingcart)
        editshoppingcart = input("If you'd like to add an item to your shopping cart enter 'Add', if you want to remove an item, enter 'Remove', for billing press any key, and enter\n")
        if (editshoppingcart == "Add"):
            print("category not available at the moment due to reliability issues, sorry for the inconvenience")
            category = input("What category does this item belong to? [smartphones/Televisions]")
            if (category == "smartphones"):
                catag = smartphones;
                shopping(catag)
            elif (category == "Television"):
                catag = Televisions;
                shopping()
            else:
                print("Catergory does not exist, please try again")
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
            elif (payment == "N"):
                print("Payment cancelled")
                quit()
            else:
                print("Error, wrong key, no condintion has been satisfied")
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
                    whatcategory = smartphones
                elif (whatcategory == "Televisions"):
                    whatcategory = Televisions
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
                list(whatcategory)
                stockitemname = input("name of item:")
                stockupdate = int(input("updated stock of item(+/-):"))
                for prod in whatcategory:
                    if (prod["name"] == stockitemname):
                        updatestock = prod["Stock"] + stockupdate;
                        prod.update({"Stock" : updatestock})
        else:
            print("Wrong password!")
    else:
        closemainmenu = True;
