
from enum import Enum

class TimelineExceptionType(Enum):
    RETRY = 1 # 重试
    INVALID_USE = 2 # 使用方法错误
    ABORT = 3 # 中止
    UNKNOWN = 4 # 未知错误