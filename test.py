import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model ="gemini-2.5-flash",
    temperature=0.4,
    max_tokens=500
)

response = llm.invoke("Hello, how are you?")
print(response)