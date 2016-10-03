from bs4 import  BeautifulSoup
import urllib
import time
import random





# url for working over
url = 'http://tanglepatterns.com/category/b-tangles'
data = urllib.urlopen(url).read()

# Pauser
def pause():
	time.sleep(random.randint(0,5))

# Go and grab it
pause()
soup = BeautifulSoup(data,"html.parser")
print type(soup)

# returns a list of the images in main div
def getImageUrl(url):
	data = urllib.urlopen(url).read()
	pause()
	soup = BeautifulSoup(data, "html.parser")
	images_div = soup.find_all('div', attrs={'class':'post-boodycopy clearfix'})
	image_link
	return images


# find alist of posts in the body
# find main content div <td id="middle"></td> div
body = soup.find('td', attrs = {'id':'middle'})

# listification!
post_divs = body.find_all('div', attrs={'class':'post-headline'})
for div in post_divs:
	name = div.a.text[17:]
	page = div.a['href']

	images = getImageUrl(page)

	[image['src'] for image in images]
	print name + " " + page