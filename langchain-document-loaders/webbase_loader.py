from langchain_community.document_loaders import WebbaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=ChatGroq(
    model="openai/gpt-oss-120b")
prompt_template = PromptTemplate(template='write a summary of the following text:\n{text}',
input_variables=['text'])
parser = StrOutputParser()
url="https://www.geeksforgeeks.org/what-is-big-data/"
loader=WebbaseLoader(url)
docus=loader.load()
chain=prompt_template | model | parser
print(chain.invoke({'text':docus[0].page_content}))
