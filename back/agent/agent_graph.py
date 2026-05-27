from langchain.agents import create_agent
from back.llm.get_openai_llm import get_openai_llm
from back.agent.prompts.system_prompt import system_prompt
from back.tools.query_claims import query_claims_tool
from back.tools.query_policy import query_policies_tool
from typing import Dict, List

#get the llm we will use
llm = get_openai_llm(
    model_name="gpt-4o-mini",
    model_temperature=0,
    model_max_tokens=620
)

tool_list:List = [
    query_claims_tool,
    query_policies_tool
]

stream_config:Dict = {
    "recursion_limit":6
}

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    tools=tool_list
).with_config(stream_config)