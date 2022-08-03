import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('D:\Escritorio\Programacion\Projects\chromedriver.exe',options=option)

url_prev = 'https://spotifycharts.com/regional/global/weekly/'

rank = []
canciones = []
artistas = []
visualizaciones = []
fechas_rep = []

fechas = ['2020-12-25--2021-01-01',
 '2020-12-18--2020-12-25',
 '2020-12-11--2020-12-18',
 '2020-12-04--2020-12-11',
 '2020-11-27--2020-12-04',
 '2020-11-20--2020-11-27',
 '2020-11-13--2020-11-20',
 '2020-11-06--2020-11-13',
 '2020-10-30--2020-11-06',
 '2020-10-23--2020-10-30',
 '2020-10-16--2020-10-23',
 '2020-10-09--2020-10-16',
 '2020-10-02--2020-10-09',
 '2020-09-25--2020-10-02',
 '2020-09-18--2020-09-25',
 '2020-09-11--2020-09-18',
 '2020-09-04--2020-09-11',
 '2020-08-28--2020-09-04',
 '2020-08-21--2020-08-28',
 '2020-08-14--2020-08-21',
 '2020-08-07--2020-08-14',
 '2020-07-31--2020-08-07',
 '2020-07-24--2020-07-31',
 '2020-07-17--2020-07-24',
 '2020-07-10--2020-07-17',
 '2020-07-03--2020-07-10',
 '2020-06-26--2020-07-03',
 '2020-06-19--2020-06-26',
 '2020-06-12--2020-06-19',
 '2020-06-05--2020-06-12',
 '2020-05-29--2020-06-05',
 '2020-05-22--2020-05-29',
 '2020-05-15--2020-05-22',
 '2020-05-08--2020-05-15',
 '2020-05-01--2020-05-08',
 '2020-04-24--2020-05-01',
 '2020-04-17--2020-04-24',
 '2020-04-10--2020-04-17',
 '2020-04-03--2020-04-10',
 '2020-03-27--2020-04-03',
 '2020-03-20--2020-03-27',
 '2020-03-13--2020-03-20',
 '2020-03-06--2020-03-13',
 '2020-02-28--2020-03-06',
 '2020-02-21--2020-02-28',
 '2020-02-14--2020-02-21',
 '2020-02-07--2020-02-14',
 '2020-01-31--2020-02-07',
 '2020-01-24--2020-01-31',
 '2020-01-17--2020-01-24',
 '2020-01-10--2020-01-17',
 '2020-01-03--2020-01-10']

for fecha in fechas:
    
    url_fecha = fecha
    
    url = url_prev+url_fecha

    driver.get(url)
    
    time.sleep(10)
    
    tabla = driver.find_element_by_xpath('/html/body/div/div/div/div/span/table')
    
    rank_prev = tabla.find_elements_by_css_selector('td.chart-table-position')
    
    canciones_prev = tabla.find_elements_by_css_selector('td.chart-table-track')
    
    visualizaciones_prev = tabla.find_elements_by_css_selector('td.chart-table-streams')
    
    for i in range(20):
        rank.append(rank_prev[i].text)
        canciones.append(canciones_prev[i].text.split(' by ')[0])
        artistas.append(canciones_prev[i].text.split(' by ')[1])
        visualizaciones.append(visualizaciones_prev[i].text)
        fechas_rep.append(fecha)
        print(str(i)+fecha)
        
lista = {'ranking':rank,'canciones':canciones,'artistas':artistas,'visualizaciones':visualizaciones,'Semana':fechas_rep}

df=pd.DataFrame(lista)