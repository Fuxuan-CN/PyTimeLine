
from .IMessage import IMessage
from ..javaInterface.AtomicInterger import AtomicInterger
from ..javaInterface.Constant import JAVA_MAX_INTERGER_VALUE
from ..common.TimelineException import TimelineException
from ..common.TimelineExceptionType import TimelineExceptionType
from ..utils.Utils import Utils
from ..javaInterface._string import JavaString

class DistinctMessage(IMessage):
    """
    消息接口的一种抽象实现，此抽象类会自动创建消息ID。 如果继承DistinctMessage实现自己的消息类，则在自定义消息类中不需要再次实现getMessageID接口。
    """
        
    base_id = AtomicInterger(0)
    machine_id = f"{Utils.get_process_id()}@{Utils.get_local_ip()}:"
    
    def __init__(self) -> None:
        self.message_id = None

    def getMessageId(self) -> str:
        if self.message_id is None:
            DistinctMessage.base_id.CompareAndSet(JAVA_MAX_INTERGER_VALUE, 0)
            self.message_id = f"{DistinctMessage.machine_id}{str(DistinctMessage.base_id.addAndGet(1))}"

    def setMessageId(self, message_id: str) -> None:
        if JavaString.isempty(message_id):
            raise TimelineException(TimelineExceptionType.INVALID_USE, "Message id cannot be null or empty.")
        self.message_id = message_id