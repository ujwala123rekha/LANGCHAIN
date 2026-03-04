"""So our next improvement of the model is changing/developing the output more convinient to user 

      StrOutputParser
      JsonOutputParser
      PydanticOutputParser
      StructuredOutputParser
      RegexParser

out of all lets focus on the StrOutputParser and PydanticOutputParser

1.StrOutputParser

      from langchain_core.output_parsers import StrOutputParser
      
      parser = StrOutputParser()
      
      chain = prompt | model | parser
      
or 

2.Pydantic

   It structures the output format .
   
   It can include fields like answer, confidence, sentiment, etc.
   
3. RunnableSequence

   prompt | model | parser
   
   Each component passes its output to the next component.
   
4.Streaming : 

      instead of generating answer at a time and giving once...this feels good understanding by displaying what it generates slowly 
      
Streaming allows the LLM to return tokens as they are generated

instead of waiting for the full response.

Benefits:

        - faster user feedback
        - real-time interaction
        - better UX in chat applications
        
5.Runnable Parallel:

  It helps in running two diff sysetm where one generates answers and other summarises them
  
  RunnablePassthrough forwards the original input unchanged
  
  so it can be used in multiple parts of the chain.

    In RAG pipelines, it allows the original question to be passed
    
    alongside the retrieved context to the prompt.
"""
#This includes StrOutputParser and streaming only 
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = "gemma3:4b",temperature = 0)
prompt = ChatPromptTemplate.from_messages([
  ("system","You are a helpful assistant"),
  ("user","{question}")])
parser = StrOutputParser()
chain = prompt | model | parser

while True:
  user_input = input("Enter the question : ")
  if user_input.lower() in {"quit","exit","bye"}:
    print("Have a nice day")
    break
  for chunk in chain.stream({"question": user_input}):
    print(chunk,end=" ",flush = True)
  print()

#This is finalise Pydantic,streaming and runnable parallel
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableParallel
from pydantic import BaseModel, Field


model = ChatOllama(
    model="gemma3:4b",
    temperature=0
)

class AnswerSchema(BaseModel):
    answer: str = Field(description="Answer to the question")
    confidence: float = Field(description="Confidence score between 0 and 1")

parser = PydanticOutputParser(pydantic_object=AnswerSchema)

format_instructions = parser.get_format_instructions()


answer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful AI assistant. Return the answer in JSON format."),
    
    ("user",
     "Question: {question}\n\n{format_instructions}")
])

answer_chain = answer_prompt | model | parser


summary_prompt = ChatPromptTemplate.from_messages([
    ("system","You summarize answers briefly."),
    ("user","Summarize this question: {question}")
])

summary_chain = summary_prompt | model | StrOutputParser()


parallel_chain = RunnableParallel(
    structured_answer=answer_chain,
    summary=summary_chain
)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in {"exit","quit","bye"}:
        print("AI: Goodbye!")
        break

    print("\nAI thinking...\n")

    result = parallel_chain.invoke({
        "question": user_input,
        "format_instructions": format_instructions
    })

    structured = result["structured_answer"]

    print("Answer:", structured.answer)
    print("Confidence:", structured.confidence)

    print("\nSummary:", result["summary"])

  
#Usually the model recieves the question then gives to retriever get the relevent context 
#Then we sent it to prompttemplate but.......
#To answer it more accurately we need both parameters as question and context so we use...
#Runnable passthorugh it just passes the copy of question to the prompt 

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel


model = ChatOllama(
    model="gemma3:4b",
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
""")


def fake_retriever(question):
    return "Artificial Intelligence is the simulation of human intelligence in machines."

chain = (
    {
        "context": fake_retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in {"exit","quit","bye"}:
        print("AI: Goodbye!")
        break

    print("\nAI: ", end="", flush=True)

    for chunk in chain.stream(user_input):
        print(chunk, end="", flush=True)

    print()
