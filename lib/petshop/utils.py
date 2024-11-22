import allure
import requests
import json
from random import randint


class PetShopMethods:
    def __init__(self):
        pass
    URL = 'https://petstore.swagger.io/v2/pet/'

    # @JsonWriter.write_to_file
    # @StatusChecker.success_check
    def get_pet(self, pet_id: int) -> dict | str:
        url = f'{self.URL}{pet_id}'
        resp = requests.get(url=url)
        if resp.status_code != 200:
            return {'status_code': resp.status_code, 'data': resp.json()}
        return {'status_code': resp.status_code, 'data': resp.json()}

    def add_pet(
        self,
        name: str,
        status: str,
        category_name: str,
    ) -> int | dict:
        """
        Для добавления зверушки в систему
        :param name: Имя зверушки
        :param status: Статус
        :param category_name: Название категории
        :return: response.status_code | {'status_code': response.status_code, 'data': response.json()}
        """
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "id": randint(0, 100500),
            "category": {
                "id": randint(0, 100500),
                "name": category_name,
            },
            "name": name,
            "status": status
        }
        resp = requests.post(url=self.URL, data=json.dumps(body), headers=headers)
        if resp.status_code != 200:
            return resp.status_code
        return {'status_code': resp.status_code, 'data': resp.json()}

    def delete_pet(self, pet_id: int) -> int:
        resp = requests.delete(url=f'{self.URL}{pet_id}')
        return resp.status_code
