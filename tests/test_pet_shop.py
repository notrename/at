import pytest

from lib.petshop.utils import PetShopMethods


class TestPetShop:
    PetShop = PetShopMethods()

    @pytest.mark.parametrize(
        'name, category_name',
        [
            ('Asteroid Destroyer', 'cat'),
            (454556, 'dog'),
            ('Felix', 'cat'),
        ],
        # ids=['cat__w Asteroid Destroyer', 'dog__w Bruce', 'cat__w Felix']
    )
    def test_add_pet(self, name, category_name):
        body = {
            "name": name,
            "status": 'processed',
            "category_name": category_name,
        }
        result = self.PetShop.add_pet(
            **body,
        )
        status_code = result.get('status_code')
        data = result.get('data')
        assert status_code == 200
        assert body.get('name') == data.get('name')

    @pytest.mark.parametrize('pet_id', [112, 1337, 952, 1])
    def test_get_pet_by_id(self, pet_id):
        result = self.PetShop.get_pet(pet_id=pet_id)
        body = result.get('data')
        status_code = result.get('status_code')
        assert status_code == 200

    @pytest.mark.skip('Не доработана функция ...')
    def test_negative(self):
        assert 3 == 4

    @pytest.mark.xfail()
    def test_xfail(self):
        assert 3 < 4
