# Walmart Stores Coffee Analysis

This Python demo project is a practical showcase of using [SerpApi's](https://serpapi.com/) [Walmart Search Engine Results API](https://serpapi.com/walmart-search-api) plus how extracted data could be used in exploratory data analysis.

This repo covers:

1. [Extracting data from Walmart Organic results](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/extraction.py).
2. [Extracting data from all store pages using SerpApi pagination](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/extraction.py#L190-L195).
3. [Extracting data from 500 Walmart stores](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/walmart-stores.json). [SerpApi provides JSON Walmart Stores Locations](https://serpapi.com/walmart-stores) with 4.460 stores in total.
4. [My full process of exploratory data analysis](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/68a28ee3fe55372194076a2177a75d7502b26f5a/analysis/walmart-coffee-analysis.ipynb).

There's also a full blog post that also shows data extraction steps: https://serpapi.com/blog/serpapi-demo-project-walmart-coffee-exploratory-data-analysis/#extracting-walmart-data

## Key Takeaways

1. The Most popular coffee seller is Walmart.
2. The Most popular coffee type is medium roast. 
3. More weight (grams) doesn't equal higher price.
    - A lower gram coffee may cost more than a higher gram coffee.
4. The Highest coffee weight is 2835 grams (2.8 kg).
5. "Folgers classic roast ground coffee" has 15k+ reviews which is the maximum value from data set.
6. ~300-500 grams is the most frequent weight.
7. The Highest coffee price is $77 (Lavazza perfetto single-serve k-cup)