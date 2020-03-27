import requests
from bs4 import BeautifulSoup
import csv
import os.path

categories = ["Cleansers", "Masks", "SkinCare", "Makeup", "BodyCare"]

cleansers_link = []
masks_links = []
skincare_links = []
makeup_links = []
bodycare_links = []

page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/cleansers.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    cleansers_link.append(a['href'])


page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/masks.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    masks_links.append(a['href'])

page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/skincare.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    skincare_links.append(a['href'])


page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/makeup.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    makeup_links.append(a['href'])

page = requests.get(
    'https://ca.naturecollection.com/en/shop/shop-by-products/body-care.html?product_list_limit=all')
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.findAll("div", {"class": "product-item-detail"})
for item in items:
    a = item.find("a", href=True)
    bodycare_links.append(a['href'])

# Output the address to csv file
with open(os.path.join('Outputs', 'cleansers_link.csv'), 'w') as file:
    for line in cleansers_link:
        file.write(line)
        file.write('\n')

with open(os.path.join('Outputs', 'masks_links.csv'), 'w') as file:
    for line in masks_links:
        file.write(line)
        file.write('\n')

with open(os.path.join('Outputs', 'skincare_links.csv'), 'w') as file:
    for line in skincare_links:
        file.write(line)
        file.write('\n')

with open(os.path.join('Outputs', 'makeup_links.csv'), 'w') as file:
    for line in makeup_links:
        file.write(line)
        file.write('\n')

with open(os.path.join('Outputs', 'bodycare_links.csv'), 'w') as file:
    for line in bodycare_links:
        file.write(line)
        file.write('\n')
