import requests
from langchain_core.prompts import ChatPromptTemplate

Api = ""#add your own api key from chutes here
Link = "https://llm.chutes.ai/v1/chat/completions"
prompt = """You are Mike, a Butler to Rahul who has created you. Act professionally and use British English."""

# Fixed: Added comma between tuples and corrected placeholder
prompt_temp = ChatPromptTemplate.from_messages([
    ("system", prompt), 
    ("human", "{question}") 
])

class Deepseek:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {Api}",
            "Content-Type": "application/json",
        }

    def get_response(self, user_input: str) -> str:
        formatted_prompt = prompt_temp.format_messages(question=user_input)
        
        payload = {
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input},
            ],
            "temperature": 0.7,
        }
        # Fixed: Corrected typo (header -> headers), and API endpoint (Link, not Api)
        response = requests.post(Link, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

def main():
    chatbot = Deepseek()
    print("You're chatting with Mike! Type 'goodbye' to exit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "goodbye":
            break
        print(f"Mike: {chatbot.get_response(user_input)}")

if __name__ == "__main__":
    main()