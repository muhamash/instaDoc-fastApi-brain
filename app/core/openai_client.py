import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = OpenAI(api_key="<DeepSeek>", base_url="https://api.deepseek.com")


def ask_openai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=100,
    )
    content = response.choices[0].message.content

    print(content)
    # return content.strip() if content is not None else ""
    return content if content is not None else ""
