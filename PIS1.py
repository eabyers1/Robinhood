#!/usr/bin/python3
import csv
import urllib.request
import urllib.parse
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/Users/enochbyers/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)

Price = []
saveFile1 = open('withHeaders.csv','w')
saveFile2 = open('E-LogFile.txt','w')


for i in range(485):
	t = time.localtime()
#	print(t[5])
	if i == 0:
		urld = 'https://robinhood.com/login'
		driver.get(urld)
		time.sleep(17)
		elem = driver.find_element_by_name('username')
		elem.send_keys('enochbyers@gmail.com')
		elem = driver.find_element_by_name('password')
		elem.send_keys('Tenison141')
		elem.send_keys(Keys.RETURN)
		 
#Selector copied directly from website inspection option, old and inefficient method
#		driver.find_element_by_css_selector("#react_root > div > div > div > div:nth-child(2) > div > div > form > footer > div > button > span").click()
		time.sleep(18)
		urld = 'https://robinhood.com/stocks/450dfc6d-5510-4d40-abfb-f633b7d9be3e'
		driver.get(urld)
#	if i >= 1:
	time.sleep(29)
	t = time.localtime()
#	print(t[5])
	while 8 < t[3] < 13:
#		print(t[5],'yep')

		try:
			url = 'https://www.nasdaq.com/symbol/aapl/real-time'
			req = urllib.request.Request(url)
			resp = urllib.request.urlopen(req)
			respData = resp.read()
			goods = re.findall(r'<span id="quotes_content_left__LastSale" style="display:inline-block;">(.*?)</span>',str(respData))
			saveFile1.write("%s; " % str(goods[0]))
			prices = driver.find_elements_by_class_name('_9YsRP4ChsxbL9qzZnKv0K')
#			driver.find_element_by_name('quantity').send_keys(int('1'))
			for price in prices:
				Price.append(price.text)
			Price = [x for x in Price if x !='']
			for p in Price:
				saveFile1.write(p)
			saveFile1.write("; %s %s %s\n" % (t[3],t[4],t[5]))
			Price = []

		except Exception as e:
			saveFile2.write(str(e))

		break	

saveFile1.close()
saveFile2.close()

#D = 50;

#if time between open and close then run, if not then quit program

#p = price of stock
#if p in range then buy and s = D/p

#For s =! 0
#While D < profit margin you set
#if D <= 0 stop


