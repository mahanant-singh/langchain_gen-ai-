# from langchain_text_splitters import CharacterTextSplitter

# text = """

# Keyword arguments:
# argument -- description
# Return: return_description
# """

# splitter = CharacterTextSplitter(
#     chunk_size=5,
#     chunk_overlap=0,
#     separator=''
# )

# result = splitter.split_text(text)
# print(result)
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("D:/compax_langchain/basic_of_langchain/text_splitters/mahanantsingh_cv.pdf")
docs=loader.load()
splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''

)
result=splitter.split_documents(docs)
# print(len(result))
print(result[1].page_content)