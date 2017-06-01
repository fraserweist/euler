
from tqdm import *
from math import *

def str_map(s1, s2, n1):
	n = len(s1)
	nstr = str(n1)
	mapping = dict()
	for i in range(n):
		mapping[s1[i]] = nstr[i]
	n2 = ""
	for i in range(n):
		n2 += mapping[s2[i]]
	return int(n2)

def aligns(n, s):
	if len(str(n)) != len(s):
		return False
	nstr = str(n)
	nseen, sseen = [], []
	ncheck, scheck = "", ""
	nctr, sctr = 0, 0
	for i in range(len(s)):
		if nstr[i] not in nseen:
			ncheck += str(nctr)
			nctr += 1
			nseen.append(nstr[i])
		else:
			ncheck += str(nseen.index(nstr[i]))
		if s[i] not in sseen:
			scheck += str(sctr)
			sctr += 1
			sseen.append(s[i])
		else:
			scheck += str(sseen.index(s[i]))
	return ncheck == scheck


def is_square(n):
	sq = int(sqrt(n))
	return sq**2 == n

def is_anagram(s1, s2):
	return sorted(list(s1)) == sorted(list(s2))

def main():

	words = []
	with open("098-anagramic-squares.txt","r") as f:
		words = (f.read()).split(',')
		words = map(lambda x: x[1:-1], words)
	n = len(words)
	pairs = []
	for i in tqdm(range(n)):
		for j in range(i+1,n):
			if len(words[j]) > 4:
				if is_anagram(words[i], words[j]):
					pairs.append((words[i],words[j]))
	pairs.sort(key=lambda (s1,s2): -len(s1))

	start = 10000000000
	ctr = int(sqrt(start))
	solution, strings = 0, ("","")
	
	while True:
		n1 = ctr**2
		if n1 < 10000: break
		lst = filter(lambda (s1,s2): len(s1) == len(str(n1)), pairs)
		for (s1,s2) in lst:
			if aligns(n1, s1):
				n2 = str_map(s1,s2,n1)
				if len(str(n2)) != len(str(n1)): break
				if is_square(n2):
					if n1 > solution:
						solution, strings = n1, (s1, s2)
					if n2 > solution:
						solution, strings = n2, (s2, s1)
			if aligns(n1, s2):
				n2 = str_map(s2,s1,n1)
				if len(str(n2)) != len(str(n1)): break
				if is_square(n2):
					if n1 > solution:
						solution, strings = n1, (s1, s2)
					if n2 > solution:
						solution, strings = n2, (s2, s1)
		ctr -= 1
	s1,s2 = strings
	print solution, str_map(s1,s2,solution), strings

main()