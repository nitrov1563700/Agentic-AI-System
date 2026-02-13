from config.config import MAX_ITERATIONS

class ManagerAgent:
    def __init__(self,planner,executor,critic,Itm):
        self.planner = planner
        self.executor = executor
        self.critic = critic
        self.Itm = Itm

    def run(self,goal):
        plan = self.planner.create_plan(goal)
        steps = plan.split("\n")


        iteration = 0
        final_results = []

        while iteration < MAX_ITERATIONS:
            for step in steps:
                if not step.strip():
                    continue
                result = self.executor.execute_task(step)
                critique = self.critic.critique(result)

                improved_prompt = f"""
Improve the result using this critique.

Result:
{result}

Critique:
{critique}
"""
                improved = self.executor.think(improved_prompt)
                final_results.append(improved)

                self.Itm.save("\n".join(final_results))
                iteration += 1

            return final_results