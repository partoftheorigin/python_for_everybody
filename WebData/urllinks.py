# Note - this code must run in Python 2.x and you must download

# http://www.pythonlearn.com/code/BeautifulSoup.py

# Into the same folder as this program


import urllib

import ssl
from BeautifulSoup import *


url = raw_input('Enter - ')


for i in range(7):

	scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

	html = urllib.urlopen(url, context=scontext).read()

	soup = BeautifulSoup(html)


	# Retrieve all of the anchor tags

	tags = soup('a')

	url = tags[17].get('href', None)

	
print url
