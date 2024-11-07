
import threading

class AtomicInterger:
    """
    仿照 java 中的 AtomicInteger 类实现的原子操作类
    """
    def __init__(self, initial_value=0):
        self.value = initial_value
        self.lock = threading.Lock()

    def CompareAndSet(self, expect_value, update_value):
        with self.lock:
            if self.value == expect_value:
                self.value = update_value
                return True
            else:
                return False
            
    def addAndGet(self, delta):
        with self.lock:
            self.value += delta
            return self.value

    def increment(self):
        with self.lock:
            self.value += 1

    def decrement(self):
        with self.lock:
            self.value -= 1

    def get(self):
        with self.lock:
            return self.value

    def set(self, value):
        with self.lock:
            self.value = value