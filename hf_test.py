import os
import requests

API_URL = "https://router.huggingface.co/hf-inference/models/google/gemma-7b-it"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}",
    "Content-Type": "application/json"
}

payload = {
    "inputs": "Say hello in a friendly way",
    "parameters": {
        "max_new_tokens": 50,
        "temperature": 0.7
    }
}

response = requests.post(API_URL, headers=headers, json=payload)

print("STATUS:", response.status_code)
print("TEXT RESPONSE:")
print(response.text)
