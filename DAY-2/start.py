print("Hello, World!")
print("This is DAY-2 start.py file.")
#Data types in Python
print()
print("Data types in Python:")
price=40
print("Integer:", price)
print("Data type of price:", type(price))
rating=4.5
print("Float:", rating)
print("Data type of rating:", type(rating))
item="Fried rice"
print("String:", item)
print("Data type of item:", type(item))
is_rating=True
print("Boolean:", is_rating)
print("Data type of is_rating:", type(is_rating))
menu=["Fried rice", "Noodles", "idli", "Dosa"]
print("List:", menu)
print("Data type of menu:", type(menu))
print(menu[0])
print("Appending Biryani to the list:")
menu.append("Biryani")
print(menu)
print("Removing Dosa from the list:")
menu.remove("Dosa")
print(menu)
print("Slicing the list from index 1 to 3:")
print(menu[1:3])
working_days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("Tuple:", working_days)
print("Data type of working_days:", type(working_days))
cost={"Fried rice": 40, "Noodles": 50, "idli": 30, "Dosa": 60}
print("Dictionary:", cost)
print("Data type of cost:", type(cost))
print("Cost of Noodles:", cost["Noodles"])
print("Adding Biryani to the dictionary with cost 80:")
cost["Biryani"] = 80
print(cost)
print("Removing Dosa from the dictionary:")
del cost["Dosa"]
print(cost)