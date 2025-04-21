n=int(input("enter a number"))
if n>1:
	while(n>1):
		m=(n)*(n-1)
		n=n-1
	print("the factorial of number is:", m)
elif n==1 or n=0:
	print("the factorial of number is: 1")
else:
	print("enter valid input...!")
