"""

    This codes purpose is to give me the latest story
    listing from a specific website. Website not mentioned for reasons.

"""

import requests
from bs4 import BeautifulSoup

# get input from user
url = input("Enter the URL: ")
finalUrl = ""

# check if user input www
if "www." in url:
    # replace www with http://
    finalUrl = url.replace("www.", "http://")
else:
    finalUrl = "https://" + url

print("url : " + finalUrl)


# get web page html content
r = requests.get(finalUrl)

# grab all the text and parse to html
soup = BeautifulSoup(r.text, 'html.parser')

formatted_link = []

for link in soup.find_all('h2', class_='post-block__title'):
    # get the name of the a attribute with whitespaces stripped
    name = [text for text in link.stripped_strings]
    print("TITLE : " + name[0])
    print("URL : " + link.a['href'])
    """
    data = {
        'title': name[0],
        'URL': link.a['href']
    }
    print(data)
    #formatted_link.append(data)
    """
#print(formatted_link)