import sys
import json


print('{', end='')


def out(k, w):
	if w:
		print(f'{json.dumps(k)}: {json.dumps(w)}, ', end='')


lastkey = 0
words = dict()

for line in sys.stdin:
	key, value = line.split()
	if key == lastkey:
		if value in words:
			words[value] += 1
		else:
			words[value] = 1
	else:
		out(lastkey, words)
		lastkey = key
		words = dict()
		words[value] = 1

if words:
	print(f'{json.dumps(key)}: {json.dumps(words)}' + '}')
