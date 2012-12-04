import webbrowser
from bs4 import BeautifulSoup
import urllib

### Prep ###
# Get a file-like object for the Python Web site's home page.
site = "http://www.france24.com/fr/"
f = urllib.urlopen(site)

# Read from the object, storing the page's contents in 'html_page'
html_page = f.read()
f.close()

# Prep soup var
soup = BeautifulSoup(html_page)

those_divs = soup.find("div", class_="title-provider")
# res2 = ''.join(tmp.getText().strip() for tmp in those_divs.findAll('a'))
those_divs.find_all("a")
for child in those_divs:
	grandchild = child.find_all("a")
	print(grandchild)

# print html_page

#### Helper ####
# def grab_data():
	

#### RUN ####
# ids = grab_data()

# for num in range(0,9): # assume >= 10
# 	webbrowser.open_new_tab("http://www.facebook.com/"+ids[0]) # open in a tab
	# webbrowser.open_new_tab("http://www.python.org") # open in a tab
