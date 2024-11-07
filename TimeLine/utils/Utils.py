
import loguru
from concurrent.futures import Future
import os
import sys
import socket

class Utils:

    CONTENT_COLUMN_START_ID = 10000
    SYSTEM_COLUMN_NAME_PREFIX = "__"

    logger = loguru.logger
    logger.remove()
    my_fmt = "<lvl>{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | {name}.{function} | {file}:{line} | {message}</lvl>"
    stream_handler = sys.stdout
    logger.add(stream_handler, format=my_fmt, level="TRACE")

    @staticmethod
    def waitForFuture(f: Future):
        try:
            return f.result()
        except KeyboardInterrupt:
            Utils.logger.error("KeyboardInterrupt")
            return None
        except Exception as e:
            Utils.logger.error(f"the Thread was aborted due to an error: {e}")
            return None
        
    @staticmethod
    def get_process_id() -> int:
        return os.getpid()
    
    @staticmethod
    def get_local_ip() -> str:
        return socket.gethostbyname(socket.gethostname())
    
    @staticmethod
    def getLogger() -> loguru.Logger:
        return Utils.logger