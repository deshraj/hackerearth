import sys
t = sys.stdin.readline()
t = int(t)
n2 = sys.stdin.readline().split(' ')
for i in n2:
	for n in range(1,int(i)+1):
		if(n%3==0 and n%5==0):
			print "FizzBuzz"
		elif (n%3==0):
			print "Fizz"
		elif(n%5==0):
			print "Buzz"
		else:
			print n
