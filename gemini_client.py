import os
from google import genai
from dotenv import load_dotenv

# load the .env content
load_dotenv()

# connect the gemini api key to the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# select specific model
MODEL_ID = "gemini-3-flash-preview"

# function to generative content
def generate_text(prompt: str) -> str:
    response= client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    ) 
    return response.text