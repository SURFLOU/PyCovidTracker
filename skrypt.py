import configparser
from bs4 import BeautifulSoup
import requests
import re
import pymongo
import dns
 
 
class Infections:
    def __init__(self, date, number, deaths, hospitals, month):
        self.date = date
        self.number = number
        self.deaths = deaths
        self.hospitals = hospitals
        self.month = month

 
client = pymongo.MongoClient("mongodb+srv://piotrus:02031998@cluster0.co6jd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['covid']
col = db['zakazenia']
 
quote_page = 'https://pl.wikipedia.org/wiki/Pandemia_COVID-19_w_Polsce'
page = requests.get(quote_page)
 
soup = BeautifulSoup(page.text, 'html.parser')
 
for tag in soup():
    for attribute in ["style"]:
        del tag[attribute]
 
stat_tables = soup.find_all(name=True, attrs={'class': ['wikitable', 'mw-collapsible',
                                                        'mw-collapsed', 'mw-made-collapsible']})[-7:-2]
 
month_list = []
for table in stat_tables:
    month_list.append(table.get_text())
 
 
infection_list = []
 
for i, el in enumerate(month_list):
    month_list[i] = el.split('\n')
    month_list[i] = list(filter(None, month_list[i]))
 
 
    current_list = month_list[i]
    for y, ele in enumerate(current_list):
        if re.match('([0-2][0-9]|(3)[0-1])(\.)(((0)[0-9])|((1)[0-2]))', ele):
            string = str(ele)
            month = ""
            if string[4] == "6":
                month = "June"
            elif string[4] == "7":
                month = "July"
            elif string[4] == "8":
                month = "August"
            elif string[4] == "9":
                month = "September"
            elif string[4] == "0":
                month = "October"
            deaths = str(current_list[y+3])
            if deaths == "–":
                deaths = "0"
            infections = str(current_list[y+1])
            infections_string = infections.replace(u'\xa0', u'')  # removed completely
            infections_New = infections_string.replace(u' ', u'')
            hospitals = str(current_list[y+7])
            hospitals_string = hospitals.replace(u'\xa0', u'')  # removed completely
            infection_list.append(Infections(ele, infections_New, deaths, hospitals_string, month))

