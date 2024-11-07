
from ..TimelineEntry import TimelineEntry
from abc import ABC, abstractmethod
from .._typeAliases import T

class TimelineCallback(ABC):
    """
    异步接口中的回调接口。 如果LIB使用者选择异步时使用callback，则需要实现TimelineCallback接口。如果使用Future接口，则不需要实现TimelineCallback接口。
    """
    
    @abstractmethod
    def onCompleted(self, timelineId: str, request: T, timelineEntry: TimelineEntry) -> None: ...

    @abstractmethod
    def onFailed(self, timelineId: str, request: T, ex: Exception) -> None: ...

    @abstractmethod
    def __call__(self, *args, **kwargs) -> None: ...