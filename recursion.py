# write a program to find factorial of a given number using recursion
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
n=int(input("enter a number"))
if (n<0):
  print("factorial does not exist for negative numbers")
else:
  print(fact(n))
