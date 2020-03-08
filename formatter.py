import sys
import re


for line in sys.stdin:
	sentcs = line.split('.')
	for snt in sentcs:
		print(' '.join(re.findall(r'[a-zA-Z0-9]+', snt)).lower())
		