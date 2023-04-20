from requests import get, codes 
from bs4 import BeautifulSoup
import json

def get_element(ancestor, selector = None, attribute = None, return_list = False):
    try:
        if return_list:
           return [tag.text.strip() for tag in opinions_select]
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return  ancestor.select_one(selector)[attribute].strip()
        return  ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None
    
# product_code = input("Please enter product code: ")
# product_code = "138536499"
product_code = "138536499"
#url = "https://www.ceneo.pl/" + product_code + "tab=reviews"
#url = "https://www.ceneo.pl/" + product_code + "tab=reviews", format(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
while url:
    response = get(url)
if response.status_code == codes['ok']:
    page_dom = BeautifulSoup(response.text, "html.parser")
    try:
        opinions_count = page_dom.select_one("a.product-review__link > span").text.strip()
    except AttributeError:
        opinions_count = 0
    if opinions_count > 0:
        all_opinions = []
        opinions = page_dom.select("div.js_product-review")
        for opinion in opinions:
            single_opinion = {}
            for key, value in selectors.items():
                single_opinion[key] = get_element(opinion, *value)
            all_opinions.append(single_opinion)
    try: 
        url = "https://www.ceneo.pl" + get_element(page_dom, "a.pagination_next, "href")
        with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf
                    json.dumps(all_opinions, jf, indent=4, ensure_ascii=False)