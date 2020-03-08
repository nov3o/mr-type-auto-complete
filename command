cat text | py formatter.py | py mapper.py | sort -k 1,1 | py reducer.py
