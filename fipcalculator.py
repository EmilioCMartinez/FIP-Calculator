#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:54:24 2019

@author: EmilioMartinez
"""
'''
import requests
from bs4 import BeautifulSoup 

# specify the url
url = 'https://rmacsports.org/stats.aspx?path=baseball&year=2019' 
page = requests.get(url)

soup = BeautifulSoup(page, 'html.parser' ) 
'''


#FIP Calculator  
lgERA = 6.57
lgHR =  395
lgBB = 1518
lgHBP = 419 
lgK  = 2720
lgIP = 3193.1

HR = 2
BB = 10
HBP = 0
K = 52
IP = 52.2

CONST =   lgERA - (((13*lgHR) + (3*(lgBB + lgHBP)) - (2 * lgK)) / lgIP)

FIP = (((13 * HR) + (3* (BB + HBP)) - (2 * K)) / IP) + CONST

print(FIP)
