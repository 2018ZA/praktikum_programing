from abc import ABC, abstractmethod

# Интерфейс реализации
class Implementor(ABC):
    """Интерфейс реализации, который определяет методы, используемые в абстракциях."""

    @abstractmethod
    def operation_implementation(self):
        pass

# Конкретная реализация
class ConcreteImplementorA(Implementor):
    """Первая конкретная реализация интерфейса Implementor."""

    def operation_implementation(self):
        return "Конкретная реализация A"

# Вторая конкретная реализация
class ConcreteImplementorB(Implementor):
    """Вторая конкретная реализация интерфейса Implementor."""

    def operation_implementation(self):
        return "Конкретная реализация B"

# Абстракция
class Abstraction:
    """Основная сущность, которая определяет интерфейс для работы с объектами реализации."""

    def __init__(self, implementor: Implementor):
        self.implementor = implementor

    def operation(self):
        return self.implementor.operation_implementation()

# Рефинированная абстракция
class RefinedAbstraction(Abstraction):
    """Конкретная реализация абстракции, которая добавляет дополнительные функциональные возможности."""

    def another_operation(self):
        return f"Расширенное поведение: {self.implementor.operation_implementation()}"

# Клиентский код
def client_code(abstraction: Abstraction):
    """Демонстрирует работу клиента с объектом Абстракцией."""
    print(f"Абстракция: {abstraction.operation()}")

if __name__ == "__main__":
    # Пример использования первой конкретной реализации
    concrete_implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_implementor_a)
    client_code(abstraction)

    # Пример использования второй конкретной реализации
    concrete_implementor_b = ConcreteImplementorB()
    refined_abstraction = RefinedAbstraction(concrete_implementor_b)
    client_code(refined_abstraction)
    print(f"Расширенные возможности: {refined_abstraction.another_operation()}")
