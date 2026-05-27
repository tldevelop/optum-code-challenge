from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv())

def get_openai_llm(
        model_name:str,
        model_temperature:int,
        model_max_tokens:int
) -> ChatOpenAI:
    """
    This function retrieves any OpenAI LLM for a langchain/langgraph
    workflow, accepts model name, temperature and max tokens as args
    for essential configuration
    """

    llm = ChatOpenAI(
        model=model_name, 
        temperature=model_temperature, 
        max_tokens=model_max_tokens
    )

    return llm