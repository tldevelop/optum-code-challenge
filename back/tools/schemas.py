from pydantic import BaseModel, Field

class QueryPolicyInput(BaseModel):
    query:str = Field(description="The query you need to perform over policy documents")

class QueryClaimsToolInput(BaseModel):
    query:str = Field(description="The query you need to perform over the claims dataset")