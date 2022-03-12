class MemoryDatabase:
    _instance = None

    def __init__(self):
        self.users_table = {}

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance