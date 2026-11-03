import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

for m in client.models.list().data:
    print(m.id)
# 

# any information of model 
# for m in client.models.list().data:
#     print(m.id, "|", m.owned_by, "|", m.context_window)