import requests

API_KEY = "YOUR-API-KEY"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Speaking Chatbot"
}

messages = [
    {"role": "system", "content": "You are a helpful AI."}
]

print("Speaking chatbot ready! Type 'quit' to exit.\n")

while True:
    user = input("You: ")
    if user.lower() == "quit":
        break

    messages.append({"role": "user", "content": user})

    response = requests.post(
        url,
        headers=headers,
        json={
            "model": "openai/gpt-4o-mini",
            "messages": messages,
            "max_tokens": 200
        }
    )

    if response.status_code != 200:
        print("❌ Error:", response.text)
        continue

    data = response.json()

    reply = data["choices"][0]["message"]["content"]
    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})
