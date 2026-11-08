from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model = "gemini-2.5-flash")

response = llm.invoke("what is the capital of France?")

print(response)