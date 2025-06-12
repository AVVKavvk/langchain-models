from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_model = ChatAnthropic(model_name="claude-2-100k",timeout=30,stop=["\n"])

result = anthropic_model.invoke("Hello, how are you?")
print(result)