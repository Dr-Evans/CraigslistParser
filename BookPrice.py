import urllib2
import requests
from bs4 import BeautifulSoup as BS

class BookPrice:
	def __init__(self):
		self.promptInput()

	def promptInput(self):
		query = raw_input("Search your query\n")
		self.search(query)

	def search(self, query):
		site = "http://gainesville.craigslist.org/search/bka/"
		payload = {"query": query}
		r = requests.get(site, params=payload)
		print(r.url)

		soup = BS(r.text)

		htmlList = soup.find(id="toc_rows").findAll("p", class_="row")

		self.displaySearchResults(htmlList)

		print ""
		self.promptInput()

	def displaySearchResults(self, htmlList):
		for item in htmlList:
			title = item.span.a.get_text()
			print "Title: " + title

			price = item.find("span", class_="l2").find("span", class_="price")
			if price != None:
				price = price.get_text()			
				print "Price: " + price		
			else:
				print "Price not listed"

			place = item.find("span", class_="l2").find("span", class_="pnr").find("small")
			if place != None:
				place = place.get_text()			
				print "Place: " + place[2:-1]		
			else:
				print "Place not listed"
			
			print "---------------------"
			
BookPrice()
