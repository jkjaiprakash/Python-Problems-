year = int(input("Enter Year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Yes")
elif year % 100 == 0:
    print( "not")
elif year % 400 ==0:
    print("Yes")
else:
    print("not")
