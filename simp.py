
#!/usr/bin/python3
import requests
import urllib.request
import urllib.parse
import csv
import datetime
import time
import random
import re
#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Multiple windows can be opened.  Use this to compare info.  Driver2 is for NASDAQ

chromedriver = '/Users/enochbyers/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
#driver2 = webdriver.Chrome(chromedriver)

saveFile1 = open('withHeadersRobin.csv','w')
saveFile2 = open('E-LogFileRobin.txt','w')

url = 'https://robinhood.com/login'
#url2 = 'https://nasdaq.com/symbol/zyne/real-time'
driver.get(url)
#driver2.get(url2)
time.sleep(20)
elem = driver.find_element_by_name("username")
elem.send_keys('enochbyers@gmail.com')
elem = driver.find_element_by_name("password")
elem.send_keys('Tenison141')
elem.send_keys(Keys.RETURN)


#selector copied directly from website inspection option.  Old and inefficient way to click button
#driver.find_element_by_css_selector("#react_root > div > div > div > div:nth-child(2) > div > div > form > footer > div > button").click()


#url = 'https://robinhood.com/stocks/e39605bf-9789-41f5-8b50-9bd38fec8f17'
#		url = 'https://robinhood.com/stocks/FCEL'
#		url = 'https://api.robinhood.com/mfa'
#		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
#		headers = {'User-Agent': user_agent}
#		headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
#		headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
#headers = {}		
#headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
#req = urllib.request.Request(url)
#resp = urllib.request.urlopen(req)
#respData = resp.read()
#		goods = re.findall(r'<span id="quotes_content_left__LastSale" style="display:inline-block;">(.*?)</span>',str(respData))
#r = s.post(url, data=payload)

time.sleep(20)

#Below URL is for APPLE as a test

url = 'https://robinhood.com/stocks/450dfc6d-5510-4d40-abfb-f633b7d9be3e'
driver.get(url)
time.sleep(16)

#Now we want to input how many shares we want.  The selector to complete order,
#must change div.theme in code to open or closed. closed = after hours

driver.find_element_by_name('quantity').send_keys(int('1'))
#driver.find_element_by_css_selector("#react_root > div > main > div:nth-child(2) > div > div._203Qy0QZFOhcU3wYhTYKdj > div > main > div.row > div.col-5 > div > form > div:nth-child(2) > div.theme-closed-up > div > div._3_Y5qz2hHsr3c1JlQ15G0N > button").click()

#Reading price in Robinhood


prices = driver.find_elements_by_class_name('_9YsRP4ChsxbL9qzZnKv0K')
Price = []
for price in prices:
	Price.append(price.text)
Price = [x for x in Price if x !='']
for p in Price:
	saveFile1.write(p)
#time.sleep(10)
#result = s.get(url)

#saveFile1.write(str(result))
#	except Exception as e:
#		saveFile2.write(str(e))	

#url = 'https://api.robinhood.com/oauth2/token/'
#Site = 'https://api.robinhood.com/user/'
#Site1 = 'https://google.com'
#with requests.Session() as session:
#	post = session.post(url, data=payload)
#	time.sleep(10)
#	r = session.get(Site)
#	p = session.get(Site1)
#	saveFile2.write(str(p))
#	if r.status_code == 404:
#		saveFile2.write(str(r))
#	if r.ok:	
#		saveFile1.write(str('OMG SUCCESS!!!!!'))

saveFile1.close()
saveFile2.close()

#driver.quit()

