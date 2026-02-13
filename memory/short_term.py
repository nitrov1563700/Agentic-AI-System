class ShortTermMemory:
    def __init__(self):
        self.buffer = []

    def add(self, text):
        self.buffer.append(text)

    def get(self):
        return "\n".join(self.buffer[-10:])