t,k=raw_input().split()
t=int(t)
k=int(k)
for num in range(t,k+ 1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num,
