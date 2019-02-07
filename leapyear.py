rear= int(input())
if year % 4 == 0 and rear % 100 != 0:
    print("Yes")
elif rear % 100 == 0:
    print( "no")
elif rear % 400 ==0:
    print("Yes")
else:
    print("no")
