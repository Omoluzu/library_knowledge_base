from typing import Any, Optional, TypeVar
import asyncio
from types import TracebackType

_T = TypeVar('_T')


class QEventLoop(asyncio.AbstractEventLoop):
    """QEventLoop - интеграция Qt и asyncio"""

    def __init__(self, parent: Optional[Any] = None) -> None:
        """Инициализация с опциональным родительским Qt объектом"""
        ...

    # Методы контекстного менеджера (для работы with)
    def __enter__(self) -> 'QEventLoop':
        """Вход в контекстный менеджер"""
        ...

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> Optional[bool]:
        """Выход из контекстного менеджера"""
        ...

    # Основные методы цикла событий
    def run_forever(self) -> None:
        """Запуск цикла событий навсегда"""
        ...

    # def run_until_complete(
    #         self, future: Union[asyncio.Future[_T], Coroutine[Any, Any, _T]]
    # ) -> _T:
    #     """Запуск до завершения future"""
    #     ...

    def stop(self) -> None:
        """Остановка цикла событий"""
        ...

    def close(self) -> None:
        """Закрытие цикла событий"""
        ...

    def is_closed(self) -> bool:
        """Проверка, закрыт ли цикл"""
        ...

    def is_running(self) -> bool:
        """Проверка, запущен ли цикл"""
        ...

    # def call_soon(
    #         self, callback: Callable[..., Any],
    #         *args: Any, context: Optional[Any] = None
    # ) -> asyncio.Handle:
    #     """Вызов callback при первой возможности"""
    #     ...

    # def call_later(
    #         self, delay: float, callback: Callable[..., Any],
    #         *args: Any, context: Optional[Any] = None
    # ) -> asyncio.TimerHandle:
    #     """Вызов callback через delay секунд"""
    #     ...

    # def call_at(
    #         self, when: float, callback: Callable[..., Any],
    #         *args: Any, context: Optional[Any] = None
    # ) -> asyncio.TimerHandle:
    #     """Вызов callback в абсолютное время when"""
    #     ...

    # def create_task(
    #         self, coro: Coroutine[Any, Any, _T], *,
    #         name: Optional[str] = None, context: Optional[Any] = None
    # ) -> asyncio.Task[_T]:
    #     """Создание задачи из корутины"""
    #     ...

    def get_debug(self) -> bool:
        """Получение флага отладки"""
        ...

    def set_debug(self, enabled: bool) -> None:
        """Установка флага отладки"""
        ...


# Для обратной совместимости и явного экспорта
__all__ = ("QEventLoop", )
