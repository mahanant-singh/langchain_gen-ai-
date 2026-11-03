from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
os.environ["HF_HOME"] = "D:/huggingface_cache"
llm=HuggingFacePipeline.from_model_id(
    model_id='tinyllama',
    pipeline_kwargs=dict(
        tempertemperature=0.5,
        max_new_tokens=100
    )
)
Model=ChatHuggingFace(llm=llm)
result=Model.invoke("what is the coptial of india")

# tinyllama run karna kaliya pytorch ka use karna pada ga 

#  cmd ya ha gpu pr run hogi
# pip uninstall torch -y
# pip install torch --index-url https://download.pytorch.org/whl/cu124