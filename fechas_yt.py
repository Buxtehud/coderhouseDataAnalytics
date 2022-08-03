import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options



url = 'https://charts.youtube.com/charts/TopSongs/global?hl=es'


option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('D:\Escritorio\Programacion\Projects\chromedriver.exe',options=option)
driver.get(url)

time.sleep(2)

fechas = driver.find_element_by_xpath('/html/body/ytmc-app/div[3]/ytmc-charts/div[1]/div[2]/ytmc-dropdown/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox')

fechas_1=fechas.find_elements_by_tag_name('paper-item')

fechas_full = []

for i in fechas_1:
    partial = i.get_attribute('option-id')[7:].replace(':','-')
    if partial[:4]=='2020':
        fechas_full.append(partial)