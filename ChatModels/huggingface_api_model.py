from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
  task="text-generation",
)

hf_model = ChatHuggingFace(llm=llm)

result = hf_model.invoke("Hello, how are you?")
print(result)