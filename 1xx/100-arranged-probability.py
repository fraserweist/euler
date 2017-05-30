from math import *
from tqdm import tqdm

def main():
	blues = 15
	discs = 21

	while discs < 1000000000000:
		nextb = 3*blues + 2*discs - 2
		nextd = 4*blues + 3*discs - 3
		blues, discs = nextb, nextd

	print blues, discs

main()