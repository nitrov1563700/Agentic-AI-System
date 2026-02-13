class BaseAgent:
    def __init__(self,name,llm,stm,Itm):
        self.name = name
        self.llm = llm
        self.stm = stm
        self.Itm = Itm

    def think(self, prompt):
        response = self.llm.call(prompt)
        self.stm.add(f"{self.name}:{response}")
        return response