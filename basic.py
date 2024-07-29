# write a program to convert fahrenheit to celsius
f=float(input("enter the fahrenheit"))
c=(f-32)*5/9
print(" the celsius",c)
output:
enter the fahrenheit98
 the celsius 36.666666666666664

# write a program to find simple interest
p=float(input("enter the P value",))
t=float(input("enter the T value"))
r=float(input("enter the R value"))
SI=(p*t*r)/100
print(SI)

output:
enter the P value123
enter the T value20
enter the R value10
246.0

# write a program to find area and perimeter of rectangle
l=float(input("enter l"))
b=float(input("enter b"))
a=l*b
b=2*(l+b)
print("area",a)
print("perimeter",b)

output:

enter l3
enter b4
area 12.0
perimeter 14.0

# write a program to find area and circumference of a circle
r=float(input("enter radius"))
a=r*r*3.14
c=2*3.14*r
print(a)
print(c)

output:
enter radius5
78.5
31.400000000000002

# write a program to find the speed of a vehicle
d=float(input("enter the distance in kms"))
t=float(input("enter the time min"))
s=d/t
print(s,"kmph")

output:
enter the distance in kms60
enter the time min60
1.0 kmph

# write a program to check whether triangular is valid or not if sides are given
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
if a+b>c and a+c>b and b+c>a:
    print("triangle is valid")
else:
    print("triangle is not valid")


output:
enter a5
enter b7
enter c10
triangle is valid

# check the given number is even or odd
a=float(input("enter a"))
if a==2:
    print("given number is even")
else:
    print("the number is  odd")

output:
enter a5
the number is  odd

# check the given alphabet is vowel or consonant
a=(input("enter the alphabet"))
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("vowel")
else:
    print("consonant")

output:
enter the year2024
is leap year

# write a program to determine the grade based on marks
a=float(input("enter the marks"))
if a>=90:
      print("grade a")
elif a>=80 and a<=90:
      print("grade b")
elif a>=70 and a<=80:
      print("grade c")
elif a>=60 and a<=70:
      print("grade a")
elif a>=50 and a<=60:
      print("grade a")
else:
      print("failed")

output:
enter the marks2
failed

# prompt: determine the day of a week

day = float(input("Enter a number between 1 and 7: "))

if day == 1:
  print("Sunday")
elif day == 2:
  print("Monday")
elif day == 3:
  print("Tuesday")
elif day == 4:
  print("Wednesday")
elif day == 5:
  print("Thursday")
elif day == 6:
  print("Friday")
elif day == 7:
  print("Saturday")
else:
  print("Invalid input. Please enter a number between 1 and 7.")


Enter a number between 1 and 7: 1
Sunday

# print the *
n=int(input("enter the n"))
i=1
while i<=n:
  j=1
  while j<=i:  
    print('*',end='')
    j=j+1
  print()
  i=i+1   

enter the n5
*
**
***
****
*****

 # print the *
n=int(input("enter the n"))
i=5
while i>=1:
  j=1
  while j<=i:  
    print('*',end='')
    j=j+1
  print()
  i=i-1   

enter the n5
*****
****
***
**
*

 # program to find the sum of first 10 natural numbers(while loop)
n=int(input("enter the value"))
sum=0
i=1
while i<=n:
  sum=sum+i
  i=i+1
print(sum)

enter the value10
55

# program to find the sum of first 10 natural numbers(for loop)
n=int(input("enter the value"))
sum=0
for i in range(1,n+1):
  sum=sum+i
print(sum)

enter the value10
55

# write a program multiplication table (while loop)
n=int(input("enter the value"))
i=1
while i<=10:
  print(n,"*",i,"=",n*i)
  i=i+1

enter the value5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

# write a program multiplication table (for loop)
n=int(input("enter the value"))
for i in range(1,11):
  print(n,"*",i,"=",n*i)

enter the value5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50


