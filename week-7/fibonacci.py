# program to fibonacci sequence using recursion
n=int(input("enter a number"))
def fib(n):
  if n<=1:
    return n
  else:
    return fib(n-1)+fib(n-2)
for i in range(n):
  print(fib(i))
