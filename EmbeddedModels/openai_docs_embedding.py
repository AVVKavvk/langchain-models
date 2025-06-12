from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-ada-002",dimensions=32)

docs =[
  "Vipin loves cricket",
  "Vipin is a good cricketer",
  "Vipin is a good bowler",
]
result = embedding.embed_documents(docs)
print(str(result))