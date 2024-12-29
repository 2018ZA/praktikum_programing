from abc import ABC, abstractmethod

# Базовый класс продукта
class Product:
    """Базовый класс продукта."""

    def operation(self):
        """Операция, которую должен выполнять продукт."""
        raise NotImplementedError("Метод должен быть переопределен в конкретном классе")


# Конкретные продукты
class ConcreteProductA(Product):
    """Конкретный продукт А."""

    def operation(self):
        """Реализация операции для продукта А."""
        return "Конкретный продукт A"


class ConcreteProductB(Product):
    """Конкретный продукт B."""

    def operation(self):
        """Реализация операции для продукта B."""
        return "Конкретный продукт B"


# Абстрактный класс создателя
class Creator(ABC):
    """Абстрактный класс создателя."""

    @abstractmethod
    def factory_method(self):
        """Абстрактный фабричный метод."""
        pass

    def some_operation(self):
        """
        Операция, которая использует фабричный метод для получения продукта.
        
        :return: строка с результатом вызова операции над продуктом.
        """
        product = self.factory_method()
        result = f"Creator: Вернул {product.operation()}"
        return result


# Конкретные создатели
class ConcreteCreatorA(Creator):
    """Конкретный создатель А."""

    def factory_method(self):
        """Создание конкретного продукта А."""
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """Конкретный создатель B."""

    def factory_method(self):
        """Создание конкретного продукта B."""
        return ConcreteProductB()


# Демонстрация работы клиента с фабрикой
def client_code(creator: Creator):
    """Демонстрация работы клиента с фабрикой."""
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    print("Пример работы фабрики с конкретным продуктом A:")
    client_code(ConcreteCreatorA())

    print("\nПример работы фабрики с конкретным продуктом B:")
    client_code(ConcreteCreatorB())



