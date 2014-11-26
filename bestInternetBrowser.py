import sys,math
t = sys.stdin.readline()
t = int(t)
q = ['a','e','i','o','u']
while(t):
	s = sys.stdin.readline().rstrip('\n')
	len1 = len(s)
	count  = 0
	for i in s[4:-4]:
		if i not in q:
			count = count+1
			# print i,count
	print str(count+4)+"/"+str(len1)
	t = t-1
