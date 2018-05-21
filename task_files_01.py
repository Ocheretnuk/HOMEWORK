q = int(input())
w = int(input())

with open('data.txt') as f:
	o1 = ''
	o2 = ''
	for i in f.read().split():
		i = int(i)
		if i%q == 0:
			o1 += str(i) + ' '
		o2 += str(pow(i,w)) + ' '
		
with open('out-1.txt', 'w') as f:
	f.write(o1)

with open('out-2.txt', 'w') as f:
	f.write(o2)