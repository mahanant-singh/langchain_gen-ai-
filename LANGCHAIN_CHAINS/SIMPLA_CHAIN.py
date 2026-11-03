from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
prompt=PromptTemplate(
    template='tu pagal ha sala {name}',
    input_variables=['name']
)
Model=ChatGroq(model="openai/gpt-oss-safeguard-20b")
parser=StrOutputParser()
chain=prompt |Model|parser
result=chain.invoke({'name':'ayan'})
print(result)
chain.get_graph().print_ascii()


# Method	      Work
# chain.invoke()	 Chain execute karta hai
# chain.get_graph()	 Chain ka graph obtain karta hai
# print_ascii()	     Terminal mein graph print karta hai
# get_graph()       .nodes	Graph ke nodes access karta hai
# get_graph().        edges	Nodes ke connections access karta hai