import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'resultsTable'})
rows = soup.find('tr')

data = []
for row in rows:
    th_cell = rows.findAll('th')
    td_cell = rows.findAll('td')
    try:
	    data.append({'description' : th_cell[0].get_text().replace('&nbsp;', ''),
		             'record' : td_cell[0].get_text().replace('&nbsp;', '')})
    except IndexError:
	    pass

		
with open('./inmates.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)