import itertools

def apply(x,y,op):
	if x == None or y == None: return None
	if op == "a": return x+y
	if op == "s": return x-y
	if op == "m": return x*y
	if op == "d": 
		if y == 0: return None
		else: return x*1.0/y

def all_nums(a,b,c,d):
	perms = list(itertools.permutations([a,b,c,d]))
	ops = ["a","m","s","d"]
	res = []
	for w,x,y,z in perms:
		for op1 in ops:
			for op2 in ops:
				for op3 in ops:
					num1 = apply(apply(apply(w,x,op1),y,op2),z,op3)
					num2 = apply(apply(w,x,op1),apply(y,z,op3),op2)
					num3 = apply(apply(w,apply(x,y,op2),op1),z,op3)
					num4 = apply(w,apply(x,apply(y,z,op3),op2),op1)
					num5 = apply(w,apply(apply(x,y,op2),z,op3),op1)
					for num in [num1,num2,num3,num4,num5]:
						if num != None and num > 0:
							res.append(num)
	ctr = 1
	res = set(res)
	while True:
		if ctr not in res: break
		ctr += 1
	return ctr-1

def main():
	most = 0
	sol = ""
	for a in range(1,10):
		for b in range(a+1,10):
			for c in range(b+1,10):
				for d in range(c+1,10):
					cur = all_nums(a,b,c,d)
					if cur >= most:
						most = cur
						sol = str(a)+str(b)+str(c)+str(d)
	print most, sol
	print all_nums(1,2,5,8)
main()
