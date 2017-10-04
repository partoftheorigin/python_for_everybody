import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_233206.txt"
handle = open(name)

total = 0
count = 0
a = tuple()
for line in handle:
	line = line.rstrip()
	a = re.findall('[0-9]+', line)
	for num in a:
		if len(a)<1: continue
		count += 1
		total += int(num)
print count	
print total

