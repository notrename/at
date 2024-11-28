import json

import allure
import pytest

from lib.petshop.utils import PetShopMethods


@allure.epic('Тестирование API')
@allure.feature('Проверка методов PetShop')
@allure.severity('Critical')
class TestPetShop:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.pet_shop = PetShopMethods()

    @allure.story('Проверка метода добавления зверушки')
    def test_add_pet(self):
        with allure.step('Подготовка тестовых данных'):
            body = {
                "name": 'tea',
                "status": 'processed',
                "category_name": 'cat',
            }
        with allure.step('Добавляем зверушку'):
            result = self.pet_shop.add_pet(
                **body,
            )

        status_code = result.get('status_code')
        data = result.get('data')
        with allure.step('Проверка status_code'):
            assert status_code == 200
        with allure.step('Проверка что вернулось тело сообщения'):
            assert body.get('name') == data.get('name')
        with allure.step('Ответ ручки сваггера'):
            allure.attach(
                body=json.dumps(data),
                name='response body',
                attachment_type=allure.attachment_type.JSON
            )

    def test_get_pet_by_id(self):
        result = self.pet_shop.get_pet(pet_id=1)
        body = result.get('data')
        status_code = result.get('status_code')
        assert status_code == 200

    # https://allurereport.org/docs/install-for-windows/
    # irm get.scoop.sh | iex
    # scoop install allure

    # allure serve allure-results