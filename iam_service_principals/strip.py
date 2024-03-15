with open("i.txt", 'r') as f:
	raw = f.readlines()
	
data = []
for line in raw:
	for chunk in line.split(" "):
		if "@" in chunk:
			data.append(chunk)
			continue

with open('o.txt', 'w') as f:
	f.write('\n'.join(data))
