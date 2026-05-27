from langchain.agents import create_agent
from back.llm.get_openai_llm import get_openai_llm
from back.agent.prompts.query_generator import query_generator_prompt

#get the llm we will use
llm = get_openai_llm(
    model_name="gpt-4o-mini",
    model_temperature=0,
    model_max_tokens=620
)

postgres_agent = create_agent(
    model=llm,
    system_prompt=query_generator_prompt
)