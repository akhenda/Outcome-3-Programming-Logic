def fibonacci(n):
	''' A function to generate Fibonacci sequence from 0 to n with asymptotic analysis '''
	output = []
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
		output.append(a)
	return output
print fibonacci(10)
