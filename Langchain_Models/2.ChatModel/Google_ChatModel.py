from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

response = chatModel.invoke("what is the capital of France?")

print(response)