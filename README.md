# Walmart Stores Coffee Analysis

<p align="center">
  <img src="https://user-images.githubusercontent.com/78694043/197740034-7da619f9-3155-4c6f-8a8c-4183914ee052.png" />
</p>

This Python demo project is a practical showcase of using [SerpApi's](https://serpapi.com/) [Walmart Search Engine Results API](https://serpapi.com/walmart-search-api) plus how extracted data could be used in exploratory data analysis.

This repo covers:

1. [Extracting data from Walmart Organic results](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/extraction.py).
2. [Extracting data from all store pages using SerpApi pagination](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/extraction.py#L190-L195).
3. [Extracting data from 500 Walmart stores](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/74d06e8016c1903ff53bfbde0263f98264baca1c/script/walmart-stores.json). [SerpApi provides JSON Walmart Stores Locations](https://serpapi.com/walmart-stores) with 4.460 stores in total.
4. [My full process of exploratory data analysis](https://github.com/dimitryzub/walmart-stores-coffee-analysis/blob/68a28ee3fe55372194076a2177a75d7502b26f5a/analysis/walmart-coffee-analysis.ipynb).

There's also a full blog post that also shows data extraction steps: https://serpapi.com/blog/serpapi-demo-project-walmart-coffee-exploratory-data-analysis/#extracting-walmart-data

Kaggle Dataset: https://www.kaggle.com/datasets/dimitryzub/walmart-coffee-listings-from-500-stores

## Key Takeaways

1. The most popular coffee seller is Walmart.
2. The most popular coffee type is medium roast. 
3. More weight (grams) doesn't equal higher price.
    - A lower gram coffee may cost more than a higher gram coffee.
4. The highest coffee weight is 2835 grams (2.8 kg).
5. "Folgers classic roast ground coffee" has 15k+ reviews which is the maximum value from data set.
6. ~300-500 grams is the most frequent weight.
7. The highest coffee price is $77 (Lavazza perfetto single-serve k-cup)

## Plots

![image](https://user-images.githubusercontent.com/78694043/197485001-8b89ea37-c1fe-44ab-bcc9-6ceaaea0dd53.png)


![image](https://user-images.githubusercontent.com/78694043/197485893-40ba9a63-66af-41d0-9bb2-169867ef4ba1.png)

### Most Frequent Weight (~300-500 grams)

![image](https://user-images.githubusercontent.com/78694043/197485990-222d62fa-47ac-43e5-868c-14a3550b8d2d.png)    

![image](https://user-images.githubusercontent.com/78694043/197486235-0eb214f9-aa67-41c5-84f1-acf0288c9e05.png)

### Higher weight = higher price?

![image](https://user-images.githubusercontent.com/78694043/197486297-93733268-0f8c-4e5f-8765-fbe37aac1cbf.png)

![image](https://user-images.githubusercontent.com/78694043/197486373-0d100eaa-da3c-4e43-aa68-16a8f94bc64e.png)
