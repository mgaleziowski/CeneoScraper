import requests, json 
from bs4 import BeautifulSoup

def get_element(ancestor, selector=None, attribute=None, return_list=False):
       try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
       except AttributeError:
           return None
       
selectors={
        "opinion_id":[None,"data-entry-id"],
        "author":["span.user-post__author-name"],
        "recomendation":["span.user-post__author-recomendation > em"],
        "score":["span.user-post__score-count"],
        "purchased":["div.review-pz"],
        "published_at":["span.user-post__published > time:nth-child(1)","datetime"],
        "purchased_at":["span.user-post__published > time:nth-child(2)","datetime"],
        "thubs_up":["button.vote-yes > span"],
        "thumbs_down":["button.vote-no > span"],
        "content":["div.user-post__text"],
        "pros":["div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item",None,True],
        "cons":["div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item",None,True],
    }

#product_code=input("Podaj kod produktu: ")
product_code="96875119"
#product_code="11017453"
nr=1
while(nr<3):
    url=f"https://www.ceneo.pl/{product_code}/opinie{nr}"
    response=requests.get(url)
    page=BeautifulSoup(response.text,'html.parser')
    #print(get_element(page))
    opinions=page.select("div.js_product-review")
    all_opinions=[]
    for opinion in opinions:
        single_opinion={}
        #print(opinion["data-entry-id"])
        for k,v in selectors.items():
            single_opinion[k]=get_element(opinion,*v)
        all_opinions.append(single_opinion)
        with open(f"./opinions/{product_code}.json","w",encoding="UTF-8") as jf:
            json.dump(all_opinions,jf,indent=4,ensure_ascii=False)


    