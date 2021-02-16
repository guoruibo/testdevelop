class Calcultor:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return ("b不能为除数")
