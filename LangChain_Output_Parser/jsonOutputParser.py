# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation'
# )
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
# model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(template = "write a poem on {topic}", input_variables = ["topic"])
template2 = PromptTemplate(template = "summarize in 2 sentence {text}", input_variables = ["text"])

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser   

result = chain.invoke({'topic':'black hole'})

print(template)
print(result)

# You can not enforce Schema in JsonOutputParser