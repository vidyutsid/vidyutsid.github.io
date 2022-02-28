import os
item1 = {
  "name": "Rice",
  "unitprice": 100,
  "stock": 100
}

item2 = {
  "name": "Bannana",
  "unitprice": 30,
  "stock": 20
}

x = item1.get("unitprice")

# print(x)

catalog = [item1, item2]
# print(catalog)

quitmainmenu = False;
while (quitmainmenu == False):
  choice = input("Menu::\n1. Sale\n2. Manage Catalog\n3. Quit\nEnter Choice(1/2/3)::")
  if (choice == "1"):
    quitesale = False;
    total = 0;
    while (quitesale == False):
      name = input("Name of item:")
      quantity = int(input("Quantity:"))
      for item in catalog:
        if (item["name"] == name):
          if (item["stock"] >= quantity):
            total += quantity * item["unitprice"]
            item["stock"] = item["stock"] - quantity
          else:
            print("No Stock!")
          moreitems = input("More Items(Y/N)")
      if (moreitems == "N"):
        print("Bill Amount:", total)
        quitesale = True
  elif (choice == "2"):
    quitcatalog = False
    while (quitcatalog == False):
      catalogchoice = input("Manage Catalog::\n1. Add Item\n2. Remove Item\n3. Update Stock \n4. View Stock\n5. Quit:\nEnter Choice(1/2/3/4/5)::")
      if (catalogchoice == "1"):
        print("In Add Item")
        name = input("Item Name:")
        unitprice = int(input("Unit Price(Rs):"))
        stock = int(input("Quantity(Kg):"))
        item = {"name" : name, "unitprice" : unitprice, "stock": stock}
        catalog.append(item)
        print(catalog)
      elif (catalogchoice == "2"):
        print("In Remove Item")
        name = input("Item Name:")
        for item in catalog:
          if (item["name"] == name):
            catalog.remove(item)
        print(catalog)
      elif (catalogchoice == "3"):
      	print("In Restock Item")
      	name = input("Item name:")
      	quantity = int(input("(+/-) Stock:"))
      	for item in catalog:
      	  if (item["name"] == name):
      	    currentstock = item.get("stock")
      	    updatedstock = currentstock + quantity;     	    
      	    item.update({"stock" : updatedstock})
      	print(catalog)
      elif (catalogchoice == "4"):
        print("[ItemName]", "[Qty]")
        for i in range(len(catalog)):
          print(catalog[i]["name"], catalog[i]["stock"])
      else:
        quitcatalog = True
  else:
    quitmainmenu = True

    

