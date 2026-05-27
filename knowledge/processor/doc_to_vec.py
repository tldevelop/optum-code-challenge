import sys
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from typing import Dict, List

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

sys.path.append(ROOT_DIR)

DOC_DIR = os.path.join(
    ROOT_DIR,
    "knowledge",
    "raw"
)

from back.utils.supabase_connection import supabase

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents:List[Document] = []

policy_files:List[Dict] = [
    {
        "filename":"policy_claims.txt",
        "policy_type":"claims_policy"
    },
    {
        "filename":"policy_glp.txt",
        "policy_type":"glp_policy"
    },
    {
        "filename":"policy_provider.txt",
        "policy_type":"provider_policy"
    }
]

for policy in policy_files:
    file_path = os.path.join(
        DOC_DIR,
        policy["filename"]
    )

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    document = Document(
        page_content=content,
        metadata={
            "source":policy["filename"],
            "policy_type": policy["policy_type"]
        }
    )

    documents.append(document)

for doc in documents:
    embedding = embeddings.embed_query(
        doc.page_content
    )

    data:Dict = {
        "content":doc.page_content,
        "metadata":doc.metadata,
        "embedding":embedding
    }

    supabase.table(
        "policy_documents"
    ).insert(data).execute()

    print(
        f"Inserted: {doc.metadata['source']}"
    )

print("All documents indexed!")