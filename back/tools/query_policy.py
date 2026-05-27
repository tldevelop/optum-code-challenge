from back.tools.utils.vector_connection import query_policy_documents
from back.tools.schemas import QueryPolicyInput
from langchain_core.tools import StructuredTool
from typing import List

def query_documents(
        query:str
) -> List:
    response = query_policy_documents(query)

    results:List = []

    for doc in response:

        results.append(
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            }
        )

    return results

query_policies_tool = StructuredTool.from_function(
    args_schema=QueryPolicyInput,
    func=query_documents,
    name="query_policies_tool",
    description="""
    Use this tool for:
    - policy questions
    - GLP-1 coverage
    - denial reasons
    - provider review policies
    - healthcare approval rules
    """
)