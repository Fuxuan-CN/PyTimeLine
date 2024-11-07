

class Filter:
    """
    过滤器，用于对数据进行过滤
    """
    def __init__(self):
        self.conditions = []

    def add_condition(self, condition):
        self.conditions.append(condition)

    def apply(self, items):
        return [item for item in items if all(condition(item) for condition in self.conditions)]