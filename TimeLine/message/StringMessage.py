from ..common.TimelineException import TimelineException
from ..common.TimelineExceptionType import TimelineExceptionType
from .DistinctMessage import DistinctMessage

class StringMessage(DistinctMessage):
    """ 一种简单的字符串类型的消息实现 """
    def __init__(self):
        super().__init__()
        self.content: str = ""
        self.message_id: str = None
        self.attrs: dict[str, str] = {}

    @classmethod
    def with_id(cls, message_id: str, content: str = ""):
        message = cls(content)
        message.message_id = message_id

    @classmethod
    def with_content(cls, content: str):
        message = cls(content)
        cls.message_id = super().getMessageId()
        return message
    
    def getContent(self) -> str:
        return self.content
    
    def newInstance(self) -> "StringMessage":
        return StringMessage()
    
    def serialize(self) -> bytes:
        return bytes(self.content, "utf-8")
    
    def deserialize(self, data: bytes):
        self.content = data.decode("utf-8")

    def addAttribute(self, attribute, value) -> None:
        if attribute is None or attribute == "":
            raise TimelineException(TimelineExceptionType.INVALID_USE, "Attribute name cannot be empty or None")
        if value is None or value == "":
            raise TimelineException(TimelineExceptionType.INVALID_USE, "Attribute value cannot be empty or None")
        self.attrs[attribute] = value
    
    def updateAttribute(self, attribute, new_value) -> None:
        if attribute not in self.attrs.keys():
            raise TimelineException(TimelineExceptionType.INVALID_USE, "Attribute does not exist")
        else:
            self.attrs[attribute] = new_value

    def getAttributes(self) -> dict[str, str]:
        return self.attrs
    
    def getMessageId(self) -> str:
        return self.message_id
    
    def setMessageId(self, message_id: str) -> None:
        self.message_id = message_id