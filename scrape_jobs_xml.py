#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("http://sandiego.craigslist.org/search/sof")
webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

"""
updated=[]
description=[]
other=[]
"""

def start_program():
    for counter in soup.find_all('section', class_='page-container'):
        for n, tag in enumerate(counter.find_all('li', class_='result-row')):
            description = [x for x in tag.find_all('li')]
            print("Description: ", description[n].text.strip())
            print()


data = pd.DataFrame({"Description", description})
print(pd)

with open('data_write.xml', 'w') as f: # Writing in XML file
    for line in xml_data:
        f.write(line)
start_program()