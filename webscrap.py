'''
Implement a program in python to auto generate Amazon Price
[ Automated Amazon Price Tracker ]

Author: Chirag Ganguli
Last Modified: 03 Oct 2022
'''

import os
import requests
from bs4 import BeautifulSoup

files = os.listdir(".")

def downloadSiteSource(link):
    file = open("scrapped-content.txt", 'w')
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    page = requests.get(link, headers=HEADERS)
    soup = BeautifulSoup(page.content, "lxml")

    parentprice = soup.find("span", attrs={"class": "a-price a-text-price a-size-medium apexPriceToPay"})
    price = parentprice.find("span", "a-offscreen").text.strip().replace(',', '').replace('₹', '')
    print("Product Price: ", str(price))
    file.write(f"{price}")
    #file.write(str(soup))
    file.close()

def checkPrice(expectedPrice):
    file = open("scrapped-content.txt", "r")
    price = int(float(file.read()))
    if(price <= expectedPrice):
        print("Congratulations! Product is within Expected Price Range")
    else:
        print("Sorry! Price of the Product is still higher")
    

if __name__ == '__main__':
    print("Input an Amazon Link to track price: ")
    link = str(input())
    downloadSiteSource(link)
    expectedPrice = int(input("Price Expected Price for Purchase: "))
    checkPrice(expectedPrice)

try:
    del link
    del expectedPrice
except Exception:
    pass