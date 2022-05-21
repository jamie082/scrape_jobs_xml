#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

updated = []
description = []
other = []

response = requests.get("http://pythonjobs.github.io/")
webpage = response.content

# Store the webpage contents
webpage = response.content

# Create a BeautifulSoup object out of the webpage content
soup = BeautifulSoup(webpage, "html.parser")

data = []
data = pd.DataFrame({"updated", updated, "Description", description, "other", other})
print(pd)