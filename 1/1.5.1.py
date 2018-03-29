class MoneyBox:
    def __init__(self, capacity):
        self.cur = 0
        self.capacity = capacity
# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.cur + v <= self.capacity:
            return True
        else:
            return False
# True, если можно добавить v монет, False иначе

    def add(self, v):
        self.cur += v
        # положить v монет в копилку