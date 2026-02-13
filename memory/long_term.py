class LongTermMemory:
    def __init__(self):
        self.store = []

    def save(self,text):
        self.store.append(text)

    def recall(self):
        return "\n".join(self.store)