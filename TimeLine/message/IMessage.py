
from abc import ABC, abstractmethod

class IMessage(ABC):
    """ 消息类的接口，LIB的使用者需要继承IMessage或者DistinctMessage实现自己的Message类 """

    @abstractmethod
    def getMessageId(self):
        """ 获取消息ID """
        pass

    @abstractmethod
    def setMessageId(self, messageId):
        """ 设置消息ID """
        pass

    @abstractmethod
    def newInstance(self) -> 'IMessage':
        """ 创建一个新的消息实例 """
        pass

    @abstractmethod
    def serialize(self) -> bytes:
        """ 序列化消息 """
        pass

    @abstractmethod
    def deserialize(self, data: bytes):
        """ 反序列化消息 """
        pass

    @abstractmethod
    def addAttribute(self, attribute: str, value: str):
        """ 添加属性 """
        pass

    @abstractmethod
    def getAttribute(self, attribute: str) -> str:
        """ 获取属性值 """
        pass

    @abstractmethod
    def getAttributes(self) -> dict[str, str]:
        """ 获取所有属性 """
        pass