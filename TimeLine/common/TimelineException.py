
from .TimelineExceptionType import TimelineExceptionType


class TimelineException(RuntimeError):

    def __init__(self, exception_type: TimelineExceptionType, message: str, cause: Exception) -> None:
        if cause is not None:
            message += f"\nCaused by: {type(cause).__name__}: {str(cause)}"
        super().__init__(message)
        self.exception_type = exception_type

    @property
    def Etype(self) -> TimelineExceptionType:
        return self.exception_type