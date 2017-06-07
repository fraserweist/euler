import itertools

def apply(x,y,op):
	if x == None or y == None: return None
	if op == "a": return x+y
	if op == "s": return x-y
	if op == "m": return x*y
	if op == "d": 
		if y == 0: return None
		elif x%y != 0: return None
		else: return x/y

def all_nums(a,b,c,d):
	perms = list(itertools.permutations([a,b,c,d]))
	ops = ["a","m","s","d"]
	opperms = list(itertools.permutations(ops,3))
	res = []
	for w,x,y,z in perms:
		for op1,op2,op3 in opperms:
			num = apply(z,apply(y,apply(w,x,op1),op2),op1)
			if num != None and num > 0:
				res.append(num)
	return set(sorted(res))

def main():
	print all_nums(1,2,3,4)

main()