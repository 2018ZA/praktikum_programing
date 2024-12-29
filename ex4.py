from abc import ABC, abstractmethod

# Интерфейс коллеги
class Colleague(ABC):
    """Абстрактный класс коллеги, который зависит от посредника."""

    def __init__(self, mediator=None):
        self.mediator = mediator

    @abstractmethod
    def receive(self, message):
        """Получает сообщение от посредника."""
        pass

    @abstractmethod
    def send(self, message):
        """Отправляет сообщение посреднику."""
        pass

# Коллеги
class Colleague1(Colleague):
    """Первый коллега."""

    def receive(self, message):
        print(f"Colleague1 получил сообщение: {message}")

    def send(self, message):
        print(f"Colleague1 отправляет сообщение: {message}")
        self.mediator.notify(message, self)

class Colleague2(Colleague):
    """Второй коллега."""

    def receive(self, message):
        print(f"Colleague2 получил сообщение: {message}")

    def send(self, message):
        print(f"Colleague2 отправляет сообщение: {message}")
        self.mediator.notify(message, self)

# Интерфейс посредника
class Mediator(ABC):
    """Абстрактный класс посредника, который координирует взаимодействие коллег."""

    @abstractmethod
    def notify(self, message, sender: Colleague):
        """Уведомляет других коллег о сообщении."""
        pass

# Посредник
class MediatorImpl(Mediator):
    """Реализация посредника."""

    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague: Colleague):
        """Добавляет нового коллегу в список."""
        self.colleagues.append(colleague)
        colleague.mediator = self

    def notify(self, message, sender: Colleague):
        """Уведомляет других коллег о сообщении, кроме отправителя."""
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive(message)

# Клиентский код
def client_code():
    """Демонстрирует работу паттерна Посредник."""
    mediator = MediatorImpl()

    colleague1 = Colleague1()
    colleague2 = Colleague2()

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)

    colleague1.send("Привет!")
    colleague2.send("Здравствуйте!")

if __name__ == "__main__":
    client_code()
