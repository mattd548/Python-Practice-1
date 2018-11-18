#exercise 1
print("******************************")
print("\tWelcome!")
print("Please choose a number from the following options")
print("1\tPlay the game!")
print("2\tDemo the game!")
print("3\tExit")
print("******************************")

#exercise 2
num1=578
num2=986
num3=1066
num4=714
sum=num1+num2+num3+num4
print("\n\nthe sum of these numbers is",sum)
average=sum/4
print("the sum of these numbers is",average)


#exercise 3
#input function takes only strings
n1=input("\nEnter the first number ")
n2=input("Enter the second number:")
n3=input("Enter the third number:")
n4=input("Enter the fourth number:")
sum=int(n1)+int(n2)+int(n3)+int(n4)
print("the sum of these numbers is:",sum)
average=sum/4
print("the average of these numbers are:",average)

#exercise 4
stocks=input("\nEnter the number of shares purchased: ")
stockprice=input("Enter price of shares when purchased: ")
stockprice_now=input("Enter the stock's price now: ")
Profit = (float(stocks) * float(stockprice_now)) - (float(stocks) * float(stockprice))
print("you have made a profit of $ {0:06.2f}".format(Profit)," since you bought",stocks," shares of this stock")


#exercise 5
