import requests
from bs4 import BeautifulSoup
import random
import time

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.sleep112.102 Safari/537.36 OPR/90.0.4480.84 (Edition Yx 08)'
   
}

f = open('page.txt', 'r')
sleep = 4

list_link = []

def get_html(url):
    link = requests.get(url, headers = headers)
    while link.status_code != 200:
        time.sleep(sleep)
        link = requests.get(url, headers = headers)

    return link

def get_str_info():
    csv_file = open("AnimeData.csv", "w")
    csv_file.write(f"Название,Тип,Количество,Длительность,Статус,Возростной рейтинг,Реитинг,Оценивают,Рецензий,Комментариев\n")
    for i in f:
        try:         
            link = get_html(i).text
            print(link.find('age-restricted-warning'))

            soup = BeautifulSoup(link, 'html.parser')  
            if soup.find('p', class_ = 'age-restricted-warning'):
                continue

            "Название"
            #a = soup.find('alternativeHeadline').string
            start_search = link.find('h1') + len('h1>')
            end_search = link.find("<span", start_search) - 1
            name_title = link[start_search:end_search]
            if len(name_title) > 50:
                continue
            
            
            "Другое название"
            a = soup.find('h1')
            start_search = link.find('h1') + len('h1>')
            end_search = link.find("<span", start_search) - 1
            name_title = link[start_search:end_search]

            "Тип"
            type_title = soup.find("div", class_ = "value").string
            
            "Количество эпизодов"
            ss = link.find("Эпизоды") # для определения наличия большого количества серий
            start_c_eps = link.find('value', ss) + len("value'>")
            end_c_eps = link.find("<", start_c_eps)
            if ss == -1:
                count_ep = ("1")
            elif link[start_c_eps:end_c_eps] == "Спешл":
                count_ep = ("1")
            else:
                count_ep = link[start_c_eps:end_c_eps]
                if "/" in count_ep:
                    get_space = count_ep.find(" ")
                    count_ep = count_ep[:get_space]

            "Длительность"
            sde = link.find("Длительность эпизода")
            lf_search_dur = link.find("span", sde)
            start_search_dur = link.find(">", lf_search_dur) + 1
            end_search_dur = link.find("</span>", start_search_dur)
            duration_ep = link[start_search_dur:end_search_dur - 1]

            "Статус"
            sde = link.find("Статус")
            lf_search_stat = link.find("data-text=", sde) + len("data-text=") + 1
            end_search_stat = link.find(">", lf_search_stat)
            if link[lf_search_stat:end_search_stat - 1].lower() == "онгоинг":
                status = "0"
            else:
                status = "1"

            "Возрастной рейтниг"
            sde = link.find("Рейтинг")
            lf_search_age_rating = link.find("span", sde)
            start_search_age_rating = link.find(">", lf_search_age_rating) + 1
            end_search_age_rating = link.find("</span>", start_search_age_rating)
            age_rating = link[start_search_age_rating:end_search_age_rating]

            "Рейтинг"
            
            ssr = link.find('score-value score')
            start_search_rating = link.find('>', ssr) + 1
            end_search_rating = link.find('<', start_search_rating)
            rating = link[start_search_rating:end_search_rating]

            "Оценка"
            second_rating = soup.find(class_ = "score-notice").string

            "отзывов"
            sde = link.find("У аниме:")
            lf_search_age_rating = link.find("reviews", sde) + 1
            start_search_age_rating = link.find('"', lf_search_age_rating) + 2
            end_search_age_rating = link.find(' ', start_search_age_rating)
            review_list = link[start_search_age_rating:end_search_age_rating]
            if review_list.isdigit() == False:
                review_list = 0

            
            "Коменты"
            sde = link.find("У аниме:")
            lf_search_age_rating = link.find("obsuzhdenie-anime", sde) + 1
            start_search_age_rating = link.find('"', lf_search_age_rating) + 2
            end_search_age_rating = link.find(' ', start_search_age_rating)
            comment = link[start_search_age_rating:end_search_age_rating]


            """------------------------------"""

            "Вывод"
            result_str = f"{name_title}, {type_title}, {count_ep}, {duration_ep}, {status}, {age_rating}, {rating}, {second_rating}, {review_list}, {comment}\n"
            print(result_str)
            csv_file.write(result_str)
            time.sleep(sleep)
            len(name_title)
        except Exception as e:
            print(e)
            
            
    csv_file.close()
    

    


if __name__ == "__main__":
    pass
    