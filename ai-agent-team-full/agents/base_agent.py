class BaseAgent:
    def __init__(self, name, memory, tools=None):
        self.name = name
        self.memory = memory
        self.tools = tools or {}

    def log(self, message):
        print(f"[{self.name}] {message}")

    def think(self, input_data):
        raise NotImplementedError
