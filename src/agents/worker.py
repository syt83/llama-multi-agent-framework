class WorkerAgent:

    def __init__(self, role, llm_call):
        self.role = role
        self.llm_call = llm_call

    async def run(self, task: str):

        prompt = f"""
You are a {self.role} agent.

Complete the following task:

{task}

Be precise and practical.
"""

        response = await self.llm_call([
            {"role": "user", "content": prompt}
        ])

        return {
            "role": self.role,
            "input": task,
            "output": response
        }
