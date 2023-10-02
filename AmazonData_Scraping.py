import requests
from bs4 import BeautifulSoup
import pandas as pd

# Link of the website to be scraped
url = "https://www.amazon.in/s?k=iphone&crid=1HWGHMSLMFVN8&sprefix=iphon%2Caps%2C221&ref=nb_sb_noss_2"

# Requesting the website and extracting information through get, using header since extraction from website is denied
proxies = {'https': '162.223.94.164'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, headers=headers)

# It is difficult to scrap using just response object, hence we use BS object.
soup = BeautifulSoup(r.content, 'html.parser')

# Storing the extracted data
data = {'Product Name': [], 'Price': []}

# Scraping product name
# Extracting all span elements with class given below
ProductName = soup.select("span.a-size-medium.a-color-base.a-text-normal")
for name in ProductName:
    print(name.text)
    data['Product Name'].append(name.text)

# Scraping product price
ProductPrice = soup.select("span.a-price-whole")
for price in ProductPrice:
    print(price.text)
    data['Price'].append(price.text)

# Converting the disctionary to data frame
df = pd.DataFrame.from_dict(data)

# Storing the df in a csv file
df.to_csv("data.csv", index=False)
