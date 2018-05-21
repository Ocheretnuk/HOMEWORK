def fibonacci(n):
	num_1 = 0
	num_2 = 1
	for i in range(n):
		num_1, num_2 = num_2, num_1 + num_2
		yield num_1