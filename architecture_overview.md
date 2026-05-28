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

