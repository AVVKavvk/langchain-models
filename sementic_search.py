from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-ada-002",dimensions=300)

docs =[
  "Vipin is a software developer with 1 year of experience",
  "Rahul is a Mtech student at IIT",
  "Mitilesh is a Income Tax Officer",
  "Sachin is a CA (Chartered Accountant)",
]

query = "who is software developer"

docs_embeddings = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], docs_embeddings)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print(score)