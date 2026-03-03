name = input("Enter your name ")
age = int(input("Enter your age "))
print("Hello ", name, "! In 5 years you will be ", age + 5)
print("Now about money")
price=float(input("What is the price?"))
paid=float(input("Which sum have you paid?"))
if (paid>price):
    print("Your return ", paid-price)
elif (price>paid):
    print("Not enough money")
else: print("Thank u")