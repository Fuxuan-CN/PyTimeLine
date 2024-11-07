

import io

class Closeable(io.IOBase):
    """ 仿照Java的Closeable接口 """

    def close(self):
        """ 关闭资源 """
        pass