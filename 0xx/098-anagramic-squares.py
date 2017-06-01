
from tqdm import *
from math import *

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
	print pairs
	start = 10000
	ctr = int(sqrt(start))

	while True:
		n = ctr**2


main()