
from .common.TimelineCallback import TimelineCallback
from .TimelineEntry import TimelineEntry
from .common.TimelineException import TimelineException
from .common.TimelineExceptionType import TimelineExceptionType
from .message.IMessage import IMessage
from .store.IStore import IStore
from .javaInterface._string import JavaString
from concurrent.futures import Future
from collections.abc import Iterator
from .ScanParameter import ScanParameter


class Timeline:
    """
    Timeline 类定义，提供读写等接口。
    使用Timeline LIB时应该调用Timeline的接口，而不是IStore的接口。
    """
    def __init__(self, timelineId: str, store: IStore) -> None:
        if JavaString.isempty(timelineId):
            raise TimelineException(TimelineExceptionType.INVALID_USE, "timelineId cannot be empty")
        if store is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "store cannot be None")
        self.timelineId: str = timelineId
        self._store: IStore = store

    def store(self, message: IMessage) -> TimelineEntry:
        if message is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "message cannot be None")
        return self._store.write(self.timelineId, message)
    
    def storeAsync(self, message: IMessage, callback: TimelineCallback[IMessage]) -> Future[TimelineEntry]:
        if message is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "message cannot be None")
        return self._store.writeAsync(self.timelineId, message, callback)
    
    def batch(self, message: IMessage) -> None:
        if message is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "message cannot be None")
        self._store.batch(self.timelineId, message)

    def update(self, sequenceId: int, message: IMessage) -> TimelineEntry:
        if message is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "message cannot be None")
        if sequenceId is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "sequenceId cannot be None")
        return self._store.update(self.timelineId, sequenceId, message)
    
    def updateAsync(self, sequenceId: int, message: IMessage, callback: TimelineCallback[IMessage]) -> Future[TimelineEntry]:
        if message is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "message cannot be None")
        if sequenceId is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "sequenceId cannot be None")
        return self._store.updateAsync(self.timelineId, sequenceId, message, callback)
    
    def get(self, sequenceId: int) -> TimelineEntry:
        if sequenceId is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "sequenceId cannot be None")
        return self._store.read(self.timelineId, sequenceId)
    
    def getAsync(self, sequenceId: int, callback: TimelineCallback[TimelineEntry]) -> Future[TimelineEntry]:
        if sequenceId is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "sequenceId cannot be None")
        return self._store.readAsync(self.timelineId, sequenceId, callback)
    
    def scan(self, parameter: ScanParameter) -> Iterator[TimelineEntry]:
        if parameter is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "parameter cannot be None")
        return self._store.scan(self.timelineId, parameter)