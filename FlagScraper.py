import requests
import re
from bs4 import BeautifulSoup
import urllib
import os


l1s = ['https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags', 'https://en.wikipedia.org/wiki/Gallery_of_flags_of_dependent_territories'] # 'https://commons.wikimedia.org/wiki/City_flags'
l2s = ['https://commons.wikimedia.org/wiki/Flags_of_unrecognized_states', 'https://commons.wikimedia.org/wiki/Flags_of_extinct_states']
l3s = ['https://en.wikipedia.org/wiki/Flags_of_country_subdivisions']
l4s = ['https://commons.wikimedia.org/wiki/Historical_flags', 'https://commons.wikimedia.org/wiki/International_flags', 'https://commons.wikimedia.org/wiki/Flags_of_active_autonomist_and_secessionist_movements', 'https://commons.wikimedia.org/wiki/Cultural_flags', ]

os.chdir('raw')

flagpages = []

for l in l1s:
	html = requests.get(l)

	#turn the HTML into a beautiful soup text object
	b = BeautifulSoup(html.text, 'lxml')

	for div in b.find_all('div', {"class":"thumb"}):
		for img in div.find_all("img"):
			flagpages += ["https://en.wikipedia.org"+img.parent.get('href')]


for l in l2s:
	html = requests.get(l)

	#turn the HTML into a beautiful soup text object
	b = BeautifulSoup(html.text, 'lxml')
	for a in b.find_all("a", {"class":"image"}):
		flagpages += ["https://en.wikipedia.org"+a.get('href')]

for l in l3s:
	html = requests.get(l)

	#turn the HTML into a beautiful soup text object
	b = BeautifulSoup(html.text, 'lxml')

	for span in b.find_all('span', {"class":"flagicon"}):
		for a in span.find_all("a"):
			flagpages += ["https://en.wikipedia.org"+a.get('href')]
for l in l4s:
	html = requests.get(l)

	#turn the HTML into a beautiful soup text object
	b = BeautifulSoup(html.text, 'lxml')

	for img in b.find_all('img', {"height":"100"}):
		flagpages += ["https://commons.wikimedia.org"+img.parent.get('href')]


for page in flagpages:
	print page
	html = requests.get(page)

	b = BeautifulSoup(html.text, 'lxml')

	div = b.find('div', {'class': "fullImageLink"})
	a = div.find_all('a')[0]
	img = a.find_all('img')[0]
	name = page[35:-4]
	name = name.replace("Flag_of_", "")
	filename = "%s.png" % name
	if img.get('src')[:6] == "https:":
		url = img.get('src')
	else:
		url = "https:"+img.get('src')
	image=urllib.URLopener()
	image.retrieve(url,filename)



