from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
load_dotenv()
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['toic']
)
parser=StrOutputParser()
model=ChatGroq(model='openai/gpt-oss-20b')
prompt2=PromptTemplate(
    template='explain the following joke-{text}',
    input_variables=['text']
)
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parllel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})
final_chain=RunnableSequence(joke_gen_chain,parllel_chain)

result=final_chain.invoke({'topic':'cricket'})
print(result['joke'])