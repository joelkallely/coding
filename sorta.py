def sum(a,b):
	return a+b
num1 = int(raw_input("Enter a:"))
num2 = int(raw_input("Enter b:"))
s = sum(num1,num2)
if s>9 and s<20:
	print"20"
else:
	print s
