# app.py

import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# LangChain Tools & Models
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

# LangGraph
from typing_extensions import TypedDict
from typing import Annotated
from langchain_core.messages import AnyMessage, HumanMessage
from langgraph.graph import add_messages, StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

# Setup tools
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=500)
arixv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv, description="Query arxiv papers")

api_wrapper_wikipedia = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper_wikipedia, description="Query Wikipedia articles")

tavily = TavilySearchResults()
tools = [arixv, wikipedia, tavily]

# LLM Setup
llm = ChatGroq(model="qwen-qwq-32b")
llm_with_tools = llm.bind_tools(tools=tools)

# Define LangGraph Agent State
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

# Node function
def tool_calling_llm(state: AgentState) -> AgentState:
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Build LangGraph
builder = StateGraph(AgentState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges("tool_calling_llm", tools_condition)
builder.add_edge("tools", END)
graph = builder.compile()

import streamlit as st
from langchain_core.messages import HumanMessage

# Page configuration
st.set_page_config(page_title=" AI Research Agent", layout="wide")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=80)
    st.markdown("# AI Research Agent")
    st.markdown(
        """
        Unlock powerful research at your fingertips!  
        
        1.  Access real-time data from **arXiv**, **Wikipedia**, and the **web**  
        2.  Ask anything about **AI**, **Machine Learning**, **RAG**, **Agents**, and more  
        3.  Powered by **LangGraph** + **LLM tools**
        """
    )
    st.markdown("---")
    st.markdown("Start exploring the frontiers of AI research now!")



# Main Title
st.markdown("<h1 style='text-align: center;'> AI Research Agent</h1>", unsafe_allow_html=True)

# Add spacing
st.markdown("###")
st.markdown("### 🔍 Ask your research question below")

# Styled input box inside a container
with st.container():
    query = st.text_input(
        "Query:",
        placeholder="E.g., What is the latest research on AI agents?",
        key="user_query",
        label_visibility="collapsed"
    )

    submitted = st.button(" Submit")

# Processing query
if submitted or query:
    if query.strip() == "":
        st.warning("⚠️ Please enter a valid query.")
    else:
        with st.spinner("🤖 Thinking..."):
            result = graph.invoke({"messages": HumanMessage(content=query)})
            st.success("✅ Response received!")

            st.markdown("### 💬 Response")
            for msg in result["messages"]:
                with st.expander(f"{msg.type.title()} Message"):
                    st.markdown(msg.content)
                   
# Footer
st.markdown("---")
st.caption("Made with ❤️ using LangGraph, Streamlit, and LLM tools.")
