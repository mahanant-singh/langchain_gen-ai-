from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
prompt1=PromptTemplate(
    template='generate a detailed report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='genrate a 5 ppinter summary from the following text \n{text}',
    input_variables=['text']
)
model=ChatGroq(model="openai/gpt-oss-20b")
parser=StrOutputParser()
chain=prompt1|model|parser|prompt2|model|parser
result=chain.invoke({'topic':'Unemployment is india'})
print(result)

chain.get_graph().print_ascii()