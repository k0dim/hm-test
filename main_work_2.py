import requests
from loguru import logger

logger.add("log.log", format="{time} {level} {message}", level="INFO")


class Yandex:
    def __init__(self, yandex_token):
        self.url_api = 'https://cloud-api.yandex.net/v1/disk/'
        self.headers = {
            'Authorization': f'OAuth {yandex_token}', 
            'Content-Type': 'application/json', 
            'Accept': 'application/json'
        }
        self.response = requests.get(self.url_api, headers= self.headers)
        logger.info(f'{self.__init__} => {self.response.status_code}')

    def creat_folder(self, name_floader=''):  # Создать папку 
        self.name_floader = name_floader
        url = f'{self.url_api}resources'
        params = {'path': self.name_floader}
        self.response = requests.put(url, params = params, headers = self.headers)
        logger.info(f'{self.creat_folder} => {self.response.status_code}')
        return self.response.status_code

    def delete_folder(self, name_floader=''):  # Удалить папку
        self.name_floader = name_floader
        url = f'{self.url_api}resources'
        params = {'path': self.name_floader}
        self.response = requests.delete(url, params=params, headers=self.headers)
        logger.info(f'{self.delete_folder} => {self.response.status_code}')
        return self.response.status_code

def get_token():
    # token = input('Укажите токен - ')
    token = 'y0_AgAAAAATf-PhAADLWwAAAADSgNHj8uipcU7YS6-VWQ7c07h0uYvj1bY'
    return token

def name_folder():
    name = input('Укажите имя папки - ')
    return name

if __name__ == "__main__":
    token=get_token()
    name=name_folder()
    ya = Yandex(token)
    res_code = ya.delete_folder(name)
    if res_code == 201:
        print(f'Папка "{name}" успешно создана !')
    else:
        print(f'Папка "{name}" не создана !')