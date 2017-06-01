from tqdm import *

def is_anagram(s1, s2):
	return sorted(list(s1)) == sorted(list(s2))

def main():
	words = []
	with open("098-anagramic-squares.txt","r") as f:
		words = (f.read()).split(',')
		words = map(lambda x: x[1:-1], words)
	n = len(words)
	pairs = set()
	for i in tqdm(range(n)):
		for j in range(i+1,n):
			if len(words[j]) > 4:
				if is_anagram(words[i], words[j]):
					pairs.add((words[i],words[j]))
	print pairs

main()