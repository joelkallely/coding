# program to check if firat or last number is 6
print"Enter 5 numbers:"
lst = []
for i in range(0,5):
	a =int( raw_input())
	lst.append(a)
print lst
if lst[0] == 6:
	print"first is a 6"
elif lst[4] == 6:
	print"last is 6"
else :
	print"neither last or first is 6"
