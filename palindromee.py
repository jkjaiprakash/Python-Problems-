def main():
 j=int(input(""))
 temp=j
 rev=0
 while(j>0):
    dig=j%10
    rev=rev*10+dig
    j=j//10
 if(temp==rev):
    print("yes")
 else:
    print("no")

if __name__ == '__main__':
    main()
