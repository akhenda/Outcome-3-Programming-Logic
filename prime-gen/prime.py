def prime(num):
	''' A function to generate prime numbers from 0 to n with asymptotic analysis '''
	primes = []
	for n in range(1,num):
		if all(n % i != 0 for i in range(2,n)):
			primes.append(n)
	return primes
