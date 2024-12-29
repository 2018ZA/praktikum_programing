from typing import Optional
from abc import ABC, abstractmethod

# Обработчик
class Handler(ABC):
    """Абстрактный класс обработчика, который определяет метод обработки запроса и поле для хранения следующего обработчика."""

    _next_handler: Optional['Handler'] = None

    def set_next(self, handler: 'Handler'):
        """Устанавливает следующий обработчик в цепочке."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        """Абстрактный метод обработки запроса."""
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# Конкретные обработчики
class ConcreteHandler1(Handler):
    """Первый конкретный обработчик."""

    def handle(self, request):
        """Пытается обработать запрос. Если не удается, передает его дальше по цепочке."""
        if request < 10:
            return f'ConcreteHandler1 обработал запрос {request}'
        else:
            return super().handle(request)

class ConcreteHandler2(Handler):
    """Второй конкретный обработчик."""

    def handle(self, request):
        """Пытается обработать запрос. Если не удается, передает его дальше по цепочке."""
        if 10 <= request < 20:
            return f'ConcreteHandler2 обработал запрос {request}'
        else:
            return super().handle(request)

class ConcreteHandler3(Handler):
    """Третий конкретный обработчик."""

    def handle(self, request):
        """Пытается обработать запрос. Если не удается, передает его дальше по цепочке."""
        if 20 <= request < 30:
            return f'ConcreteHandler3 обработал запрос {request}'
        else:
            return super().handle(request)

class FallbackHandler(Handler):
    """Последний обработчик, который обрабатывает все оставшиеся запросы."""

    def handle(self, request):
        """Обрабатывает любой оставшийся запрос."""
        return f'FallbackHandler обработал запрос {request}'

# Клиентский код
def client_code(handler: Handler):
    """Инициализирует обработку запросов."""
    for i in range(0, 35, 5):
        print(f'Клиент отправил запрос {i}')
        response = handler.handle(i)
        print(response or f'Запрос {i} остался необработанным.\n')

if __name__ == '__main__':
    # Формируем цепочку обработчиков
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    fallback_handler = FallbackHandler()

    handler1.set_next(handler2).set_next(handler3).set_next(fallback_handler)

    # Инициализируем обработку запросов
    client_code(handler1)
