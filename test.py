# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rv4Bywiz66PyDqTuyDLEtj5mpxWVNZPd
"""

import matplotlib.pyplot as plt

plt.rc('font', family='NanumBarunGothic') 

import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/item/main.nhn?code=005930")

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

soup.select('#time')[0].text

onestep=soup.select('.blind')[5].text
print(onestep)

onestep.soup.select('.blind')
