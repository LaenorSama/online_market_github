import random
import pytest

def lucky_step(chance: float = 0.6) -> None:
    """
    С вероятностью `chance` ломает тест.
    Возможные исходы с весами:
      - Failed (pytest.fail) 50%
      - Broken (ValueError, TypeError, KeyError) 30%
      - Skipped (pytest.skip) 20%
    Сообщения выбираются случайно из предопределенных списков.
    """
    if not 0 <= chance <= 1:
        raise ValueError("Параметр 'chance' должен быть в диапазоне от 0 до 1")

    if random.random() < chance:
        # Определяем исход с весами
        outcome = random.choices(
            ["failed", "broken", "skipped"],
            weights=[50, 30, 20],
            k=1
        )[0]

        # Списки сообщений
        failed_messages = [
            "Assertion провалился: тест упал",
            "Нарушена проверка условий",
            "Failed: случайная ошибка в тесте"
        ]
        broken_messages = [
            "ValueError: что-то пошло не так",
            "TypeError: неправильный тип данных",
            "KeyError: ключ не найден"
        ]
        skipped_messages = [
            "Пропущено: тест не был выполнен",
            "Skipped: условие не выполнено",
            "Пропуск шага теста случайно"
        ]

        # Выбор сообщения и вызов соответствующей ошибки/skip
        if outcome == "failed":
            pytest.fail(random.choice(failed_messages))

        elif outcome == "broken":
            error_type = random.choice([ValueError, TypeError, KeyError])
            raise error_type(random.choice(broken_messages))

        elif outcome == "skipped":
            pytest.skip(random.choice(skipped_messages))
