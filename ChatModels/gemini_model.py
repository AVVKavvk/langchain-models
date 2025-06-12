from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result = gemini_model.invoke("Hello, how are you?")
print(result)