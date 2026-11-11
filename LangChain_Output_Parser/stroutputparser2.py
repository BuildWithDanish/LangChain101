from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

template1 = PromptTemplate(template = "write a poem on {topic}", input_variables = ["topic"])
template2 = PromptTemplate(template = "summarize in 2 sentence {text}", input_variables = ["text"])

parser = StrOutputParser()

# prompt1 = template1.invoke({"topic": "Nature"})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({"text": result1.content})
# result2 = model.invoke(prompt2)

# print(parser.parse(result2.content))


chain = template1 | model | template2 | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)