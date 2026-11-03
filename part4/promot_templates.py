from langchain_core.prompts  import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()
model=ChatOllama()
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)
prompt=template2.invoke({'name':'mahanant'})
result=model.invoke(prompt)
print(result.content)