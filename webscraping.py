# import bs4
# import requests
# import re

# res = requests.get('https://www.amazon.co.uk/Your-Home-Scratching-Activity-Scratcher/dp/B07FSMBQ3G/ref=pd_sbs_199_3/258-4522559-4297905?_encoding=UTF8&pd_rd_i=B07FSMBQ3G&pd_rd_r=d5f8333a-54a9-11e9-9482-49d0c5d60177&pd_rd_w=SbGjH&pd_rd_wg=rukRy&pf_rd_p=18edf98b-139a-41ee-bb40-d725dd59d1d3&pf_rd_r=YE6HY5XC7XZZ21KSNQQY&psc=1&refRID=YE6HY5XC7XZZ21KSNQQY')
# res.raise_for_status()


# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# elems = soup.select('#price_inside_buybox')
# price = elems[0].text.strip()

# print(price)



# import bs4,requests,pyperclip

# def getAmazonPrice(productUrl):
# 	res = requests.get(productUrl)
# 	res.raise_for_status()

	# soup = bs4.BeautifulSoup(res.text,'html.parser')
	# elems = soup.select('#price_inside_buybox')
	# #amazonTitle = soup.select('#productTitle')

	# return elems[0].text.strip()[0:]

# amazonText = open('amazonUrls.txt','r')
# amazonUrlList = amazonText.readlines()


# getAmazonPrice('https://www.amazon.co.uk/Brother-LS14S-Chassis-Sewing-Machine/dp/B07B6KL7VZ?ref_=Oct_DLandingS_PC_5adf3ab2_NA&smid=A3P5ROKL5A1OLE')


