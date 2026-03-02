""" 
 LangChain : It is an application framework for LLMs.

Model abstraction
Prompt management
Memory handling
Tool integration
RAG pipelines
Multi-step reasoning chains

Lets  see from starting clearly:

Here we implement the basic way of asking a model and we get the answers
     Firstly we need to choose the model : There are 2 types as open source and closed soource(black box) 
     for open source we can download the model and use them or closed there will be restricted access and payable
     Open source :Can be run locally or self-hosted and Full control over usage.
     closed source : Access via paid API and Limited customization.As OpenAI,Anthropic,Google Gemini
     So using open source we can download model using 
             Hugging face           ollama
     In hugging face get the name and use them 
     In Ollama download it with "ollama pull model_name:
     📌 Basic LangChain Flow
            User Input
               ↓
            Prompt Template
               ↓
            LLM
               ↓
            Response

     Lets start to code
     """
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model ="phi")
prompt = ChatPromptTemplate.from_messages([
  ("system","you are a helpful assistant "),
  ("user","{question}")])

chain = prompt | model
while True:
  user_input = input("Enter your question")
  if user_input.lower() in {"bye","goodbye","exit","quit"}:
    print("Have a good day,I am here to help always")
    break
  response= chain.invoke({"question":user_input})
  print(response.content)
