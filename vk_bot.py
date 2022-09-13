import bs4, requests
class VkBot:

    def __init__(self, user_id):
    
        print("\nСоздан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        
        self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        
        return user_name.split()[0]

        # Метод для очистки от ненужных тэгов
 
    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        
        return result

    def new_message(self, message):

        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"
        
        # Погода
        elif message.upper() == self._COMMANDS[1]:
            return self._get_weather()
        
        # Время
        elif message.upper() == self._COMMANDS[2]:
            return self._get_time()
        
        # Пока
        elif message.upper() == self._COMMANDS[3]:
            return f"Пока-пока, {self._USERNAME}!"
        
        else:
            return "Не понимаю о чем вы..."
        

            # Получение времени:
    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    # Получение погоды
    def _get_weather(city_name: str = "Moscow") -> list:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        api_weather = '2167c514c5f8603fab1bf6a82b12f3ab'
        
        params = {'APPID': api_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)
        weather = result.json()

        # request = requests.get("https://sinoptik.com.ru/погода-" + city)
        # b = bs4.BeautifulSoup(request.text, "html.parser")
        
        # p3 = b.select('.temperature .p3')
        # weather1 = p3[0].getText()
        # p4 = b.select('.temperature .p4')
        # weather2 = p4[0].getText()
        # p5 = b.select('.temperature .p5')
        # weather3 = p5[0].getText()
        # p6 = b.select('.temperature .p6')
        # weather4 = p6[0].getText()
        # result = ''
        # result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        # result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        # temp = b.select('.rSide .description')
        # weather = temp[0].getText()
        # result = result + weather.strip()

        result = "🌡В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + " °C\n" 
        + "📈Максимальная температура " + str(float(weather['main']['temp_max'])) + " °C\n" 
        + "📉Минимальная температура " + str(float(weather['main']['temp_min'])) + " °C\n" 
        + "💨Скорость ветра " + str(float(weather['wind']['speed'])) + " м/с\n" 
        + "🅿️Давление " + str(float(weather['main']['pressure'])) + " мбар\n" 
        + "💦Влажность " + str(int(weather['main']['humidity'])) + " %\n" 
        + "👀Видимость " + str(weather['visibility']) + "\n" 
        + "📜Описание: " + str(weather['weather'][0]["description"]) + "\n\n"
        return result