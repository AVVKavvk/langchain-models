from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openai_llm = OpenAI(model="gpt-3.5-turbo-instruct",api_key=os.getenv("OPENAI_API_KEY"))

result = openai_llm.invoke("Hello, how are you?")
print(result)