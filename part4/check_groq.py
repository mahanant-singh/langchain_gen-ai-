from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()  # .env se GROQ_API_KEY load hoga

model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0.7,
)

result = model.invoke("What is the capital of India?")
print(result.content)