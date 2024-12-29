from abc import ABC, abstractmethod

# Интерфейс элемента
class Element(ABC):
    """Абстрактный класс элемента, который принимает посетителя."""

    @abstractmethod
    def accept(self, visitor):
        """Принимает посетителя."""
        pass

# Элементы
class ElementA(Element):
    """Первый элемент."""

    def accept(self, visitor):
        """Принимает посетителя и вызывает его метод visit_element_a."""
        visitor.visit_element_a(self)

    def operation_a(self):
        """Операция, характерная для элемента A."""
        return "Элемент A"

class ElementB(Element):
    """Второй элемент."""

    def accept(self, visitor):
        """Принимает посетителя и вызывает его метод visit_element_b."""
        visitor.visit_element_b(self)

    def operation_b(self):
        """Операция, характерная для элемента B."""
        return "Элемент B"

# Интерфейс посетителя
class Visitor(ABC):
    """Абстрактный класс посетителя, который определяет методы для посещения различных типов элементов."""

    @abstractmethod
    def visit_element_a(self, element):
        """Посещение элемента A."""
        pass

    @abstractmethod
    def visit_element_b(self, element):
        """Посещение элемента B."""
        pass

# Посетители
class Visitor1(Visitor):
    """Первый посетитель."""

    def visit_element_a(self, element):
        """Выполняет операцию с элементом A."""
        print(f'{self.__class__.__name__} посещает {element.operation_a()}')

    def visit_element_b(self, element):
        """Выполняет операцию с элементом B."""
        print(f'{self.__class__.__name__} посещает {element.operation_b()}')

class Visitor2(Visitor):
    """Второй посетитель."""

    def visit_element_a(self, element):
        """Выполняет другую операцию с элементом A."""
        print(f'{self.__class__.__name__} посещает {element.operation_a()}')

    def visit_element_b(self, element):
        """Выполняет другую операцию с элементом B."""
        print(f'{self.__class__.__name__} посещает {element.operation_b()}')

# Клиентский код
def client_code(elements, visitors):
    """Демонстрирует работу паттерна Посетитель."""
    for element in elements:
        for visitor in visitors:
            element.accept(visitor)

if __name__ == '__main__':
    elements = [ElementA(), ElementB()]
    visitors = [Visitor1(), Visitor2()]

    client_code(elements, visitors)
