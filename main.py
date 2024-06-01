import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from threading import Thread
import time
"""
    ФАЙЛ НЕ ИСПОЛЬЗУЕТСЯ
"""

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.sleep112.102 Safari/537.36 OPR/90.0.4480.84 (Edition Yx 08)'
   
}
links = requests.get('http://www.world-art.ru/animation/animation.php?id=311', headers)
link = links.text
soup = BeautifulSoup(link, 'html.parser')

f = open("page.txt", "r")
name_list = []
type_list = []
count_episode_list = []
duration_ep_list = []
status_list = []
age_rating_list = []
rating_list = []
second_rating_list = []
review_list = []
comment_list = []

sleep = 1
next_sleep = 2
class Get_information:

    
        def __init__(self):
            self.f = open("page.txt", "r")
            
            
        "1"
        def get_name(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(5)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                
                #soup = BeautifulSoup(link, 'html.parser')
                start_search = link.find('h1') + len('h1>')
                end_search = link.find("<span", start_search)
                
                #name_list.append(soup[start_search:end_search])
                #print(soup[start_search:end_search])
                #print(link[start_search:end_search])
                name_list.append(link[start_search:end_search])
                time.sleep(sleep)
                print(link[start_search:end_search])
                
                
            print(name_list)
            time.sleep(next_sleep)
            Get_information().get_type()
        "2"
        def get_type(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                soup = BeautifulSoup(link, 'html.parser')
                type_list.append(soup.find("div", class_ = "value").string)
                #print(soup.find("div", class_ = "value").string)
                time.sleep(sleep)
            print(type_list)
            time.sleep(next_sleep)
            time.sleep(next_sleep)
            Get_information().get_count_episode()
            
        "3"
        def get_count_episode(self):
            for i in self.f:
            
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                #soup = BeautifulSoup(link, 'html.parser')

                ss = link.find("Эпизоды") # для определения наличия большого количества серий
                start_c_eps = link.find('value', ss) + len("value'>")
                end_c_eps = link.find("<", start_c_eps)
                if ss == -1:
                    count_episode_list.append("1")
                else:
                    #print(link[ss:ss+len("Эпизоды")])
                    count_episode_list.append(link[start_c_eps:end_c_eps])
            
                time.sleep(sleep)
            i
            print(count_episode_list)
            time.sleep(next_sleep)
            Get_information().get_dur_ep()

        "4"
        def get_dur_ep(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                sde = link.find("Длительность эпизода")
                lf_search_dur = link.find("span", sde)
                start_search_dur = link.find(">", lf_search_dur) + 1
                end_search_dur = link.find("</span>", start_search_dur)
                duration_ep_list.append(link[start_search_dur:end_search_dur - 1])
                time.sleep(sleep)
            print(duration_ep_list)
            time.sleep(next_sleep)
            Get_information().get_status()

        "5"
        def get_status(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                sde = link.find("Статус")
                lf_search_stat = link.find("data-text=", sde) + len("data-text=") + 1
                end_search_stat = link.find(">", lf_search_stat)
                if link[lf_search_stat:end_search_stat - 1].lower() == "онгоинг":
                    status_list.append("0")
                else:
                    status_list.append("1")
                
                time.sleep(sleep)
            print(duration_ep_list)
            time.sleep(next_sleep)
            Get_information().get_age_rating()

        "6"       
        def get_age_rating(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                sde = link.find("Рейтинг")
                lf_search_age_rating = link.find("span", sde)
                start_search_age_rating = link.find(">", lf_search_age_rating) + 1
                end_search_age_rating = link.find("</span>", start_search_age_rating)
                age_rating_list.append(link[start_search_age_rating:end_search_age_rating])
                time.sleep(sleep)
            print(age_rating_list)
            time.sleep(next_sleep)
            Get_information().get_rating()
        
        "7"
        def get_rating(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                soup = BeautifulSoup(link, 'html.parser')
                rating_list.append(soup.find(class_ = "score-value score-9").string)
                time.sleep(sleep)
            print(rating_list)
            time.sleep(next_sleep)
            Get_information().get_second_rating()
                

        "8"
        def get_second_rating(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                soup = BeautifulSoup(link, 'html.parser')
                second_rating_list.append(soup.find(class_ = "score-notice").string)
                time.sleep(sleep)
            print(second_rating_list)
            time.sleep(next_sleep)
            Get_information().count_review()

        "9"
        def count_review(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                sde = link.find("У аниме:")
                lf_search_age_rating = link.find("reviews", sde) + 1
                start_search_age_rating = link.find('"', lf_search_age_rating) + 2
                end_search_age_rating = link.find(' ', start_search_age_rating)
                review_list.append(link[start_search_age_rating:end_search_age_rating])
                time.sleep(sleep)
            print(review_list)
            time.sleep(next_sleep)
            Get_information().count_comment()
        "10"
        def count_comment(self):
            for i in self.f:
                links = requests.get(i, headers=headers)
                while links.status_code == 429:
                    print("Повтор")
                    time.sleep(3)
                    links = requests.get(i, headers=headers)
                    print(links.status_code)
                link = links.text
                sde = link.find("У аниме:")
                lf_search_age_rating = link.find("obsuzhdenie-anime", sde) + 1
                start_search_age_rating = link.find('"', lf_search_age_rating) + 2
                end_search_age_rating = link.find(' ', start_search_age_rating)
                print(link[start_search_age_rating:end_search_age_rating])
                comment_list.append(link[start_search_age_rating:end_search_age_rating])
                time.sleep(sleep)
                
            print(comment_list)
            time.sleep(next_sleep)
            Get_information().run()
            
        
        def run(self):
            a = zip(name_list, type_list, count_episode_list, duration_ep_list, status_list, age_rating_list, second_rating_list, rating_list, review_list, comment_list, strict=True)
            #new_str = '\n'.join(''.join(elems) for elems in a)
            #new_list = list(a)
            
            

            with open("zipfile.csv", 'w') as filek:
                filek.write(f"Название, Тип, Количество, Длительность, Статус, Возростной рейтинг, Рейтинг, Оценивают, Рецензий, Комментариев\n")
                for i in a:
                    filek.write(f"{', '.join(i).replace('(', '')}\n")
            
          
"""with open("zipfile.csv", 'r') as fi:
    for i in fi:
        print(type(i))"""

run = Get_information()

Get_information().get_name()