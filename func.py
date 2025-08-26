import random
import pytest


def lucky_step(chance: float = 0.3) -> None:
    """
    С вероятностью `chance` ломает тест.
    Возможные исходы:
      - Failed (AssertionError)
      - Broken (любая runtime-ошибка)
      - Skipped (pytest.skip)
    """
    if not 0 <= chance <= 1:
        raise ValueError("Параметр 'chance' должен быть в диапазоне от 0 до 1")

    if random.random() < chance:
        outcome = random.choice(["failed", "broken", "skipped"])

        if outcome == "failed":
            raise AssertionError("Случайная ошибка: тест упал (failed)")

        elif outcome == "broken":
            error_types = [ValueError, TypeError, KeyError]
            error_type = random.choice(error_types)
            raise error_type(f"Случайная ошибка: тест сломался ({error_type.__name__})")

        elif outcome == "skipped":
            pytest.skip("Случайная ошибка: тест пропущен")
