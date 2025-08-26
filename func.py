import random
import pytest

def lucky_step(chance: float = 0.5) -> None:
    """
    С вероятностью `chance` ломает тест.
    Возможные исходы с весами:
      - Failed (AssertionError) 50%
      - Broken (ValueError, TypeError, KeyError) 30%
      - Skipped (pytest.skip) 20%
    """
    if not 0 <= chance <= 1:
        raise ValueError("Параметр 'chance' должен быть в диапазоне от 0 до 1")

    if random.random() < chance:
        outcome = random.choices(
            ["failed", "broken", "skipped"],
            weights=[50, 30, 20],
            k=1
        )[0]

        if outcome == "failed":
            pytest.fail("Случайная ошибка: тест упал (failed)")

        elif outcome == "broken":
            error_types = [ValueError, TypeError, KeyError]
            error_type = random.choice(error_types)
            raise error_type(f"Случайная ошибка: тест сломался ({error_type.__name__})")

        elif outcome == "skipped":
            pytest.skip("Случайная ошибка: тест пропущен")
