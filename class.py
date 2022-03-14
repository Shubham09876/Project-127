import time 
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

StarUrl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
chromeBrowser = webdriver.Chrome('chromedriver.exe')
chromeBrowser.get(StarUrl)
time.sleep(10)

def scrapeData():
    headers = ['V Mag' , 'Proper Name' , 'Bayer Designation' , 'Distance' , 'Spectral Class' , 'Mass' , 'Radius' , 'Luminosity']
    starData = []

    for i in range( 0 , 198 ):
        soup = BeautifulSoup(browser.page_source , 'html.parser')

        for ulTag in soup.find_all('ul' , attrs = {'class' , 'stars'}):
            liTag = ulTag.find_all('li')
            starList = []

            for index , li in enumerate(liTag):
                if index == 0:
                    starList.append(li.find_all('a')[0].contents[0])
                else:
                    try:
                        starList.appned(li.contents[0])
                    except:
                        starList.append("")

            starData.append(starList)

            browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open('Project127.csv' , 'w') as file :
        fileWrite = csv.writer(file)
        fileWrite.writerow(headers)
        fileWrite.writerows(starData)

scrapeData()

    