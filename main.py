from llm.groq_llm import GroqLLM
from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from agents.planner_agent import PlannerAgent
from agents.executor_agent import ExecutorAgent
from agents.critic_agent import CriticAgent
from agents.manager_agent import ManagerAgent

def main():
    llm = GroqLLM()
    stm = ShortTermMemory()
    Itm = LongTermMemory()

    planner = PlannerAgent("Planner",llm,stm,Itm)
    executor = ExecutorAgent("Executor",llm,stm,Itm)
    critic = CriticAgent("Critic",llm,stm,Itm)

    manager = ManagerAgent(planner,executor,critic,Itm)
    goal = input("\nEnter Autonomous Goal:")

    print(("\n[bold cyan]Running Level-10 Agentic System...[/bold cyan]\n"))
    results = manager.run(goal)

    print("\n[bold green]FINAL OUTPUT[/bold green]")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
