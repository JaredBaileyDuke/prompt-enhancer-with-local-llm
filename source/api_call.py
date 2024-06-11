from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:8080/v1',
    api_key="sk-no-key-required"
)

completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are Llamafile, an AI assistant."},
        {"role": "user", "content": "Write a short story about llamas."}
    ]
)