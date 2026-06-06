import allure
import requests
import unittest

BASE_URL = "http://5.181.109.28:9090/api/v3/"

@allure.feature("Pet")
class TestPet(unittest.TestCase):
    @allure.title("Попытка удалить несуществующего питомца")
    def test_delete_nonexistent_pet(self):
        with allure.step("Отправка запроса на удаление несуществующего питомца"):
            response = requests.delete(url=f"{BASE_URL}/pet/9999")

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текстового содержимого ответа"):
            assert response.text == '{"code":404,"message":"HTTP 404 Not Found"}', \
                "Текст ошибки не совпал с ожидаемым"