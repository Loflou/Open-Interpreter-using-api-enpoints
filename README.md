# Open Interpreter

## Custom Integration with API Endpoint

Follow these steps to set up and run the custom integration.

### Installation Guide

1. **Install Python** \n    ensure you have Python installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Open Interpreter** \n    Open a command prompt and install Open Interpreter using pip:\n   ```sh\n   pip install open-interpreter\n   ```\n\n 3. **Set Up API Server** \n   Set up a FastAPI server to handle the requests and responses. Use the `api_server.py` script provided in this repository.\n\n 4. **Run Custom Interpreter** \n   Use the `custom_interpreter.py` script to run the custom interpreter.

### Example Code

### FastAPI Server (api_server.py)

``python\nfrom fastapi import FastAPI, Request\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass ChatRequest(BaseModel):\n  message: str\n  user_id: str\n\n@app.post("/chat")\nasync def chat(request: ChatRequest):\n  message = request.message\n  response_text = f "You said: { message }. This is a placeholder response from the AI.\n  return {"response": response_text}\n\nif __name__ == "__main__":\n  import uvicorn\n  uvicorn.run(app, host="0.0.0.0", port=8000)\n``\n\n### Custom Interpreter (custom_interpretor.py)\n``python{\nimport requests\nfrom interpreter import interpreter\n\nclass CustomInterpretor(interpreter.Interpretor):\n  def __init__(self, api_url):\n    super(__init__)\n    self.api_url = api_url\n\n  def chat(self, message, display=True, stream=False):\n    payload = {\n        message: message,\n        user_id: "YOUR USER ID #### Replace with your user id or any required auth\n    }\n\n    response = requests.post(self.api_url, json=payload)\n\n    if response.status_code == 200:\n        result = response.json()\n        response_text = result.get("response", "No response from API.")\n    else:\n        response_text = f "Error: {${response.status_code}}\n\n    if display:\n        print(response_text)\n    return response_text\n\nAPI_URL = "http://localhost:8000/chat"\n\ncustom_interpretor = CustomInterpretor(API_URL)\n\ncustom_interpretor.chat("What operating system are we on")\n``