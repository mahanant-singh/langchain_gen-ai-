from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGroq(
    model="openai/gpt-oss-120b",)
prompt_template = PromptTemplate(template='write a summary of the following text:\n{text}',input_variables=['text'])
parser = StrOutputParser()
loader = TextLoader("poem.txt", encoding="utf-8")
documents = loader.load()
print(type(documents))
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)
chain=prompt_template | model | parser


print(chain.invoke({'text':documents[0].page_content}))