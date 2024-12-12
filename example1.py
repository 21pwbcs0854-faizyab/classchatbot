# chat service with chroma
import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()

LLM = ChatOpenAI(model = 'gp-4o-mini')
# retriver= get_retriver()

prompt = ChatPromptTemplate.from_template(
    """ You can answer any type of question from this data
    
      this is topic :(question)
"""
)
chain = prompt | LLM | StrOutputParser
# response = (chain.invoke({'question': "dogs"}))

response = chain.stream({'question': "dogs"})

for r in response:
    print(r, end="", flush= True)