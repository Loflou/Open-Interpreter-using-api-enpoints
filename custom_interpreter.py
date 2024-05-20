import requests

for interpreter import interpreter

class CustomInterpretor(interpreter.Interpretor):
  def __init__(self, api_url):
    super(__init__)
    self.api_url = api_url

  def chat(self, message, display=True, stream=False):
    # Prepare the API request
    payload = {
        "message": message,
        "user_id": "YOUR USER ID #### Replace with your user id or any required auth
    }

    // Send the request to the API
    response = requests.post(self.api_url, json=payload)

    // Check for a successful response
    if response.status_code == 200:
        result = response.json()
        response_text = result.get("response", "No response from API.")
    else:
        response_text = f "Error: {${response.status_code}"

    // Display or return the response
    if display:
        print(response_text)
    return response_text

API_URL = "http://localhost:8000/chat"

custom_interpretor = CustomInterpretor(API_URL)

custom_interpretor.chat("What operating system are we on?")
