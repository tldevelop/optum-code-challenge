# Architecture Overview
In this document we will cover how this project was made, the technologies selected
architecture flow, weakpoints or areas of improvement and next steps to fix this and make it
more robust and ready for a first production version

## Challenge
The challenge requires an AI solution capable of query over structured and unstructured data (text documents)
so it can answer questions related to the data using natural language, the solution should also provide some data analitics
capabilities, the solution should have the hability to decide which knowledge source to query based in the question and
for some special cases use both sources, provide the queries used and the data referenced to support it's answer

It requires a simple but functional UI

## Initial reasoning
To save development time I focused into using solutions that can give me a lot of time savings but at the same time be 
strong or robust enough for the prototype

For the UI I decided to use Chainlit as it integrates very easily with LangChain and LangGraph and is an out of the box
solution for building fast and reliable interfaces for Chat and Agentic solutions

Supabase offers a very easy to use infrastructure without the all the workload to make a backend from scratch, and also it
provides both of the needed DB solutions required for this challenge, PostgreSQL DB for the claims structured data and a vector
DB version of it for the policies documents

LangChain will help us a lot of time at the moment of building the agentic solution thanks to it's prebuilt graphs

As the solution should have the hability to reason which data source to query based in the question, a classsi RAG approach would not be
the best for this, so an Agentic solution would be better making use of a ReAct agent and tools for each data source

I decided to work with OpenAI models mainly the GPT-4o-mini and the text-embedding-3-small for saving costs and fast inference to reduce a bit
the latency and for vectorize and embbed the documents in a "compatible" way

## Brief textual description of the architecture
The task mention to deliver backend and front end code but my approach makes it a 3 separated services
- A service to process the documents and embed them into the vector DB using text-embedding-3-small
- The Agent code or the Agent backend
- The Chainlit front end integration

### Document processing service
The document processor takes the documents from the project root and extracts it's content with the Open function
then those documents are put into a list with the corresponding metadata, after that a loop processes the documents with
the embedding model selected (living in a reusable function) and adds them into the vector DB
Perhaps the structured data was uploaded manually using the import CSV function in the supabase panel we can also add a
script to update the DB and avoid duplicates and all that

### Agent service
Using the prebuilt ReAct agent graph from langchain, the agent have access to 2 tools made using the structured tool approach, one tool is
designed specifically to query over the claims data and the other to query over the policies documents, the tool that queries the claims data uses an LLM
layer to analyze the query passed by the main agent and given explicit PostgreSQL rules and table context in the system prompt for security reasons
it generates the adequate query avoiding delete, update queries and focusing only in retrieval queries, average, sum and grouping for some analysis tasks,
the tooln that queries the policy documents use the same embedding model to transform the query and send it to the DB and return the k=3
With some prompt engineering techniques I indicate the ReAct agent when to use each tool based in an analysis of the question and how to handle questions that
involve querying both data sources

### Front end service
The front end is managed by chainlit an out of the box solution that delivers a ChatGPT like UI, it imports and connects directly to the main agent graph
perfeclty defining the user role for the incoming message for having some security using prompt isolation

*A little extra*
Here you have a basic diagram of the architecture
[Architecture Diagram]()

## Limitations, improvements and next steps
- Improve data processing layer to support bigger text documents, implement chunking based in the document needs (fixed, sentence, recursive for paragraphs and related,
document specific chunking), chunking overlap, rerank techniques for results, hybrid search, avoid duplicated documents, use of MMR for larger and very similar documents
if needed (also apply the same principles into the policies tool)
- Add a function to keep the claims data updated in the DB and avoid duplicates so the data keeps up to date automatically if there not will be a direct process or integration
that will be updating it
- Improve query generation and add guardrails to the tool that query claims data, think of fixed most used queries and make tools for each type could be a solution to have
more security over the queries executed, also having some validation layers such as the use of a guardrail API or solution such as OpenAI moderation API, human in the loop for query approval and review
- Refine main agent system prompt for better handling ambiguity and other edge cases
- Add memory so the agent can remember data in more complex or deeper conversations
- Improve the front end by using a custom and more robust solution
- Add observabilty tools such as LangSmith or LangFuse and other governability solutions such as datadog
- Include tool & input validations and other guardrail layers to preserve the integrity of data 
- Wrap the agent service in a Rest API or websocket
- Add unit testing for code and testing SDKs or libraries for agentic solutions such as AI foundry evaluators
