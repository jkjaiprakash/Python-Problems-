test=['a','e','i','o','u','A','E','I','O','U']
a=raw_input()
if(a in test):
	print('vowel')
elif(a!=test):
	print('consonant')
else:
	print('invalid')
