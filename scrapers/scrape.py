"""import os
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()"""
"""
browser = webdriver.Chrome("\Users\Aumit\Downloads\chromedriver_win32\chromedriver.exe")  
browser.get('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&;langId=-1&a;storeId=58552')  
html_source = browser.page_source  
browser.quit()

soup = BeautifulSoup(html_source,'html.parser')  
#class "postText" is not defined in the source code
soup.prettify()
"""






























from bs4 import BeautifulSoup
import urllib2
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html

class Render(QWebPage):  
	def __init__(self, url):  
	    self.app = QApplication(sys.argv)  
	    QWebPage.__init__(self)  
	    self.loadFinished.connect(self._loadFinished)  
	    self.mainFrame().load(QUrl(url))  
	    self.app.exec_()

	def _loadFinished(self, result):  
		self.frame = self.mainFrame()
		self.app.quit() 


url = 'http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&;langId=-1&a;storeId=58552';
r = Render(url)
result = r.frame.toHtml()
formatted_result = str(r.frame.toHtml().toAscii())


#page = str(result)
#test = html.fromstring(str(result.toAscii()))
#page = html.fromstring(str(result.toAscii()))
#r = urllib2.urlopen('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&;langId=-1&a;storeId=58552').read()



#http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552
#r = urllib2.urlopen('https://www.google.com/').read()
soup = BeautifulSoup(formatted_result, 'html.parser') 

#temp = soup.find("div", {"class" : "accessFCMLink"})
print soup.title
print soup.prettify()[0:1000]

print "Some people want it bad, other just of want it" 






































"""from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://rutgers.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&langId=-1&storeId=58552').read()

#r = urllib.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all').read()

soup = BeautifulSoup(r, "lxml")
print type(soup)
#print soup.prettify()[0:1000]
#print soup.title
print soup.find_all('h1')
bookForm = soup.find("form", {"id": "FindCourse"})

"""



"""
#Example app to login to GitHub
import argparse
import mechanicalsoup

parser = argparse.ArgumentParser(description='Login to GitHub.')
parser.add_argument("username")
#parser.add_argument("aumleo13@gmail.com")
parser.add_argument("password")
#parser.add_argument("a3h15l97")

args = parser.parse_args()

browser = mechanicalsoup.Browser()

# request github login page. the result is a requests.Response object http://docs.python-requests.org/en/latest/user/quickstart/#response-content
#login_page = browser.get("https://github.com/login")
# Attempting to log in to facebook test
login_page = browser.get("https://www.facebook.com/")

# login_page.soup is a BeautifulSoup object http://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup 
# we grab the login form
login_form = login_page.soup.select("#login")[0].select("form")[0]
#login_form = login_page.soup.select("#menu_login_container")[0].select("form")[0]

# specify username and password
login_form.select("#login_field")[0]['value'] = args.username
login_form.select("#password")[0]['value'] = args.password

#testing for facebook
#login_form.select("#inputtext")[0]['value'] = args.username
#login_form.select("#inputtext")[1]['value'] = args.password

# (or alternatively)
# login_form.input({"login": args.username, "password": args.password})

# submit form
page2 = browser.submit(login_form, login_page.url)

# verify we are now logged in
messages = page2.soup.find('div', class_='flash-messages')
if messages:
    print(messages.text)
assert page2.soup.select(".logout-form")
#assert page2.soup.select("._w0d")

print(page2.soup.title.text)

# verify we remain logged in (thanks to cookies) as we browse the rest of the site
page3 = browser.get("https://github.com/hickford/MechanicalSoup")
#page3 = browser.get("https://www.facebook.com/messages/100008620874932")
assert page3.soup.select(".logout-form")
#page3.soup.select("._w0d")
"""
