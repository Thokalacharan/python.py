# palindrom
str=input("enter the string")
if str==str[::-1]:
    print(str,"palindrom")
else:
    print(str,"not palindrom")


# triangle is valid or not
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a+b>c and b+c>a and a+c>b:
    print("triangle is valid")
else:
    print("triangle is not valid")

a=int(input("enter the a"))
b=int(input("enter the b"))
  #arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
  #relation operators
print(a>b)
print(a>=b)
print(b>a)
print(b>=a)
print(a==b)
print(a!=b)

# speed and distance
d=int(input("distance in kilo"))
t=int(input("time in mins"))
s=d/t
print(s)


# second large element
def second_large(list):
    a=max(list)
    list.remove(a)
    print(max(list))
list=[1,23,4,56,]    
second_large(list)
    


# greatest of three numbers
a=int(input("enter the a"))
b=int(input("enter the b"))
c=int(input("enter the c"))
if a>b and a>c:
    print(a)
if b>c:
    print(b)
else:
    print(c)



# area and perimetre
l=float(input("enter a"))
b=float(input("enter b"))
a=l*b
b=2*(l+b)
print("area",a)
print("perimeter",b)



# even length word
n=input("enter the string").split()
for i in n:
    if len(i)%2==0:
        print(i)


# swap first and last element
list = [1,2,3,4]
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print(list)

# reverse the string
n=input("enter the string")
rev=" "
for i in n:
    rev =i+rev
print(rev)    

# logical operator and bitwise
a=int(input("enter the a"))
b=int(input("enter the b"))
print(a>b and b<a)
print(a>b or a<b)
print(not a)
print(a&b)
print(a/b)
print(~a)


# grade marks
a=int(input("enter the marks"))
if a>=90:
    print("grade a")
elif a>=80 and a<=90:
    print("grade b")
elif a>=70 and a<=80:
    print("grade c")
elif a>=60 and a<=70:
    print("garde d")
elif a>=50 and a<=50:
    print("grade e")
else:
    print("fail")

# gcd
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the valve"))
b=int(input("enter the value b"))
print(gcd(a,b))
