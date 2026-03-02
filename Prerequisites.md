
📘 LANGCHAIN – COMPLETE THEORY GUIDE

1️⃣ What is LangChain?
LangChain is an application framework for building applications powered by Large Language Models (LLMs).
An orchestration layer between application and model :A composable runtime for LLM workflows and  a modular system for AI pipelines

It provides structured components to:

    Connect LLMs
    Manage prompts
    Add memory
    Integrate external tools
    Build RAG systems
    Create multi-step reasoning workflows

LangChain does not create models.
It orchestrates them.

2️⃣ Why Use LangChain? (Advantages)
    
✅ 1. Model Abstraction
Switch between models (OpenAI, Ollama, Hugging Face) with minimal code change.

✅ 2. Prompt Management
Reusable and structured prompt templates.

✅ 3. Memory Handling
Maintains conversation history.

✅ 4. RAG Support
Easy integration of retrieval + LLM.

✅ 5. Tool Integration
Allows models to use tools (APIs, calculators, databases).

✅ 6. Modular Design
Build complex workflows using chains and runnables.

3️⃣ Core Terms in LangChain (One-Line Meanings)

Here are the most important terms you must know:

🔹 LLM
A large language model that generates text responses.
Example:
      GPT
      LLaMA
      Mistral
      
🔹 Chat Model
A structured LLM using message roles:
      system
      user
      assistant
Used in conversational systems.

🔹 Chain
A sequence of components connected together (Prompt → Model → Output).

🔹 Prompt Template
A structured format for sending dynamic input to the model.
Example:
("user", "{question}")

🔹 Runnable
Core abstraction in modern LangChain.
Everything is a Runnable:
      Model
      Prompt
      Retriever
      Tool
Runnables support:
      .invoke()
      .batch()
      .stream()
      .ainvoke() (async)
This is very important for advanced systems

🔹 Output Parser
Transforms model output into:
      JSON
      Structured objects
      Pydantic models
Used for structured generation.

🔹 Embeddings
Numerical vector representation of text.
Used for:
Similarity search
RAG systems

🔹 Vector Store
Stores embeddings for retrieval.
Examples:
      FAISS
      Chroma
      Pinecone
Used in RAG pipelines.

🔹 RAG (Retrieval-Augmented Generation)
A system that retrieves relevant documents before generating an answer.

🔹 Retriever
Component that fetches relevant documents from a vector database.

🔹 Memory
Stores previous interactions to maintain context.
Types:
ConversationBufferMemory
SummaryMemory
TokenBufferMemory

🔹 Tool
External function that the LLM can call.

🔹 Agent
An intelligent system that decides which tool to use dynamically.
      Decides what action to take
      Chooses tools dynamically
      Executes multi-step reasoning
🔹 Document Loaders

Load data from:
PDFs
Websites
Notion
CSV
Markdown

🔹 Text Splitters
Split long documents into chunks before embedding.
This is critical in real-world RAG pipelines.

4️⃣ LangChain Internal Structure (High-Level Architecture)

Modern LangChain is modular.
It mainly consists of:
📦 1. langchain-core

    Base abstractions
    Runnables
    Prompts
    Messages
    Interfaces

📦 2. langchain-community

    Third-party integrations
    Vector stores
    External tools
    Model connectors

📦 3. Provider Packages
    
    Examples:
    langchain-openai
    langchain-ollama
    langchain-huggingface
These connect LangChain to actual LLM providers.

5️⃣ How LangChain Works Internally
                                                              User Input
                                                                 ↓
                                                              Prompt Template
                                                                 ↓
                                                              LLM (Model)
                                                                 ↓
                                                              Output Parser
                                                                 ↓
                                                              Final Response
                                          
  With RAG:
                                          
                                          User Query
                                             ↓
                                          Retriever
                                             ↓
                                          Relevant Documents
                                             ↓
                                          Prompt Template
                                             ↓
                                          LLM
                                             ↓
                                          Answer

Agent Types :
        ReAct
        Tool-calling agents
        OpenAI function agents
        Plan-and-execute agents
        Self-reflection agents

Agents are more complex than just “choosing tools”.
6. How to Install LangChain
pip install langchain
