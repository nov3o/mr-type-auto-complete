import sys


for line in sys.stdin:
	words = line.split()
	for i in range(len(words) - 1):
		print(f"{words[i]}\t{words[i + 1]}")