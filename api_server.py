from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

Class ChatRequest(BaseModel):
  message: str
  user_id: str

@app.post("/chat")
async def chat(request: ChatRequest):
  message = request.message
  response_text = f "You sid: {message}. This is a placeholder response from the AI."
  return {"response": response_text}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)