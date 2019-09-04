from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://www.newegg.com/global/in-en/p/pl?d=graphics+card'

uClient= uReq(my_url)

page_html=uClient.read()
uClient.close()
#HTML parsing
page_soup= soup(page_html, "html.parser")
# grabs product
containers= page_soup.findAll("div",{"class":"item-container"})

filename= "products.csv"
f= open(filename, "w")
headers= "brand, product_name\n"

f.write(headers)

for container in containers:

   cont= container.findAll("a",{"class":"item-img"})
   brand= cont[0].img["title"]

   title_container= container.findAll("a", {"class": "item-title"})
   product_name= title_container[0].text.strip()

   print("brand: "+ brand)
   print("product_name: "+ product_name)

   f.write(brand.replace(",","|") +","+ product_name.replace(",","|")+ "\n")

f.close()
   
