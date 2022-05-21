#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("http://sandiego.craigslist.org/search/sof")
webpage = response.content
soup = BeautifulSoup(webpage, "html.parser")

updated = [1,2,3,4,5]
"""
updated=[]
description=[]
other=[]
"""

data = []
data = pd.DataFrame({"updated", updated, "Description", description, "other", other})
print(pd)

with open('data_write.xml', 'w') as f: # Writing in XML file
    for line in xml_data:
        f.write(line)