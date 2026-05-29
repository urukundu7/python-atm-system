amount=4000
pin=3994
attempts=0
while attempts<3:
      user_pin=int(input("Enter your correct pin :"))
      if pin==user_pin:
            print("Welcome to SBI 🙏")
            break
      else:
            print("Wrong pin please try again ⚠️")
            attempts=attempts+1

else:
      print("ATM blocked due to 3 attempts are closed 😯") 
      exit()


while True:
      print("Please choose your option ❤️")
      print("1.Check balance")
      print("2.Deposite money")
      print("3.Withdraw money")
      print("4.Exit")

      choice=input("Enter your choice :")

      if choice=="1":
          print("Your amount is :",amount)

      elif choice=="2":
            balance=int(input("Enter amount to deposite :"))
            amount=amount+balance
            print("deposite successful your amount is :",amount)

      elif choice=="3":
            balance=int(input("Enter amount to withdraw money :"))

            if amount>=balance:
                amount=amount-balance
                print("wuthdraw successfull your amount is :",amount)
            else:
                 print("Insufficient money ⚠️")  
      elif choice=="4":
            print("Thank you for visiting 🙌") 
            exit()           

                   

