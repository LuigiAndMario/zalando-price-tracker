import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
f = open('watchlist.json')
watchlist = json.load(f)
f.close()

for item in watchlist:
    contents = watchlist[item]
    
    page = requests.get(contents['url'], timeout=10, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    full_price = soup.find_all('span', class_=contents['full price'])[0].string
    reduction = soup.find_all('span', class_=contents['reduction']) if 'reduction' in contents else list()

    if (len(reduction) == 0):
        output = item + ': ' + full_price
    else:
        reduced_price = soup.find_all('span', class_=contents['reduced price'])[0].string
        output = item + ': ' + reduced_price + ' (reduction of ' + reduction[0].string.split(' ')[0] + ')'
    

    print(output)
