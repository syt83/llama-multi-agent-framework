from fastapi import FastAPI
from schemas import ChatRequest, ChatResponse
from llama_client import chat_with_llama

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):

    reply = await chat_with_llama([
        {
            "role": "user",
            "content": req.message
        }
    ])

    return ChatResponse(reply=reply)
