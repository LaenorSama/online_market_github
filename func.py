import random
import pytest
import time

def lucky_step(chance: float = 0.6) -> None:
    """
    С вероятностью `chance` ломает тест.
    Возможные исходы с весами:
      - Failed (pytest.fail) 50%
      - Broken (ValueError, TypeError, KeyError) 30%
      - Skipped (pytest.skip) 20%
    Сообщения выбираются случайно из расширенных списков.
    """
    if not 0 <= chance <= 1:
        raise ValueError("Параметр 'chance' должен быть в диапазоне от 0 до 1")

    if random.random() < chance:
        outcome = random.choices(
            ["failed", "broken", "skipped"],
            weights=[50, 30, 20],
            k=1
        )[0]

        # Расширенные осмысленные сообщения
        failed_messages = [
            "Failed: условие в тесте не выполнено",
            "AssertionError: проверка данных не прошла",
            "Тест упал: обнаружено несоответствие результата ожидаемому",
            "Ошибка проверки: результат не совпадает с эталоном",
            "Failed: проверка элементов страницы не удалась",
            "AssertionError: значение переменной не соответствует ожиданиям"
        ]

        broken_messages = [
            "Broken: ValueError — некорректное значение в тесте",
            "Broken: TypeError — тип данных не совпадает с ожидаемым",
            "Broken: KeyError — ключ не найден в словаре",
            "Broken: Ошибка выполнения шага теста",
            "Broken: Необработанное исключение во время теста",
            "Broken: runtime exception, тест не удалось корректно завершить"
        ]

        skipped_messages = [
            "Skipped: условие для выполнения шага не выполнено",
            "Пропущено: тестовый шаг был проигнорирован",
            "Skipped: зависимость теста отсутствует или не активна",
            "Пропуск шага: данные для проверки недоступны",
            "Skipped: выполнение шага временно отключено",
            "Пропущено: тест не применим для текущей конфигурации"
        ]

        if outcome == "failed":
            pytest.fail(random.choice(failed_messages))
        elif outcome == "broken":
            error_type = random.choice([ValueError, TypeError, KeyError])
            raise error_type(random.choice(broken_messages))
        elif outcome == "skipped":
            pytest.skip(random.choice(skipped_messages))

def lucky_sleep(min_seconds: int = 10, max_seconds: int = 100) -> None:
    """
    Задержка выполнения теста на случайное время в диапазоне [min_seconds, max_seconds].
    По умолчанию от 10 до 100 секунд.
    """
    if min_seconds < 0 or max_seconds < min_seconds:
        raise ValueError("Некорректные параметры задержки")

    delay = random.randint(min_seconds, max_seconds)
    print(f"[lucky_sleep] Тест ждет {delay} секунд...")
    time.sleep(delay)