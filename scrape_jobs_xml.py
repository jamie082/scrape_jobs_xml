#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

# craigslist page, data for Python3 http://sandiego.craigslist.org/search/sof

response = requests.get("http://sandiego.craigslist.org/search/sof")
webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

"""
updated=[]
description=[]
other=[]
"""

def start_program():
    for counter in soup.find_all('form', class_='search-form'):

        for n, tag in enumerate(counter.find_all('ul', class_='rows')):
            description = [x for x in tag.find_all('li')]
            # output job
            print("Description: ", description[n].text.strip())
            print()


"""
data = pd.DataFrame({"Description", description, "Location", location,})
print(pd)
"""

with open('data_write.xml', 'w') as f: # Writing in XML file
    for line in xml_data:
        f.write(line)
start_program()