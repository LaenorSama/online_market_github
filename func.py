import random

def lucky_step(chance=0.1):
    """
    С вероятностью `chance` выбрасывает случайную ошибку из списка.

    :param chance: вероятность ошибки (0.0–1.0), по умолчанию 0.1 (10%)
    """

    ERROR_TYPES = [IndexError, ValueError, TypeError, KeyError]
    if random.random() < chance:  # 10% шанс на ошибку
        error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
        raise error_type(f'Случайная ошибка: {error_type.__name__}')
