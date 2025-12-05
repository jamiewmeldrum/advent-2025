class NumberRange:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def in_range(self, number):
        return number >= self.start and number < self.end