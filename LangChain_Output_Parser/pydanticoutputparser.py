# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from typing import final

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation'
# )
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# model = ChatHuggingFace(llm = llm)


class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    city: str = Field(description="The person's city")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# result = model.invoke(template.invoke({'place':'New York'}))
# finalresult = parser.parse(result.content)    

chain = template | model | parser
result = chain.invoke({'place':'Lucknow'})
print(result)