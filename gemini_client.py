import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "gemini-3-flash-preview"

def generate_text(prompt: str) -> str:
    response= client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    ) 
    return response.text