
from readerwriterlock import rwlock

class ReentrantReadWriteLock(rwlock.RWLockRead):
    """
    仿照Java的ReentrantReadWriteLock实现的读写锁
    """
    def __init__(self):
        super().__init__()