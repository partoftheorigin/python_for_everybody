import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

stuff = ET.fromstring(data)

lst = stuff.findall('comments/comment')
print "Count:", len(lst)

total = 0
for item in lst:
	total += int(item.find('count').text)
print "Sum:", total



