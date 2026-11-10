from pydantic import BaseModel, Field 
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# schema
class Student(BaseModel):
    name: str
    age: int
    grade: Optional[str] = Field(description="The grade of the student, e.g., '10th grade'")

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
structured_model = model.with_structured_output(Student)

result = structured_model.invoke("""John is a diligent student who consistently performs well in his studies. He is currently 16 years old . John is known for his excellent academic record and his dedication to learning. He is also actively involved in extracurricular activities, demonstrating leadership and teamwork skills. Overall, John is a well-rounded student with a bright future ahead of him.
""")
print(result)