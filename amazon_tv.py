from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url= 'https://www.amazon.in/b/ref=s9_acss_bw_ln_x_1_1_w?node=5903486031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-leftnav&pf_rd_r=0357QYZPHFHRQ5H9DS2W&pf_rd_t=101&pf_rd_p=b6497d66-2e74-4910-be93-a3f3f25854cf&pf_rd_i=1389396031'

uClient1= uReq(my_url)

page_html1=uClient1.read()
uClient1.close()

page_soup1=soup(page_html1, "html.parser")

amazontv=page_soup1.findAll("div",{"class":"s-item-container"})

file_name= "amazontv.csv"
f1= open(file_name, "w")
headers= "product_name, Height\n"

f1.write(headers)

for amazon in amazontv:
	amaz=amazon.findAll("a",{"class":"a-link-normal a-text-normal" })
	product_name=amaz[0].img["alt"]

	height_pro=amazon.findAll("a",{"class":"a-link-normal a-text-normal"})
	Height= height_pro[0].img["height"]

	print("Product Name: "+ product_name)
	print("Height: "+ Height)

	f1.write(product_name+","+ Height+ "\n")

f1.close()	






