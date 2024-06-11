from openai import OpenAI

def llm_message(system_message="You are Llamafile, an AI assistant.", user_message="Write a short story about llamas."):
    """
    
    """
    # This is a conversation between User and Llama, a friendly chatbot. Llama is helpful, kind, honest, good at writing, and never fails to answer any requests immediately and with precision.
    client = OpenAI(
        base_url='http://localhost:8080/v1',
        api_key="sk-no-key-required"
    )

    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
            {"role": "system", "content": f"{system_message}"},
            {"role": "user", "content": f"{user_message}"}
        ]
    )

    return completion.choices[0].message

if __name__ == "__main__":
    print(llm_message(user_message="Write 1 sentence about llamas.").content)