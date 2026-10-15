"""Command-line Q&A chatbot built with LangGraph.

The graph passes ``ChatState`` through a Python-function node that calls the
chat model. An in-memory checkpointer stores state snapshots between calls.
The state contains the conversation messages; the checkpointer saves those
states, and the same thread ID tells LangGraph which conversation to resume.
In-memory checkpoints are temporary and are lost when the process exits.

Set ``GROQ_API_KEY`` in the environment (or in a local ``.env`` file) before
running this script. Enter ``quit`` or ``exit`` to stop the chat.
"""

from pydantic import BaseModel
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

# Configure the chat model used by the graph's chatbot node.
llm = ChatGroq(model="openai/gpt-oss-20b")


# State is the conversation data that flows through graph nodes.
class ChatState(BaseModel):
    messages: Annotated[list, add_messages]


graph_core = StateGraph(ChatState)


# A node is a Python function that reads the current state and returns updates.
def chatBotNode(state:ChatState) -> ChatState:
    res = llm.invoke(state.messages)
    state.messages.append(res)
    return state


# Connect the chatbot node between the graph's start and end.
graph_core.add_node("chatbot", chatBotNode)
graph_core.add_edge(START, "chatbot")
graph_core.add_edge("chatbot", END)

# Compile the graph with temporary, in-process checkpoint storage.
memory = InMemorySaver()
graph = graph_core.compile(checkpointer=memory)

# Reuse one thread ID so each turn continues the same checkpointed conversation.
thread_id = uuid4()

while True:
    query = input("User:")
    if query.lower() in ["quit", "exit"]:
        break
    res = graph.invoke(
        {"messages":[{"role":"user", "content":query}]},
        {"configurable":{"thread_id":thread_id}}
    )
    print("AI:", res["messages"][-1].content)