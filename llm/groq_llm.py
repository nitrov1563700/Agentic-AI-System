import os
from groq import Groq
from dotenv import load_dotenv

from config.config import MODEL_NAME

load_dotenv()

class GroqLLM:
    def __init__(self):
        self.client=Groq(api_key=os.getenv("GROQ_API_KEY"))

    def call(self, prompt, temperature=0.3):
        response = self.client.chat.completions.create(
            model = MODEL_NAME,
            messages = [{"role":"user","content":prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()