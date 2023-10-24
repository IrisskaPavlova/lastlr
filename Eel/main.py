import eel
import pyowm
import requests 
from bs4 import BeautifulSoup

eel.init("web")
eel.start("main.html", mode="browser")
@eel.expose

def horoscope(zodiac_sign: int, day: str) -> str: 
    url = ( 
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}") 
    soup = BeautifulSoup(requests.get(url).content, "html.parser") 

    # print(soup.find("div", class_="main-horoscope").p.text) 
    return soup.find("div", class_="main-horoscope").p.text

def zz(date,month):
    date=int(date)
    month=int(month)
    if (21<=date<=18 and month==3) or( month==4 and 1<=date<=19):
        zodiac_sign=1
        
    elif (20<=date<=30 and month==4) or( month==5 and 1<=date<=20):
        zodiac_sign=2
        
    elif (21<=date<=31 and month==5) or( month==6 and 1<=date<=21):
        zodiac_sign=3
        
    elif (22<=date<=30 and month==6) or( month==7 and 1<=date<=22):
        zodiac_sign=4
        
    elif (23<=date<=31 and month==7) or( month==8 and 1<=date<=22):
        zodiac_sign=5
        
    elif (23<=date<=31 and month==8) or( month==9 and 1<=date<=22):
        zodiac_sign=6
        
    elif (23<=date<=30 and month==9) or( month==10 and 1<=date<=23):
        zodiac_sign=7
        
    elif (24<=date<=31 and month==10) or( month==11 and 1<=date<=22):
        zodiac_sign=8
        
    elif (23<=date<=30 and month==11) or( month==12 and 1<=date<=21):
        zodiac_sign=9
        
    elif (22<=date<=31 and month==12) or( month==1 and 1<=date<=20):
        zodiac_sign=10
        
    elif (21<=date<=31 and month==1) or( month==2 and 1<=date<=18):
        zodiac_sign=11
        
    elif (19<=date<=29 and month==2) or( month==3 and 1<=date<=20):
        zodiac_sign=12
    return horoscope(zodiac_sign,'Today')




