from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to talk to backend (fixes CORS errors)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins - safe for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    user_input: str

@app.post("/chat")
def chat_endpoint(chat_input: ChatInput):
    user_message = chat_input.user_input
    bot_response = f"You said: {user_message}"
    return {"reply": bot_response}
