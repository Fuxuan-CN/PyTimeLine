
from .common.TimelineException import TimelineException
from .common.TimelineExceptionType import TimelineExceptionType
from .ScanParameter import ScanParameter
from .unknowPak.Filter import Filter

class ScanParameterBuilder:
    """ ScanParameter类的构造类，LIB使用者必须使用ScanParameterBuilder构造ScanParameter。 """

    def __init__(self, parameter: ScanParameter = None) -> None:
        self.parameter = parameter

    @staticmethod
    def scanForward() -> 'ScanParameterBuilder':
        """ 构造一个向前扫描的ScanParameterBuilder对象。 """
        parameter = ScanParameter(True)
        return ScanParameterBuilder(parameter)
    
    @staticmethod
    def scanBackward() -> 'ScanParameterBuilder':
        """ 构造一个向后扫描的ScanParameterBuilder对象。 """
        parameter = ScanParameter(False)
        return ScanParameterBuilder(parameter)
    
    def from_id(self, sequence_id: int) -> 'ScanParameterBuilder':
        """ 设置扫描的起始序列号。 """
        if sequence_id < 0:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "from must more than or equal 0")
        self.parameter.set_from(sequence_id)
        return self
    
    def to_id(self, sequence_id: int) -> 'ScanParameterBuilder':
        """ 设置扫描的结束序列号。 """
        if sequence_id < 0:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "to must more than or equal 0")
        self.parameter.set_to(sequence_id)
        return self
    
    def maxCount(self, count: int) -> 'ScanParameterBuilder':
        """ 设置最大返回数量。 """
        if count < 0:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "maxCount must more than or equal 0")
        self.parameter.setMaxCount(count)
        return self
    
    def filter(self, filter: Filter) -> 'ScanParameterBuilder':
        """ 设置过滤器。 """
        if filter is None:
            raise TimelineException(TimelineExceptionType.INVALID_USE, "filter cannot be None")
        self.parameter.setFilter(filter)
        return self
    
    def build(self) -> ScanParameter:
        """ 构造ScanParameter对象。 """
        return self.parameter