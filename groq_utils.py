from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(api_key=groq_api_key,model_name="gemma2-9b-it",)

def summarize_article(article_text):
  prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an AI journalist. Your job is to simplify and summarize news articles in plain English."),
    ("human", "Summarize the following news article in a clear and simple way:\n\n{article}")
  ])
  chain=prompt|llm
  response=chain.invoke({"article":article_text})
  return response.content