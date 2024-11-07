


class JavaString:
    """
    仿照Java的String类，实现一个Python的字符串类
    """
    @staticmethod
    def isempty(string: str) -> bool:
        """
        检查字符串是否为空
        """
        return len(string) == 0 or string == ""