import os
import google.generativeai as genai
from prompt_builder import build_prompt

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config={
        "temperature": 0.2,
        "max_output_tokens": 4096
    }
)

def generate_text(data, mode, prev):
    prompt = build_prompt(data, mode, prev)
    response = model.generate_content(prompt)
    return response.text
