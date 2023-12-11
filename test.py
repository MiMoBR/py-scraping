
from requests import get
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import time
import re

url = 'https://www.hostelworld.com/hostels/Berlin'
response = get(url)

# create soup
soup = BeautifulSoup(response.text, 'html.parser')

# creating individual containers, on each one there's information about one hostel.
holstel_containers= soup.findAll(class_= 'fabresult rounded clearfix hwta-property')

# how many hostels on the page
len(holstel_containers)
#view rawBeautifulSoup_tutorial_1.py hosted with ❤ by GitHub