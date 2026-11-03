from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model=ChatGroq(model="qwen/qwen3.8-27b")
messages=[
    SystemMessage(content='you ara a helpful assient'),
     HumanMessage(content='tell me about langchain')
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)