# zalando-price-tracker

Uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape price data from Zalando.de.

The program reads data from a file `watchlist.json`, which has the following structure:
```
{
    "item": url,
    ...
}
```

The program finds the full price of each item, as well as their reduced price (if any).