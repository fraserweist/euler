def gcd(a,b):
	if b == 0: return a
	else: return gcd(b, a%b)

def main():
	size = 50
	res = 3*(size**2)
	for x in range(1,size+1):
		for y in range(1,size+1):
			f = gcd(x, y)
			res += min(y*f/x, (size-x)*f/y)*2
	print res

main()