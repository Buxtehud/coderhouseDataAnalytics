import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from fechas_yt import fechas_full

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('D:\Escritorio\Programacion\Projects\chromedriver.exe',options=option)

rank = []
canciones = []
artistas = []
visualizaciones = []
fechas_ = []

for fecha in fechas_full:
    
    url_ini = 'https://charts.youtube.com/charts/TopSongs/global'
    url_end = '?hl=es'
    url_date = fecha
    
    url = url_ini+'/'+url_date+url_end
    
    driver.get(url)
    
    time.sleep(10)

    tabla = driver.find_element_by_xpath('/html/body/ytmc-app/div[3]/ytmc-charts/div[2]/ytmc-chart-table/div/div')
    
    rank_prev = tabla.find_elements_by_css_selector('div.current-rank.style-scope.ytmc-chart-table')
    
    canciones_prev = tabla.find_elements_by_tag_name('ytmc-ellipsis-text')
    
    artistas_prev = tabla.find_elements_by_tag_name('ytmc-artists-list')
    
    visualizaciones_prev = tabla.find_elements_by_css_selector('div.views.style-scope.ytmc-chart-table')
    
    for i in range(20):
        rank.append(rank_prev[i].text)
        canciones.append(canciones_prev[i].text)
        artistas.append(artistas_prev[i].text)
        visualizaciones.append(visualizaciones_prev[i].text)
        fechas_.append(fecha)
    
    
lista = {'ranking':rank,'canciones':canciones,'artistas':artistas,'visualizaciones':visualizaciones,'Semana':fechas_}

df=pd.DataFrame(lista)