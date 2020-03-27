import requests
from bs4 import BeautifulSoup
import pprint
import json

cleansers_item_dict = dict()
cleansers_link = []

page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/cleansers.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    cleansers_link.append(a['href'])

id = 1

for line in cleansers_link:
    print(line)
    page = requests.get(line)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1").find("span").text
    print(title)
    try:
        description = soup.find(
            "div", {"class": "value", "itemprop": "description"}).findAll("p")[0].text
    except:
        pass
    try:
        description = soup.find(
            "div", {"class": "value", "itemprop": "description"}).findAll("div")[0].text
    except:
        pass

    try:
        description = soup.find(
            "div", {"class": "value", "itemprop": "description"}).text
    except:
        pass
    price = soup.find("span", {"class": "price"}
                      ).text.strip().lstrip("$")
    img_link = soup.find(
        "div", {"class": "gallery-placeholder"}).find("img")['src']
    print("title: " + title)
    print("Description: " + description)
    print("Price: " + price)
    cleansers_item_dict.update(
        {id: {'name': title, 'description': description, 'price': price, 'img_link': img_link}})
    id += 1

pprint.pprint(cleansers_item_dict)
