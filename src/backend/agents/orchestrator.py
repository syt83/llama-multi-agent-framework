import asyncio
from agents.worker import WorkerAgent

class Orchestrator:

    def __init__(self, llm_call):
        self.llm_call = llm_call

        self.role_map = {
            "write": "writer",
            "writer": "writer",
            "coding": "code",
            "code": "code",
            "research": "research"
        }

    async def run(self, tasks):

        workers = {
            "code": WorkerAgent("code expert", self.llm_call),
            "research": WorkerAgent("research expert", self.llm_call),
            "writer": WorkerAgent("writing expert", self.llm_call),
        }

        jobs = []

        for t in tasks:

            role = self.role_map.get(t["role"], "writer")

            worker = workers.get(role, workers["writer"])

            jobs.append(worker.run(t["task"]))

        results = await asyncio.gather(*jobs)

        return {
            "results": results
        }
