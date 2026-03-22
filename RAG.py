""" 
RAG pipeline
Usually when some chatbots are created but personalising is different and makes it more accurate and perosonal style

Documents --> Chunking --> Embedding --> Vector Storage --> Similarity Search --> Retriever --> LLM --> Reranker-->Output

Take the input text do, chunking and tokenisation 
then use embedding  and convert them to numerical values
store the embeddings and when the user asks for query use the similarity searches 
then use a retriever to retrieve the data later use a reranker to rank the answers and provide the output """

1. 🔹 Better Chunking
Recursive chunking
Semantic chunking

👉 Improves retrieval quality

🔹 Prompt Engineering
👉 Reduces hallucination

🔹 Metadata Filtering
Filter by:
document type
date
source
