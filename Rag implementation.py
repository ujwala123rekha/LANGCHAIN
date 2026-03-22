# Install required:
# pip install langchain langchain-community langchain-ollama faiss-cpu

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1️⃣ Load documents
loader = TextLoader("data.txt")   # your file
documents = loader.load()

# 2️⃣ Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# 3️⃣ Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 4️⃣ Vector DB
vectorstore = FAISS.from_documents(docs, embeddings)

# 5️⃣ Retriever (Top-K)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6️⃣ LLM
model = ChatOllama(model="gemma3:4b", temperature=0)

# 7️⃣ Prompt (Context Injection)
prompt = ChatPromptTemplate.from_template("""
Answer the question using ONLY the context below.
If you don't know, say "I don't know".

Context:
{context}

Question:
{question}
""")

# 8️⃣ RAG Chain
chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | model
    | StrOutputParser()
)

# 9️⃣ Chat loop
while True:
    query = input("\nYou: ")

    if query.lower() in {"exit", "quit", "bye"}:
        print("AI: Goodbye!")
        break

    print("\nAI: ", end="")

    for chunk in chain.stream(query):
        print(chunk, end="")

    print()
