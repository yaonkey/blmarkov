from datetime import datetime

class Generator:
    """
    Генератор случайной последовательности.
    Реализован на основе метода срединных квадратов.
    """
    initial_number: int

    def __init__(self, initial_number=None):
        self.initial_number = initial_number
        # только в случае, когда входное значение отсутствует, сами генерируем первое случайное число
        if self.initial_number is None:
            self.initial_number = self._get_initial_number()
        if not isinstance(self.initial_number, int):
            raise ValueError("Входное значение не является числом!")

    def start(self):
        while True:
            square_str = str(self.initial_number ** 2)
            start_index = len(square_str) // 4
            finish_index = start_index + 1 if len(square_str) % 2 else start_index
            self.initial_number = int(square_str[start_index:-finish_index])
            yield self.initial_number

    def _get_initial_number(self):
        """
        Возвращает количество миллисекунд в текущей дате для построения случайных чисел
        """
        now = datetime.now()
        return now.microsecond
