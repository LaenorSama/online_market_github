import allure
import pytest
from func import *

@allure.id("2306")
@allure.title("Адаптивность на мобильных устройствах")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("UX тестирование")
def test_mobile_adaptive():
    lucky_sleep()
    lucky_step()

@allure.id("2308")
@allure.title("Масштабирование изображений товаров")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("UX тестирование")
def test_scale():
    lucky_sleep()
    lucky_step()

@allure.id("2309")
@allure.title("Навигация по сайту (footer)")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("UX тестирование")
def test_footer():
    lucky_sleep()
    lucky_step()

@allure.id("2310")
@allure.title("Навигация по сайту (header)")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("UX тестирование")
def test_header():
    lucky_sleep()
    lucky_step()

@allure.id("2302")
@allure.title("Навигация по сайту (menu)")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("UX тестирование")
def test_menu():
    lucky_sleep()
    lucky_step()

@allure.id("2312")
@allure.title("Временя отклика сервера при оформлении заказа")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("Нагрузочное тестирование")
def test_order_time():
    lucky_sleep()
    lucky_step()

@allure.id("2281")
@allure.title("Одновременная работа 1000 пользователей")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("Нагрузочное тестирование")
def test_many_users():
    lucky_sleep()
    lucky_step()

@allure.id("2280")
@allure.title("Открытие страницы каталога с 10 000 товаров")
@allure.label("owner", "Alex")
@allure.epic("Нагрузочное и UX тестирование")
@allure.feature("Нагрузочное тестирование")
def test_many_items():
    lucky_sleep()
    lucky_step()

@allure.id("2274")
@allure.title("Выбор транспортной компании по умолчанию")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Доставка")
def test_default_delivery():
    lucky_sleep()
    lucky_step()

@allure.id("2313")
@allure.title("Отображение планируемой даты доставки")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Доставка")
def test_show_delivery_date():
    lucky_sleep()
    lucky_step()

@allure.id("2273")
@allure.title("Оформление заказа без выбора доставки")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Доставка")
def test_order_without_delivery():
    lucky_sleep()
    lucky_step()

@allure.id("2279")
@allure.title("Отображение заказа в истории")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа", "Просмотр и редактирование профиля")
@allure.story("История заказов")
def test_show_order_in_history():
    lucky_sleep()
    lucky_step()

@allure.id("2263")
@allure.title("Оплата картой с валидными данными")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Оплата")
def test_pay_with_valid_card():
    lucky_sleep()
    lucky_step()

@allure.id("2264")
@allure.title("Отмена оплаты на этапе ввода данных")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Оплата")
def test_cancel_pay():
    lucky_sleep()
    lucky_step()

@allure.id("2266")
@allure.title("Ошибка оплаты (неверная карта)")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Оплата")
def test_error_pay_wrong_card():
    lucky_sleep()
    lucky_step()

@allure.id("2265")
@allure.title("Ошибка оплаты (недостаточно средств)")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Оплата")
def test_error_pay_insufficient_funds():
    lucky_sleep()
    lucky_step()

@allure.id("2262")
@allure.title("Редирект после успешной оплаты")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа")
@allure.story("Оплата")
def test_redirect_after_successful_pay():
    lucky_sleep()
    lucky_step()

@allure.id("2311")
@allure.title("Отображение заказа в текущих заказах")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Оформление заказа", "Просмотр и редактирование профиля")
@allure.story("Текущие заказы")
def test_show_order_in_current_orders():
    lucky_sleep()
    lucky_step()

@allure.id("2272")
@allure.title("Изменение статуса заказа")
@allure.label("owner", "Alex")
@allure.epic("Личный кабинет")
@allure.feature("Просмотр и редактирование профиля")
@allure.story("Текущие заказы")
def test_change_order_status():
    lucky_sleep()
    lucky_step()

@allure.id("2258")
@allure.title("Наличие минимум 3 фотографий у товара")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_three_product_images():
    lucky_sleep()
    lucky_step()

@allure.id("2249")
@allure.title("Наличие описания")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_description():
    lucky_sleep()
    lucky_step()

@allure.id("2261")
@allure.title("Отображение альтернативных товаров")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_show_alternative_items():
    lucky_sleep()
    lucky_step()

@allure.id("2259")
@allure.title("Отображение наличия на складе")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_stock_availability():
    lucky_sleep()
    lucky_step()

@allure.id("2303")
@allure.title("Отображение технических характеристик")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_show_specification():
    lucky_sleep()
    lucky_step()

@allure.id("2254")
@allure.title("Отображение цены (в рублях)")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Список товаров")
@allure.story("Страница товара")
def test_show_price_in_roubles():
    lucky_sleep()
    lucky_step()

@allure.id("2269")
@allure.title("CSRF при оформлении заказа")
@allure.label("owner", "Alex")
@allure.epic("Безопасность")
@allure.feature("Тесты безопасности")
def test_csrf_at_checkout():
    lucky_sleep()
    lucky_step()

@allure.id("2282")
@allure.title("SQL инъекции при регистрации и авторизации")
@allure.label("owner", "Alex")
@allure.epic("Безопасность")
@allure.feature("Тесты безопасности")
def test_sql_injection():
    lucky_sleep()
    lucky_step()

@allure.id("2267")
@allure.title("XSS инъекции в профиле, описаниях товара")
@allure.label("owner", "Alex")
@allure.epic("Безопасность")
@allure.feature("Тесты безопасности")
def test_xss_sql_injection():
    lucky_sleep()
    lucky_step()

@allure.id("2284")
@allure.title("Защита личных данных (доступ без авторизации)")
@allure.label("owner", "Alex")
@allure.epic("Безопасность")
@allure.feature("Тесты безопасности")
def test_personal_data_protection():
    lucky_sleep()
    lucky_step()

@allure.id("2283")
@allure.title("Сессии и куки (перехват, подмена)")
@allure.label("owner", "Alex")
@allure.epic("Безопасность")
@allure.feature("Тесты безопасности")
def test_spoofing_intercepting_cookies():
    lucky_sleep()
    lucky_step()

@allure.id("2248")
@allure.title("Одновременная работа нескольких фильтров")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_many_filters():
    lucky_sleep()
    lucky_step()

@allure.id("2247")
@allure.title("Сброс фильтров")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_resetting_filters():
    lucky_sleep()
    lucky_step()

@allure.id("2256")
@allure.title("Фильтрация по категориям")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_filter_by_category():
    lucky_sleep()
    lucky_step()

@allure.id("2317")
@allure.title("Фильтрация по наличию на складе")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_filter_by_availability():
    lucky_sleep()
    lucky_step()

@allure.id("2257")
@allure.title("Фильтрация по цене")
@allure.label("owner", "Alex")
@allure.epic("Поиск и каталог товаров")
@allure.feature("Фильтры")
@allure.story("Фильтрация по категориям")
def test_filter_by_price():
    lucky_sleep()
    lucky_step()

