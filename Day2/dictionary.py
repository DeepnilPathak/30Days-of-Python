dict1={}
ans='y'
while(ans=='y' or ans=='Y'):
    name=input("Enter your name: ")
    dict1[name]=int(input("Enter your marks: "))
    ans=input("Do you want to continue?(Y/N) ")
ansb= input("Do you want to look at your score?(Y/N) ")
if (ansb=='y' or ansb=='Y'):
    name=input("Enter your name: ")
    print("Your marks is ",dict1[name])