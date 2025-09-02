import allure
import pytest
from func import *


@pytest.mark.parametrize(
    "category, price_filter, discount",
    [
        ("Электроника", "1000–5000", True),
        ("Одежда", "до 1000", False),
        ("Игрушки", ">5000", True),
    ]
)
@allure.id("2248")
@allure.title("Одновременная работа нескольких фильтров")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_many_filters(category, price_filter, discount):
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("Открыть панель фильтров"):
        pass
    with allure.step("Выбрать категорию товаров из таблицы параметров"):
        pass
    with allure.step("Выбрать диапазон цен из таблицы параметров"):
        pass
    with allure.step("Выбрать наличие скидки из таблицы параметров"):
        pass
    with allure.step("Нажать Показать товары"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются товары подходящие под фильтры"):
                lucky_step()
                pass

@pytest.mark.parametrize(
    "category",
    [
        "Электроника", "Одежда", "Игрушки", "Бытовая техника"
    ]
)
@allure.id("2256")
@allure.title("Фильтрация по категориям")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_filter_by_category(category):
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("Открыть панель фильтров"):
        pass
    with allure.step("Выбрать категорию товаров из таблицы параметров"):
        pass
    with allure.step("Нажать Показать товары"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются товары подходящие под фильтр"):
                lucky_step()
                pass

@pytest.mark.parametrize(
    "stock_status",
    [
        "в наличии",
        "нет в наличии",
        "мало",
        "под заказ"
    ]
)
@allure.id("2317")
@allure.title("Фильтрация по наличию на складе")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_filter_by_availability(stock_status):
    with allure.step("Перейти в каталог товаров"):
        pass
    with allure.step("Открыть панель фильтров"):
        pass
    with allure.step("Выбрать Доступность на складе из таблицы параметров"):
        pass
    with allure.step("Нажать Показать товары"):
        with allure.step("Expected Result"):
            with allure.step("Отображаются товары подходящие под фильтр"):
                pass
    with allure.step("Перейти в систему складского учета"):
        pass
    with allure.step("Найти в системе учета товары которые отобразились на предыдущем шаге"):
        pass
    with allure.step("В системе складского учета проверить их наличие на складе"):
        with allure.step("Expected Result"):
            with allure.step("Наличие товаров на сайте соответствует наличию в системе складского учета"):
                lucky_step()
                pass

