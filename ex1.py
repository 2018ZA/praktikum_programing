from abc import ABC, abstractmethod

# Базовый класс продукта
class Product:
    """Базовый класс продукта."""

    def operation(self):
        """Операция, которую должен выполнять продукт."""
        raise NotImplementedError("Метод должен быть переопределен в классе")


# Продукты
class ProductA(Product):
    """Продукт A."""

    def operation(self):
        """Реализация операции для продукта A."""
        return "продукт A"


class ProductB(Product):
    """Продукт B."""

    def operation(self):
        """Реализация операции для продукта B."""
        return "продукт B"


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


# Создатели
class CreatorA(Creator):
    """Создатель A."""

    def factory_method(self):
        """Создание продукта A."""
        return ProductA()


class CreatorB(Creator):
    """Создатель B."""

    def factory_method(self):
        """Создание продукта B."""
        return ProductB()


# Демонстрация работы клиента с фабрикой
def client_code(creator: Creator):
    """Демонстрация работы клиента с фабрикой."""
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    print("Пример работы фабрики с продуктом A:")
    client_code(CreatorA())

    print("\nПример работы фабрики с продуктом B:")
    client_code(CreatorB())



