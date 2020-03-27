import requests
from bs4 import BeautifulSoup
import pprint
import json
import os.path

bodycare_item_dict = dict()
bodycare_links = []

page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/body-care.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    bodycare_links.append(a['href'])

id = 1

for line in bodycare_links:
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
    try:
        price = soup.find("span", {"class": "price"}
                          ).text.strip().lstrip("$")
    except:
        price = ''
    img_link = soup.find(
        "div", {"class": "gallery-placeholder"}).find("img")['src']
    print("title: " + title)
    print("Description: " + description)
    print("Price: " + price)
    bodycare_item_dict.update(
        {id: {'name': title, 'description': description, 'price': price, 'img_link': img_link, 'category': 'Body Care'}})
    id += 1

pprint.pprint(bodycare_item_dict)

with open(os.path.join('Outputs', 'bodycare.json'), 'w') as fp:
    json.dump(bodycare_item_dict, fp)
