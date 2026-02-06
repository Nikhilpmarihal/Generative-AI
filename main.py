from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest")

response = model.invoke("Hello")
print(response)