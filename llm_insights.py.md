---
created: 2025-01-08T09:15:56-08:00
modified: 2025-01-08T09:15:59-08:00
---

# llm_insights.py

import openai

openai.api_key = "your_openai_api_key"

def query_llm(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response["choices"][0]["text"].strip()
