import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("GROQ_API_KEY is missing from backend/.env")
    raise SystemExit(1)

response = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={
        "Authorization": "Bearer " + api_key
    },
    timeout=30,
)

print("Status:", response.status_code)

data = response.json()

if response.status_code != 200:
    print(data)
    raise SystemExit(1)

for model in data.get("data", []):
    print(model["id"])