"""Quick smoke-test to verify the OpenAI API key and connectivity."""
import os
import sys
from openai import OpenAI

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    print("Sending test request to OpenAI API...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Reply with exactly: API is working"}],
        max_tokens=10,
    )

    reply = response.choices[0].message.content.strip()
    print(f"Response: {reply}")
    print(f"Model used: {response.model}")
    print(f"Tokens used: {response.usage.total_tokens}")
    print("OpenAI API check passed.")

if __name__ == "__main__":
    main()
