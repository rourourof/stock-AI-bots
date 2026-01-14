import os
import openai
from template import build_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(data, mode, prev):
    prompt = build_prompt(data, mode, prev)

    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return res.choices[0].message.content
