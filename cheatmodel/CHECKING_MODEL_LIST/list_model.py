

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

for m in client.models.list().data:
    print(m.id)
    print("Model ID:", m.id)
    # print("Owned By:", m.owned_by)
    # print("Created:", m.created)
    # print("Context Window:", m.context_window)
    # print("Max Completion Tokens:", m.max_completion_tokens)
    # print("Supported Languages:", m.languages)
    # print("Active:", m.active)

    # ak particlur model ki infromation lana ha to 
#     model = client.models.retrieve("llama-3.3-70b-versatile")

# print(model.model_dump_json(indent=2))







# +++++++++++++++++++gogle genai ka liya model search karana code +++++++++++++++
# pip install google-genai python-dotenv
# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# for model in client.models.list():
#     print(model.name)

#     import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# model = client.models.get(
#     model="gemini-2.5-flash"
# )

# print(model)
# print("Name:", model.name)
# print("Display Name:", model.display_name)
# print("Description:", model.description)
# print("Input Token Limit:", model.input_token_limit)
# print("Output Token Limit:", model.output_token_limit)
# print("Supported Actions:", model.supported_actions)







# ++++++=++(pip install langchain-huggingface python-dotenv)
# import os
# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEndpoint

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="google/flan-t5-base",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     max_new_tokens=100
# )

# response = llm.invoke("What is Machine Learning?")
# print(response)




#  chat gpt ka liya use karana ha to  ( pip install openai python-dotenv)
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# models = client.models.list()

# for m in models.data:
#     print("-" * 50)
#     print("Model ID:", m.id)
    # print("Created:", m.created)
    # print("Owned By:", m.owned_by)

# koi ak paticular model ka liya 
# model = client.models.retrieve("gpt-6")

# print(model.model_dump_json(indent=2))