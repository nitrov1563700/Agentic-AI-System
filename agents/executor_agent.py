from agents.base_agent import BaseAgent

class ExecutorAgent(BaseAgent):
    def execute_task(self,task):
        prompt = f"""
Execute the task below with maximum quality.
Be precise and actionable.

Task:
{task}
"""
        return self.think(prompt)