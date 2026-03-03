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


print("Now about numbers")
number=int(input("Write a number "))
sum=0
mult=1
while (number!=0):
    sum+=number%10
    mult*=number%10
    number//=10
print("sum:", sum, " mult: ", mult)


n=int(input("write n "))
for i in range(1,11):
    result=i*n
    print(f"{n}*{i}={result}")


print("Now let's play")
import random
num1=random.randint(1, 5)
attempts=0
guess=int(input())
while(guess!=num1):
    if (guess>num1):
        print("mine less")
    elif (guess<num1):
        print("mine greater")
    guess=int(input())
print("guessed number", num1)

def is_even( num):
    return n%2==0
num=int(input("Print number for even "))
if (is_even(num)):
    print(f"{num} is even")
else:
    print(f"{num} is uneven")
