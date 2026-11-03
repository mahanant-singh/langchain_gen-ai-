from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")  

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI:", result.content)

print(chat_history)
# for msg in chat_history:
#     print(f"{msg.type}: {msg.content}")

# =======================================without message ka use kara =========================
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(model="qwen/qwen3.8-27b")  

# chat_history = []

# while True:
#     user_input = input("you: ")
#     if user_input.lower() == "exit":
#         break

#     chat_history.append(("human", user_input))
#     result = model.invoke(chat_history)
#     chat_history.append(("ai", result.content))

#     print("AI:", result.content)

# print(chat_history)