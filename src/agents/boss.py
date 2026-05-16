import json

class BossAgent:

    def __init__(self, llm_call):
        self.llm_call = llm_call

    async def plan(self, user_message: str):

        prompt = f"""
You are a task planner for a multi-agent system.

Break the request into practical, executable subtasks.

Rules:
- Tasks must be concrete and detailed enough to execute
- Do NOT make tasks too vague (like "create API")
- Include necessary technical details (framework, method, structure)
- Use ONLY these roles: code, research, writer
- Keep 2~4 tasks max
- Ensure each task is meaningful and non-trivial

Return ONLY valid JSON:

{{
  "tasks": [
    {{
      "role": "research",
      "task": "Research Flask API best practices including routing and structure"
    }},
    {{
      "role": "code",
      "task": "Implement a Flask API with GET/POST endpoints without documentation"
    }},
    {{
      "role": "writer",
      "task": "Write API documentation explaining endpoints and usage"
    }}
  ]
}}

User request:
{user_message}
"""

        response = await self.llm_call([
            {"role": "user", "content": prompt}
        ])

        try:
            data = json.loads(response)
            return data["tasks"]

        except:
            return [
                {
                    "role": "writer",
                    "task": response
                }
            ]

    async def synthesize(self, user_request, worker_results):

        formatted_results = "\n\n".join(
            f"[{i}] {r}"
            for i, r in enumerate(worker_results)
        )

        prompt = f"""
You are a final AI system synthesizer.

Your job is to combine multiple worker outputs into a single, clear, high-quality response.

User request:
{user_request}

Worker outputs:
{formatted_results}

Rules:
- Merge overlapping content
- Remove redundancy
- Produce a clean final answer
"""

        response = await self.llm_call([
            {"role": "user", "content": prompt}
        ])

        return response
