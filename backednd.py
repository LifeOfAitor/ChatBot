import openai
import os

class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=3000,
            temperature=0.5
        ).choices[0].message['content']
        return response

if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Write a joke")
    print(response)
