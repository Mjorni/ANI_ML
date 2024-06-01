import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time
import csv

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84 (Edition Yx 08)'
   
}


def test():
    line = 'https://shikimori.me/animes'
    need_page = 150
    current_page = 0
    list_link = []
    while current_page != need_page:
        links = requests.get(line, headers = headers)
        link = links.text
        soup = BeautifulSoup(link, 'html.parser')  

        for i in soup.find_all('a', class_ = 'cover anime-tooltip', href=True):
                list_link.append(f"{i['href']}\n")
        current_page += 1
        line = soup.find(class_ = 'link link-next', href = True)['href']
        time.sleep(1)
        print(line, links)
    with open("page.txt", 'w') as f:
        f.writelines(list_link)
    


    
def get_hrml():
    "через вебдрайвер(не нужно)"
    step = 0
    driver = webdriver.Chrome()
    driver.get(f"https://shikimori.me/animes/page/{step_page}")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 0.5
    list_link = []

    last_height = driver.execute_script("return document.body.scrollHeight")
    while step != step_count:
        #скролим вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # пауза
        time.sleep(SCROLL_PAUSE_TIME)
        # опять скролим по высоте,
        new_height = driver.execute_script("return document.body.scrollHeight")
        step += 1
        if step == step_count:
            main_page = driver.page_source
            soup = BeautifulSoup(main_page, 'html.parser')
            for i in soup.find_all('a', class_ = 'cover anime-tooltip-processed', href=True):
                list_link.append(f"{i['href']}\n")
            
            with open("page.txt", 'w') as f:
                f.writelines(list_link)
    last_height = new_height


if __name__ == "__main__":
    pass