
import requests
from bs4 import BeautifulSoup
import lxml
import json
import settings

session = requests.Session()



def connect(url,session=session,headers=settings.HEADERS):
	request = session.get(url,headers=headers)
	return request


def get_city_url(city,url_api=settings.URL_API):
    url = url_api + city
    json_city = json.loads(connect(url).text)
    url_city = json_city['items']
    if url_city:
        return url_city[0]['url']
    return None



def get_weather_city(url_city,url=settings.URL):
    if url_city:
        result_str = ''
        url_weather = url + url_city
        print(url_weather)
        contents = connect(url_weather).content
        soup = BeautifulSoup(contents,'lxml')
        list_div_tab_wrap = soup.find('div',{'class':'weathertabs day-1'}).find_all('div',{'class':'weathertab-wrap'})
        #print(len(list_div_tab_wrap))
        
        for div in list_div_tab_wrap:
            date = div.find('div',{'class':'date'}).text.strip()
            #print(date)
            list_temperature = div.find_all('span',{'class':'unit unit_temperature_c'})
            temperature_night = list_temperature[0].text.strip()
            #print(temperature_night)
            temperature_day = list_temperature[1].text.strip()
            #print(temperature_day)
            result_str += date + '\n температура ночью ' + temperature_night + '\n температура днем ' + temperature_day + '\n'
        return result_str
    return 'Город введен не верно повторите'

'''
def main():
    print("Программа прогноз погоды!")
    action = True
    while action:
        print("Введите ваш город!")
        enter_city = input()
        if enter_city != '':
            get_weather_city(get_city_url(enter_city))
            print('Завершить программу ? y/n')
            end_program = input().lower()
            if end_program == 'y' or end_program == 'у':
                action = False



if __name__ == '__main__':
	main()
'''