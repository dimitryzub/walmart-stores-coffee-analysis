from serpapi import WalmartSearch
from urllib.parse import (parse_qsl, urlsplit)
import pandas as pd
import os, re, json


store_ids = pd.read_json('/workspace/serpapi-demo-projects/walmart-coffee-analysis/script/walmart-stores.json')

COFFEE_TYPES = [
    'Espresso',
    'Double Espresso',
    'Red Eye',
    'caramel flavored',
    'caramel',
    'colombian',
    'french',
    'italian',
    'Black Eye',
    'Americano',
    'Long Black',
    'Macchiato',
    'Long Macchiato',
    'Cortado',
    'Breve',
    'Cappuccino',
    'Flat White',
    'Cafe Latte',
    'Mocha',
    'Vienna',
    'Affogato',
    'gourmet coffee',
    'Cafe au Lait',
    'Iced Coffee',
    'Drip Coffee',
    'French Press',
    'Cold Brew Coffee',
    'Pour Over Coffee',
    'Cowboy Coffee',
    'Turkish Coffee',
    'Percolated Coffee',
    'Infused Coffee',
    'Vacuum Coffee',
    'Moka Pot Coffee',
    'Espresso Coffee',
    'Antoccino',
    'Cafe Bombon',
    'Latte',
    'City roast',
    'American roast',
    'Half City roast',
    'New England roast',
    'Light City roast',
    'Blonde roast',
    'Cinnamon roast',
    'Breakfast roast',
    'Full City roast',
    'Continental roast',
    'High roast',
    'New Orleans roast',
    'Espresso roast',
    'Viennese roast',
    'European roast',
    'French roast',
    'Italian roast',
    'Galao',
    'Caffe Americano',
    'Cafe Cubano',
    'Cafe Zorro',
    'Doppio',
    'Espresso Romano',
    'Guillermo',
    'Ristretto',
    'Cafe au lait ',
    'Coffee with Espresso',
    'Dead eye',
    'Botz',
    'Nitro Coffee',
    'Bulletproof Coffee',
    'Black tie',
    'Red tie',
    'Dirty chai latte',
    'Yuenyeung',
    "Bailey's Irish Cream and Coffee",
    'Caffè Corretto',
    'Rüdesheimer Kaffee',
    'Pharisee',
    'Barraquito',
    'Carajillo',
    'Irish coffee',
    'Melya',
    'Espressino',
    'Caffè Marocchino',
    'Café miel',
    'Cafe Borgia',
    'Café de olla',
    'Café Rápido y Sucio',
    'Coffee with a flavor shot',
    'Caffè Medici',
    'Egg coffee',
    'Kopi susu',
    'Vienna Coffee',
    'Iced lattes',
    'Iced mochas',
    'Ca phe sua da',
    'Eiskaffee',
    'Frappé',
    'Freddo Espresso',
    'Freddo Cappuccino',
    'Mazagran',
    'Palazzo',
    'Ice Shot',
    'Shakerato',
    'Instant Coffee',
    'Canned Coffee',
    'Coffee Milk',
    'South Indian Coffee',
    'Pocillo',
    'Arabica',
    'Robusta Beans',
    'Liberica Beans',
    'Excelsa Beans',
    'White Roast Coffee',
    'Light Roast',
    'Medium Roast',
    'Medium-Dark Roast',
    'medium dark',
    'medium dark roast',
    'Classic Roast',
    'black silk ground coffee',
    'black rifle coffee',
    'Dark Roast',
    'Kopi Luwak Coffee',
    'Jacu Bird Coffee',
    'Black Ivory Coffee'
]

for store_id in store_ids['store_id']:
    params = {
        'api_key': os.getenv('API_KEY'),  # serpapi api key
        'engine': 'walmart',              # search engine
        'device': 'desktop',              # device type
        'query': 'coffee',                # search query
        'store_id': store_id
    }

    search = WalmartSearch(params)       # where data extraction happens
    print(params)                        # just to show the progress
    
    data = []
    page_num = 0

    while True:
        results = search.get_json()      # JSON -> Python dict

        if results['search_information']['organic_results_state'] == 'Fully empty':
            print(results['error'])
            break

        page_num += 1
        print(f'Current page: {page_num}')

        for result in results.get('organic_results', []):
            title = result.get('title').lower() if result.get('title') else result.get('title')
            
            # https://regex101.com/r/h0jTPG/1
            try:
                weight = re.search(r'(\d+-[Ounce|ounce]+|\d{1,3}\.?\d{1,2}[\s|-]?[ounce|oz]+)', title).group(1)
            except: weight = 'not mentioned'
            
            # ounce -> grams
            # formula: https://www.omnicalculator.com/conversion/g-to-oz#how-to-convert-grams-to-ounces
            # https://regex101.com/r/wWMUQd/1
            if weight != 'not mentioned':
                weight_formatted_to_gramms = round(float(re.sub(r'[^\d.]+', "", weight)) * 28.34952/1, 1)
            
            coffee_type = ",".join([i for i in COFFEE_TYPES if i.lower() in title])
            
            data.append({
                'title': title,
                'coffee_type': coffee_type.lower(),
                'rating': result.get('rating'),
                'reviews': result.get('reviews'),
                'seller_name': result.get('seller_name').lower() if result.get('seller_name') else result.get('seller_name'),
                'thumbnail': result.get('thumbnail'),
                'price': result.get('primary_offer').get('offer_price'),
                'weight': weight,
                'weight_formatted_to_gramms': weight_formatted_to_gramms
            })
            
        # check if the next page key is present in the JSON
        # if present -> split URL in parts and update to the next page
        if 'next' in results.get('serpapi_pagination', {}):
            search.params_dict.update(dict(parse_qsl(urlsplit(results.get('serpapi_pagination', {}).get('next')).query)))
        else:
            break
    
pd.DataFrame(data=data).to_json('coffee-listings-from-all-walmart-stores.json', orient='records')
pd.DataFrame(data=data).to_csv('coffee-listings-from-all-walmart-stores.csv', index=False)
