import webbrowser
from bs4 import BeautifulSoup
import urllib

# Get a file-like object for the Python Web site's home page.
site = "http://www.france24.com/fr/"
f = urllib.urlopen(site)

# webbrowser.open_new_tab(site) # open in browser tab

# Read from the object, storing the page's contents in 'html_page'
html_page = f.read()
f.close()

soup = BeautifulSoup(html_page)
those_items = soup.find_all("span", class_="title")
for child in those_items:
	print child.get_text().encode('utf-8')
	print

those_items = soup.find_all("h2", class_="title")
for child in those_items:
	print child.get_text().encode('utf-8')
