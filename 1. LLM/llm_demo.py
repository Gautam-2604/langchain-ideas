from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

llm = ChatOpenAI(model="allenai/olmo-3.1-32b-think:free", api_key=getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1",temperature=2)

answer = llm.invoke("What can be the capital of India ??")
print(answer)