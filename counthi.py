cnt = 0
print "enter string"
string = raw_input()
spl = string.split()
print string
print spl
for i in spl:
	if i == "hi":
		cnt+=1
print cnt
