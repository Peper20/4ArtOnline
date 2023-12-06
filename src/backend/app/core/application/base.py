from abc import ABC, abstractmethod
from typing import Any




class BaseInteractor(ABC):
    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError
