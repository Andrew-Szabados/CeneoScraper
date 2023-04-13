from requests import get, codes 
from bs4 import BeautifulSoup
# product_code = input("Please enter product code: ")
# product_code = "138536499"
product_code = "138536499"
#url = "https://www.ceneo.pl/" + product_code + "tab=reviews"
#url = "https://www.ceneo.pl/" + product_code + "tab=reviews", format(product_code)
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
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
            opinion_id = opinion["data-entry-id"]
            author = opinion.select_one("span.user-post__author-name").text.strip()
            recommendation = opinion.select_one("span.user-post__author-recomendation > em").text.strip()
            score = opinion.select_one("span.user-post__score-count").text.strip()
            content = opinion.select_one("div.user-post__text").text.strip()
            pros = opinion.select_one("div.review-feature__col:contains('+') + div.review-feature__item-list").text.strip()
            pros = [p.text.strip() for c in pros]
            cons = opinion.select_one("div.review-feature__col:contains('-') + div.review-feature__item-list").text.strip()
            cons = [p.text.strip() for c in cons]
            upvote = opinion.select_one("").text.strip()
            downvote = opinion.select_one("").text.strip()
            helpful = opinion.select_one("button.vote-yes > span").text.strip()
            unhelpful = opinion.select_one("button.vote-no > span").text.strip()
            posted = opinion.select_one("span.user-post_published > time:nth-child(1")["datetime"]
            try:
                purchased = opinion.select_one("span.user-post_published > time:nth-child(2")["datetime"]
            except TypeError:
                purchased = None
            "opinion_id": opinion_id
            "author": author
            "recommendation": recommendation
            "score": score
            "content": content
            "pros": pros
            "cons": cons
            "helpful": helpful
            "unhelpful": unhelpful
            "published_at": published
            "purchased_at": purchased
    

