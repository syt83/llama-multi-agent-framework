import httpx

LLAMA_URL = "http://127.0.0.1:8080/v1/chat/completions"


async def chat_with_llama(messages):

    async with httpx.AsyncClient() as client:

        res = await client.post(
            LLAMA_URL,
            json={
                "model": "qwen2.5-3b.gguf",
                "messages": messages,
                "temperature": 0.7
            },
            timeout=60
        )

        data = res.json()

        return data["choices"][0]["message"]["content"]
