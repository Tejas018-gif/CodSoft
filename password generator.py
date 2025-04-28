#to create a password generator
import random
print("Welcome to the password generator program.")
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['@','!','#','$','%','^','&','*','(',')']
length=int(input("Specify the length of the password: "))
l=int(input("Enter the no. of alphabets: "))
m=int(input("Enter the no. of numbers: "))
n=int(input("Enter the no. of symbols: "))
#print("Your length of the password is: ", l+m+n)
password=[]
if l+m+n==length:
    for i in range(1, l+1):
        char=random.choice(alpha)
        password+=char
    for i in range(1, m+1):
        char=random.choice(num)
        password+=char
    for i in range(1, n+1):
        char=random.choice(sym)
        password+=char
    random.shuffle(password)
#print(password)
    password_1=""
    for char in password:
        password_1+=char
    print("Your generated password is: ",password_1)    
else:
    print("Kindly check your input")
