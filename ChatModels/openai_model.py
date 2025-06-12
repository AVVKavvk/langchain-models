from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4") # temperature, max_completion_tokens

result = model.invoke("Hello, how are you?")
print(result)