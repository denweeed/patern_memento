class Calculator:
    def __init__(self):
        self._total = 0
        self._history = []

    def add(self, value):
        self._total += value
        self._history.append(('+', value))

    def subtract(self, value):
        self._total -= value
        self._history.append(('-', value))

    def undo(self):
        if not self._history:
            return
        op, value = self._history.pop()
        if op == '+':
            self._total -= value
        elif op == '-':
            self._total += value

    def create_memento(self):
        return CalculatorMemento(self._total, self._history)

    def set_memento(self, memento):
        self._total = memento.total
        self._history = memento.history

    @property
    def total(self):
        return self._total


class CalculatorMemento:
    def __init__(self, total, history):
        self.total = total
        self.history = history


# Використання калькулятора з паттерном Memento
calculator = Calculator()
calculator.add(10)
calculator.add(5)
calculator.subtract(3)
print(calculator.total)  # 12

# Зберігання стану калькулятора
memento = calculator.create_memento()

calculator.add(7)
calculator.subtract(2)
print(calculator.total)  # 17

# Відновлення попереднього стану калькулятора
calculator.set_memento(memento)
print(calculator.total)  # 12
