from openai import OpenAI
from dotenv import load_dotenv
import os

client = OpenAI()
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Hello! I my name is John!"}
    ],
)

print(response.to_json(indent=2))