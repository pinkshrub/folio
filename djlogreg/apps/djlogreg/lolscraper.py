from bs4 import BeautifulSoup
import urllib2

url = 'http://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/1001890146?gameHash=87973487c28932d6&tab=stats'
site = urllib2.urlopen(url)
html = site.read()
soup = BeautifulSoup(html,'html.parser')
table = soup.find(attrs = {'id' : 'stats-body'})




print (soup.prettify())