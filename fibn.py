import time
startTime = time.clock()
while 1:
	n = int(input("How many terms?"))
	if n < 0 :
	   	print("Enter a positive number")
	else:
		if n == 1 :
			print n
		else:
			a=0
			b=1
			c=a+b
			count=0
			print("Fibonacci sequence:")
			print a
			print b
			while (count <= n):
				c=a+b
				print c
				a=b
				b=c
				count += 1
	break
print time.clock() - startTime, "seconds"
