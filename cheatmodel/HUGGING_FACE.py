
from langchain_ollama import ChatOllama


model = ChatOllama(
    model="tinyllama",
    temperature=0.7
)


result = model.invoke("What is the capital of India?")


print(result.content)
