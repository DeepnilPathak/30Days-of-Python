Name=input("Enter your name: ")
Age=int(input("Enter your age: "))
email=input("Enter your email: ")
money=1000
ans='y'
while(ans=='y' or ans=='Y'):
    amount=float(input("Enter the amount you want to deposit: "))
    money=money+amount
    print("Please wait while your transaction is being processed.........")
    ans=input("Do you still continue?(y/n): ")
print("Your available balance is: ",money)
    