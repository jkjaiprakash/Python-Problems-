while True:
	try:
		z, b= raw_input().split( )
		z=int(z)
		b=int(b)
		break
	except:
		print("Invalid input")
		break
c=1
for x in range(b):
	c=c*z
print(c)
	
