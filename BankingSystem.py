# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GW27sRjkx37t4Zs6OUvLeaA8fTEh8nam
"""

deposit=0
inBalance=0
withdraw=0
flag=0
def menu():
  print("WELCOME TO TIMES BANK")
  print("*************************************")
  print(" 1. Open a new bank account ")
  print(" 2. Withdraw Money ")
  print(" 3. Deposit Money ")
  print(" 4. Check Customers & Balance ")
  print(" 5. Exit/Quit ")

menu()

while True:
  x = int(input("Enter your choice: "))
  #balance = (inBalance + deposit) - withdraw

  if x == 1:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    pNumber = input("Enter your phone number: ")
    inBalance = int(input("How much money do you want to deposit as the starting deposit?"))
    flag=1;
    account = print("Your bank account is created with a balance of $", inBalance )
    
  elif x == 2:
    if (flag==1):
      withdraw=int(input("How much money edo you want to withdraw "))
      print("Successfully Withdrawn $", withdraw)
    else:
      print("Create an account first")

  elif x == 3:
    if (flag==1):
      deposit = int(input("How much money do you want to deposit?"))
      print("Successfully Deposited $",deposit)
    else:
      print("Create an account first")

  elif x == 4:
    if (flag==1):
      print("Your current balance is $", balance)
    else:
      print("Create an account first")
    

  elif x == 5:
    break

  else:
    print("Invalid input")

file = open("/content/bank.txt", "w")
file.write("Your name is: " + name + '\n')
file.write("Your age is: " + str(age) + '\n')
file.write("Your Phone Number is: " + str(pNumber) + '\n')
file.write(str(balance))

file.close()

