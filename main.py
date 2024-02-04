print("Welcome to Take a Bite Pizza")
print("What would you like to have today?")
print("We have two options for the day,'CheeseBurstPizza','BasilThaiPizza'")
pizza = input("Enter your choice: ")
size_pizza = input("Enter the size of the pizza:'Small','Medium','Large':  ")
bill = 0
if pizza == "CheeseBurstPizza":
  print("You have ordered a CheeseBurstPizza")
  if size_pizza == "Small":
    bill += 120
  elif size_pizza =="Medium":
    bill += 150
  elif  size_pizza =="Large":
    bill +=170
  
elif pizza == "BasilThaiPizza":
  print("You have ordered a BasilThaiPizza")
  if size_pizza == "Small":
    bill += 140
  elif size_pizza =="Medium":
    bill += 190
  elif  size_pizza =="Large":
    bill +=210

else:
  print("Please choose the correct option")
print("Would you like to have some Cold Drink with your pizza?")
cold_drink = input("Enter 'Yes' or 'No': ")
if cold_drink == "Yes":
  print("We have two options for the day,'Coke','Sprite'")
  drink = input("Enter your choice: ")
  if drink == "Coke":
    bill +=35
  elif drink == "Sprite":
    bill+=42

print(f"Your total bill is {bill}Rs")

print("Give our service a proper rating")
print("If you rate us '5 star',we will give you a free drink")
rating =input("Enter your Rating: ")
if rating == "5 star":
  print("You have got a free drink")
  free_drink = input("Enter your choice: ")
  print(f"Here is your {free_drink}")
  
print(f"Your total bill is {bill}Rs")
print(f"Thank you for your order,Enjoy the {pizza} with your {cold_drink}") 
print("Thank you please visit again")



