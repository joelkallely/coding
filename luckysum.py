def lucky(a,b,c):
	if a == 13:
		return 0
	elif b == 13:
		return a
	elif c == 13:
		return a+b
	else:
		return a+b+c
num1=int(raw_input("Enter a:"))
num2=int(raw_input("Enter b:"))
num3=int(raw_input("Enter c:"))
ans = lucky(num1,num2,num3)
print ans
