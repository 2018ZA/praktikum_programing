from abc import ABC, abstractmethod

# Интерфейс реализации
class Implementor(ABC):
    """Интерфейс реализации, который определяет методы, используемые в абстракциях."""

    @abstractmethod
    def operation_implementation(self):
        pass

# Реализации
class ImplementorA(Implementor):
    """Первая реализация интерфейса Implementor."""

    def operation_implementation(self):
        return "Реализация A"

class ImplementorB(Implementor):
    """Вторая реализация интерфейса Implementor."""

    def operation_implementation(self):
        return "Реализация B"

# Абстракция
class Abstraction:
    """Основная сущность, которая определяет интерфейс для работы с объектами реализации."""

    def __init__(self, implementor: Implementor):
        self.implementor = implementor

    def operation(self):
        return self.implementor.operation_implementation()

# Расширенная абстракция
class RefinedAbstraction(Abstraction):
    """Реализация абстракции, которая добавляет дополнительные функциональные возможности."""

    def another_operation(self):
        return f"Расширенное поведение: {self.implementor.operation_implementation()}"

# Клиентский код
def client_code(abstraction: Abstraction):
    """Демонстрирует работу клиента с объектом Абстракцией."""
    print(f"Абстракция: {abstraction.operation()}")

if __name__ == "__main__":
    # Пример использования первой реализации
    implementor_a = ImplementorA()
    abstraction = Abstraction(implementor_a)
    client_code(abstraction)

    # Пример использования второй реализации
    implementor_b = ImplementorB()
    refined_abstraction = RefinedAbstraction(implementor_b)
    client_code(refined_abstraction)
    print(f"Расширенные возможности: {refined_abstraction.another_operation()}")

