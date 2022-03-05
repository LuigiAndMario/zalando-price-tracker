import scraper

results = scraper.scrape()

for item in results:
    output = item + ': ' + results[item][0]
    if len(results[item]) == 2:
        output = output + '(' + results[item][1] + ')'
    print(output)