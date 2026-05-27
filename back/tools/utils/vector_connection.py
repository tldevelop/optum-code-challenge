import os
from back.utils.supabase_connection import supabase
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_storage = SupabaseVectorStore(
    client=supabase,
    embedding=embeddings,
    table_name="policy_documents",
    query_name="match_policy_documents"
)

def query_policy_documents(
        query:str,
        k:int = 3
):
    docs = vector_storage.similarity_search(
        query=query,
        k=k
    )

    return docs