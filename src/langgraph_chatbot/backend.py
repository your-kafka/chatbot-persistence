from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from typing import TypedDict, Annotated 
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph.message import add_messages


load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b")

class botState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def ans(state: botState):
    prompt = f'Answer this thing asked by the user : {state['messages']}, keep the answer short and crisp under 20 words.'
    response = model.invoke(prompt)
    return {'messages':[response]}

graph = StateGraph(botState)

graph.add_node('answer', ans)

graph.add_edge(START, 'answer')
graph.add_edge('answer', END)

config1 = {'configurable':{'thread_id':1}}

checkpointer = InMemorySaver()

chatbot = graph.compile(checkpointer=checkpointer)