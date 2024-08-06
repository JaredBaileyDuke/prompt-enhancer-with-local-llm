from openai import OpenAI
import requests

def llm_message(system_message="You are Llamafile, an AI assistant.", user_message="Write a short story about llamas."):
    """
    Call the LLM API using Python
    This function is in the form of the OpenAI Python API call
    Args:
        system_message: str
        user_message: str
    Returns:
        str - response from the API
    """
    # This is a conversation between User and Llama, a friendly chatbot.
    # Llama is helpful, kind, honest, good at writing,
    # and never fails to answer any requests immediately and with precision.
    client = OpenAI(
        base_url='http://host.docker.internal:8080/v1',
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


def call_rust_service(system_message, user_message):
    """
    Call the LLM API using Rust
    This function sends a POST request to the Rust service
    Args:
        system_message: str
        user_message: str
    Returns:
        str - response from the API
    """
    url = "http://127.0.0.1:8081/llm_message"
    payload = {
        "system_message": system_message,
        "user_message": user_message
    }
    response = requests.post(url, json=payload, timeout=60)
    if response.status_code == 200:
        return response.text
    return "Error occurred"


if __name__ == "__main__":
    SYSTEM_MESSAGE="You are Llamafile, an AI assistant."
    USER_MESSAGE="Write 1 or 2 sentence about llamas."

    # print time of each run
    import time

    start = time.time()
    print(call_rust_service(SYSTEM_MESSAGE, USER_MESSAGE))
    print("Rust Time:", time.time() - start, "\n")

    start = time.time()
    print(llm_message(SYSTEM_MESSAGE, USER_MESSAGE).content)
    print("Python Time:", time.time() - start, "\n")

    start = time.time()
    print(call_rust_service(SYSTEM_MESSAGE, USER_MESSAGE))
    print("Rust Time:", time.time() - start, "\n")
