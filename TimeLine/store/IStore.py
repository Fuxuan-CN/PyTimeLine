
from abc import abstractmethod
from ..ScanParameter import ScanParameter
from ..TimelineEntry import TimelineEntry
from ..common.TimelineCallback import TimelineCallback
from ..message.IMessage import IMessage
from ..javaInterface._io import Closeable
from concurrent.futures import Future
from typing import Iterator

class IStore(Closeable):
    """ 存储层接口的定义。 """

    @abstractmethod
    def write(self, timelineId: str, message: IMessage) -> TimelineEntry:
        pass

    @abstractmethod
    def batch(self, timelineId: str, messages: IMessage) -> None:
        pass

    @abstractmethod
    def writeAsync(self, timelineId: str, message: IMessage, callback: TimelineCallback[IMessage]) -> Future[TimelineEntry]:
        pass

    @abstractmethod
    def update(self, timelineId: str, sequence_id: int, message: IMessage) -> TimelineEntry:
        pass

    @abstractmethod
    def updateAsync(self, timelineId: str, sequence_id: int, message: IMessage, callback: TimelineCallback[IMessage]) -> Future[TimelineEntry]:
        pass

    @abstractmethod
    def read(self, timelineId: str, sequence_id: int) -> TimelineEntry:
        pass

    @abstractmethod
    def readAsync(self, timelineId: str, sequence_id: int, callback: TimelineCallback[TimelineEntry]) -> Future[TimelineEntry]:
        pass

    @abstractmethod
    def scan(self, timelineId: str, scan_parameter: ScanParameter) -> Iterator[TimelineEntry]:
        pass

    @abstractmethod
    def create() -> None:
        pass

    @abstractmethod
    def drop() -> None:
        pass

    @abstractmethod
    def exist() -> bool:
        pass

    @abstractmethod
    def close() -> None:
        pass

    