for l in range(40):
	print("_", end ='')
	if l == 20:
		print("INPUT",end='')
print('')

i = float(input("Input of first concentrated point load (i): "))
j = float(input("Input of second concentrated point load (j): "))
x = float(input("Input distance of point load i from A (x): "))
y = float(input("Input distance of point load j from A (y): "))
c = float(input("Distance of point C from A (c): "))
l1 = float(input("Input of length of beam for section AB (l1): "))
l2 = float(input("Input of length of beam for section BC (l2): "))

def reactionAB():
	rb = (-j*y - i*x)/l1
	ra = -i-j-rb
	return "RA: " + str(ra) + "KN\nRB: " + str(rb)+"KN"

def internalshear():
	vc = 1-(x/l1)
	vc2 =  1 - y/l1
	c = -i*round(vc,2) - j*round(vc2,2)
	return "Internal shear force at point C: " + str(c)

def internalmoment():
	mc = 2-((2*x)/l1)
	mc2 = 2 - ((2*y)/l1)
	c = -i * round(mc,2)-j *round(mc2,2)
	return "Internal moment at point C: " + str(round(c,2))

print('')
for l in range(40):
	print("_", end ='')
	if l == 20:
		print("OUTPUT",end='')
print('')

print(reactionAB())
print(internalshear())
print(internalmoment())
