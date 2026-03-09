from fastapi import FastAPI
from pydantic import BaseModel
from agents.supervisor import SupervisorAgent

app = FastAPI()
supervisor = SupervisorAgent()

class ChatRequest(BaseModel):
    id : str
    msg : str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = supervisor.handle_message(request.id, request.msg)
    return {"response": response}
