# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation'
# )
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
# model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(template = "write a poem on {topic}", input_variables = ["topic"])
template2 = PromptTemplate(template = "summarize in 2 sentence {text}", input_variables = ["text"])

prompt1 = template1.invoke({"topic": "Nature"})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)

print(result1)
print(result1.content)
print(result2.content)