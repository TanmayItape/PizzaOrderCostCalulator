print("Welcome to Take a Bite Pizza")
print("What would you like to have today?")
print("We have two options for the day,'CheeseBurstPizza','BasilThaiPizza'")
pizza = input("Enter your choice: ")
bill = 0
if pizza == "CheeseBurstPizza":
  print("You have ordered a CheeseBurstPizza")
  bill+=8
elif pizza == "BasilThaiPizza":
  print("You have ordered a BasilThaiPizza")
  bill+=10
else:
  print("Please choose the correct option")
print("Would you like to have some Cold Drink with your pizza?")
print("We have two options for the day,'Coke','Sprite'")
drink = input("Enter your choice: ")
if drink == "Coke":
  bill +=3
elif drink == "Sprite":
  bill+=4


print("Give our service a proper rating")
print("If you rate us '5 star',we will give you a free drink")
rating =input("Enter your Rating: ")
if rating == "5 star":
  print("You have got a free drink")
  free_drink = input("Enter your choice: ")
  print(f"Here is your {free_drink}")
  
print(f"Your total bill is {bill}$")
print(f"Thank you for your order,Enjoy the {pizza} with your {drink}") 
print("Thank you please visit again")



