l = []

for a in range(2, 101):
	for b in range(2, 101):
		l.append(a ** b)

l = list(set(l))

print(len(l))