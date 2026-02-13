from agents.base_agent import BaseAgent

class CriticAgent(BaseAgent):
    def critique(self,output):
        prompt = f"""
Critically analyze this output.
List flaws, missing parts , and improvements.

Output:
{output}
"""
        return self.think(prompt)