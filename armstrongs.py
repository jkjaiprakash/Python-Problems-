j,k=raw_input().split()
j=int(j)
k=int(k)
 
for n in range(j,k):
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum =sum+ digit ** 3
       temp /= 10
 
   if n == sum:
       print(n)
