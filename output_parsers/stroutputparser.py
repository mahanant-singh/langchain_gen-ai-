from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=ChatGroq(model="openai/gpt-oss-20b")
# detailed report
template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['toic']
)
# summary
template2=PromptTemplate(
    template='write a 5 line summary on the following text ./n {text}'
)
