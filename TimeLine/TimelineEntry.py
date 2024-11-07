
from .message.IMessage import IMessage

class TimelineEntry:
    """
    Timeline实体类，包括顺序ID和消息体。
    """
    def __init__(self, sequence_id: int, message: IMessage):
        self.sequence_id = sequence_id
        self.message: IMessage = message

    def getSequenceId(self) -> int:
        return self.sequence_id
    
    def getMessage(self) -> IMessage:
        return self.message
