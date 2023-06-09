#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the Tip Calculator!")

bill = float (input ("What was the total bill? $"))

tip = int (input ("How much tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

bill_with_tip = bill * (1 + tip / 100)

bill_per_person = bill_with_tip/people

#final_amount = round (bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print (f"Each person should pay ${final_amount}")


#Primeira versao do codigo, abaixo. O resultado obtido foi aproximado do desejado,
#a exibição ficou diferente e não houve sucesso na exibição do falor final com duas casas decimais

# print ("Welcome to the tip calculator.")
#
# print (f"What was the total bill?")
#
# bill = input()
#
#
# print ("What the percentage tip would you like to give? 10, 12, or 15?")
# tip_percent = input()
#
#
#
# tip = ((( float (tip_percent) / 100)) + 1)
#
# full_bill = tip * float (bill)
#
#
# print ("How many people to split the bill?")
#
# people = input()
#
# total = full_bill / float (people)
#
# print (f"Each person should pay: ${round (total, 2)}")