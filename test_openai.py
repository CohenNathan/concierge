from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key[:20]}..." if api_key else "❌ NO KEY")

client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Solomon, a helpful concierge bear."},
            {"role": "user", "content": "Ciao, come stai?"}
        ],
        max_tokens=100
    )
    print("✅ OpenAI API works!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ OpenAI API error: {e}")
