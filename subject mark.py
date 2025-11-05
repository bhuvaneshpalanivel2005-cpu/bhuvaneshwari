print("five subject marks")
a=int(input("tamil mark:"))
b=int(input("english mark:"))
c=int(input("maths mark:"))
d=int(input("science mark:"))
e=int(input("social:"))
f=(a+b+c+d+e)
print(f)
if(f>450):
    print("excellent student")
elif(f>350):
    print("good student")
elif(f>250):
    print("average student")
else:
    print("poor student")
