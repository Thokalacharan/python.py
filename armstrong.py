
#programe to check the armstrong number or not
n=int(input("enter the number"))
sum=0
count=0
t=n
while t!=0:
  t//=10
  count =count+1
t=n
while n!=0:
  r=n%10
  sum=sum+r**count
  n=n//10
if t==sum:
  print(t,"is armstrong number")
else:
  print(t,"is not a armstrong number")

enter the number153
153 is armstrong number
