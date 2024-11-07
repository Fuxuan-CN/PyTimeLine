
from .unknowPak.Filter import Filter

class ScanParameter:
    """ 范围读取的参数类，涉及到：范围读取方向、起始位置、结束位置和最多返回个数。 """

    def __init__(self, isForward: bool) -> None:
        self.from_id: int = None
        self.to_id: int = None
        self.maxCount: int = None
        self.isForward: bool = isForward
        self.filter: Filter = None

    def get_from(self) -> int:
        return self.from_id
    
    def set_from(self, from_id: int) -> None:
        self.from_id = from_id

    def get_to(self) -> int:
        return self.to_id
    
    def set_to(self, to_id: int) -> None:
        self.to_id = to_id

    def getMaxCount(self) -> int:
        return self.maxCount
    
    def setMaxCount(self, maxCount: int) -> None:
        self.maxCount = maxCount

    def isforward(self) -> bool:
        return self.isForward
    
    def getFilter(self) -> Filter:
        return self.filter
    
    def setFilter(self, filter: Filter) -> None:
        self.filter = filter