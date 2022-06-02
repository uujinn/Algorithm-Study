from math import factorial

n = str(factorial(int(input())))[::-1]

for i in n:
	if i != '0':
		print(i)
		exit(0)