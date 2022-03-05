import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

def scrape():
    f = open('watchlist.json')
    watchlist = json.load(f)
    f.close()

    for item in watchlist:
        page = requests.get(watchlist[item], timeout=10, headers=HEADERS)
        soup = BeautifulSoup(page.content, 'html.parser')

        prices = soup.find_all('span', string=lambda text: text and '€' in text)
        if len(prices) == 1:
            price = prices[0].string
            output = item + ': ' + price
        else:
            reduced_price = prices[0].string
            # full_price = prices[1].string
            reduction = soup.find_all('span', string=lambda text: text and 'sparen' in text)[0].string.split(' ')[0]
            output = item + ': ' + reduced_price + ' (-' + reduction + ')'

        print(output)
