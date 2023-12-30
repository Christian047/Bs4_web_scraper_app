
# import relevant libraries
from turtle import title
import requests
from bs4 import BeautifulSoup

# provide a url to scrape
url = 'https://www.codewithtomi.com/'
# url = input('Enter your website: ')
# url1 = 'https://' + url


# A get request is sent to the url and stored in a variable
r = requests.get(url)

# a beautiful soup object is created 
soup = BeautifulSoup(r.content, 'html.parser')
title1 = soup.find_all('h2',{'class':'post-title'})

title2 = title1[0].getText()

# The title is looped into to get a cleaner code
for t in title1:
    print(t.getText())
