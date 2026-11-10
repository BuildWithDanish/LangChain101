from typing import TypedDict,Optional, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Optional[str], "The sentiment of the review, can be 'positive', 'negative', or 'neutral'"]

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The iPhone offers a premium design with a sleek and elegant look.
The camera captures stunning photos and high-quality videos.
Performance is smooth, fast, and reliable.
The display quality is excellent, with vibrant colors.
Overall, a great smartphone that delivers a premium user experience!
""")

print(result)