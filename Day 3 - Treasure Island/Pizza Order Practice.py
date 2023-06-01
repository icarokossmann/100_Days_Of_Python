# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == 'S':
    bill = 15
    print("Small Pizza: $15.")

elif size == 'M':
    bill = 20
    print("Medium Pizza: $20.")

elif size == 'L':
    bill = 25
    print("Large Pizza: $25")

if add_pepperoni == 'Y':
   if size == 'S':
       print("Pepperoni for Small Pizza: +$2.")
       bill += 2
   else:
       print("Pepperoni for Medium or Large Pizza :+$3")
       bill += 3

if extra_cheese == 'Y':
    bill += 1
    print("Extra cheese for any size pizza: +1.")

print(f"Your final bill is: ${bill}.")