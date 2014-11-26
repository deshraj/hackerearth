import sys
t = sys.stdin.readline()
t = int(t)
while(t):
	a,b = sys.stdin.readline().split(' ')
	a = int(a)
	b = int(b)
	print a+b
	t = t-1
