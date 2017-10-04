import json

import urllib

url = raw_input('Enter location: ')


print 'Retrieving', url
uh = urllib.urlopen(url)

data = uh.read()

print 'Retrieved',len(data),'characters'


info = json.loads(str(data))


count = len(info['comments'])

print "Count", count


total = 0

for i in range(count):

    total += int(info['comments'][i]['count'])

print "Sum:", total

