while True:
	try:
		a, b= raw_input().split( )
		a=int(a)
		b=int(b)
		break
	except:
		print("Invalid input")
		break
c=1
for x in range(b):
	c=c*a
print(c)
	
