class Calculation:
    def __init__(self, operation):
        self.operation = operation
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(str(number[0:3]))

    def flip(self):
        print("PRE FLIP")
        print(self.numbers)        
        numbers = []
        number_count = len(self.numbers)
        for i in range(0, 3):
            number = ""
            for j in range(0, number_count):
                number += self.numbers[j][i]
            numbers.append(number[::-1])
        self.numbers = numbers


    def compute(self):
        print("PRE COMPUTE")
        print(self.numbers)
        total = int(self.numbers[0])
        for i in range(1, len(self.numbers)):
            number = self.numbers[i]
            if self.operation == "+":
                total += int(number)
            elif self.operation == "*":
                total *= int(number)

        return total
    

    def flip_and_compute(self):
        self.flip()
        return self.compute()