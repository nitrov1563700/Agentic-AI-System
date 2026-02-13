from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def create_plan(self,goal):
        prompt = f"""
You are a planning agent.
Break this goal into executable steps.
Avoid fluff.

Goal:
{goal}

Return numbered steps.
"""
        return self.think(prompt)