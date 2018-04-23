x1 = int(input(''))
y1 = int(input(''))
x2 = int(input(''))
y2 = int(input(''))
x3 = int(input(''))
y3 = int(input(''))

a = ((x2-x1)**2 + (y2-y1)**2 )**0.5
b = ((x3-x2)**2 + (y3-y2)**2 )**0.5
c = ((x3-x1)**2 + (y3-y1)**2 )**0.5   

if a**2 == b**2 + c**2:
    print ("yes")
elif b**2 == a**2 + c**2:
    print ("yes")
elif c**2 == a**2 + b**2 :
    print ("yes")
else:
    print ("no")