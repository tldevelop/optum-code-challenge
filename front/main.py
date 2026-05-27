import chainlit as cl
import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(ROOT_DIR)

from back.agent.agent_graph import agent

@cl.on_message
async def main(message:cl.Message):

    response = await agent.ainvoke(
        {
            "messages":[
                {
                    "role":"user",
                    "content":message.content
                }
            ]
        }
    )

    await cl.Message(
        content=response["messages"][-1].content
    ).send()

    