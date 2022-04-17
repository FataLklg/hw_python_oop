from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, List, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    """Константа выводимого сообщения"""
    MESSAGE: str = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration:.3f} ч.; '
        'Дистанция: {distance:.3f} км; '
        'Ср. скорость: {speed:.3f} км/ч; '
        'Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self):
        return self.MESSAGE.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int  # Количество совершённых действий
    duration: float  # Длительность тренировки в часах
    weight: float  # Вес спортсмена в кг.

    LEN_STEP: ClassVar[float] = 0.65  # Длинна шага
    M_IN_KM: ClassVar[int] = 1000  # Константа для переаода из м. в км.
    COEFF_H_TO_MIN: ClassVar[int] = 60  # Константа для перевода ч. в м.

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError(
            f'Количество затраченых калорий необходимо'
            f'определить в {(type(self).__name__)}'
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )


class Running(Training):
    """Тренировка: бег."""
    """Константы для подсчёта калорий"""
    COEFF_CALORIE_1: ClassVar[int] = 18
    COEFF_CALORIE_2: ClassVar[int] = 20

    def get_spent_calories(self) -> float:
        return (
            (self.COEFF_CALORIE_1 * self.get_mean_speed()
             - self.COEFF_CALORIE_2) * self.weight / self.M_IN_KM
            * (self.duration * self.COEFF_H_TO_MIN)
        )


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float  # Рост спортсмена в см.
    """Константы для подсчёта калорий"""
    COEFF_CALORIE_1: ClassVar[float] = 0.035
    COEFF_CALORIE_2: ClassVar[float] = 0.029

    def get_spent_calories(self) -> float:
        return (
            (self.COEFF_CALORIE_1 * self.weight
             + (self.get_distance()**2 // self.height)
             * self.COEFF_CALORIE_2 * self.weight)
            * (self.duration * self.COEFF_H_TO_MIN)
        )


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    length_pool: float  # Длина бассейна в метрах
    count_pool: float  # Сколько раз спортсмен переплыл бассейн

    LEN_STEP: ClassVar[float] = 1.38  # Длина одного гребка
    """Константы для подсчёта калорий"""
    COEFF_CALORIE_1: ClassVar[float] = 1.1
    COEFF_CALORIE_2: ClassVar[int] = 2

    def get_mean_speed(self) -> float:
        return (
            self.length_pool * self.count_pool
            / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        return (
            (self.get_mean_speed() + self.COEFF_CALORIE_1)
            * self.COEFF_CALORIE_2 * self.weight
        )


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_dict: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in training_dict:
        raise KeyError(f'Тип {workout_type} отсутствует в словаре')
    return training_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
