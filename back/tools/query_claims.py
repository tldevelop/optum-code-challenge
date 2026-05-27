from back.agent.postgres_agent import postgres_agent
from back.tools.utils.db_connection import engine
from back.tools.schemas import QueryClaimsToolInput
from langchain_core.tools import StructuredTool
from sqlalchemy import text
from typing import Dict

def query_claims(
        query:str
) -> Dict:
    
    result = postgres_agent.invoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":query
                }
            ]
        }
    )

    sql_query = (
        result["messages"][-1].content
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    try:
        with engine.connect() as connection:
            result = connection.execute(
                text(sql_query)
            )

            rows = [
                dict(row._mapping)
                for row in result
            ]

            return {
                "question": query,
                "generated_sql": sql_query,
                "results": rows
            }
    except Exception as e:
        return {
            "question": query,
            "generated_sql": sql_query,
            "error": str(e)
        }
    


query_claims_tool = StructuredTool.from_function(
    args_schema=QueryClaimsToolInput,
    func=query_claims,
    name="query_claims_tool",
    description="""
    Use this tool for:
    - claims analytics
    - cost analysis
    - provider analysis
    - aggregations
    - trends
    - SQL-based healthcare questions

    Examples:
    - Total spend for Ozempic
    - Average out-of-pocket cost
    - Highest cost providers
    - Denied claims analysis
    """
)