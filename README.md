# zalando-price-tracker

Uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape price data from Zalando.de.

The program reads data from a file `watchlist.json`, which has the following structure:
```
{
    "item1": { 
        "url": "...",
        "full price": "...",
        "reduced price": "...",
        "reduction": "..."
    },
    ...
}
```

Zalando.de uses very weird class names, and they are different for every item. There needs to be another way to detect that.