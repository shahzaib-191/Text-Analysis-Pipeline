import os
from typing import TypedDict, List
import streamlit as st # type: ignore
from langgraph.graph import StateGraph, END # type: ignore
from langchain.prompts import PromptTemplate # type: ignore
from langchain_core.runnables.graph import MermaidDrawMethod # type: ignore
from langchain.schema import HumanMessage # type: ignore
from IPython.display import display, Image # type: ignore
from langchain_groq import ChatGroq # type: ignore
from dotenv import load_dotenv # type: ignore

#venv\Scripts\activate

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')


# Initialize Groq model (use your Groq model here)
llm = ChatGroq( model="llama-3.1-70b-versatile", temperature=0)
# Define the State class to hold workflow data
# Define the state for the workflow
# Define the state for the workflow
class State(TypedDict):
    text: str
    classification: str
    entities: List[str]
    summary: str
    sentiment: str
    keywords: List[str]
    context: str


# Define node functions
def classification_node(state: State):
    '''Classify the text into a dynamic category based on the content.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Based on the following text, please provide a category that best describes it. You can use categories such as News, Blog, Research, Entertainment, Technology, Health, or others.\n\nText: {text}\n\nCategory:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    classification = llm.predict_messages([message]).content.strip()
    return {"classification": classification}

def entity_extraction_node(state: State):
    '''Extract all the entities (Person, Organization, Location) from the text.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma-separated list.\n\nText:{text}\n\nEntities:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    entities = llm.predict_messages([message]).content.strip().split(", ")
    return {"entities": entities}

def summarization_node(state: State):
    '''Summarize the text in one short sentence.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text in one short sentence.\n\nText:{text}\n\nSummary:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    summary = llm.predict_messages([message]).content.strip()
    return {"summary": summary}

def sentiment_analysis_node(state: State):
    '''Determine the sentiment of the text: Positive, Negative, or Neutral.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Analyze the sentiment of the following text and classify it as Positive, Negative, or Neutral.\n\nText:{text}\n\nSentiment:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    sentiment = llm.predict_messages([message]).content.strip()
    return {"sentiment": sentiment}

def keyword_extraction_node(state: State):
    '''Extract keywords from the text.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract key phrases or keywords from the following text. Provide the result as a comma-separated list.\n\nText:{text}\n\nKeywords:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    keywords = llm.predict_messages([message]).content.strip().split(", ")
    return {"keywords": keywords}

def context_analysis_node(state: State):
    '''Identify the broader context or theme of the text, like Business, Technology, Health, etc.'''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Identify the context or theme of the following text. Is it about Business, Technology, Health, Entertainment, or something else?\n\nText:{text}\n\nContext:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    context = llm.predict_messages([message]).content.strip()
    return {"context": context}

# Create the StateGraph workflow
workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("classification_node", classification_node)
workflow.add_node("entity_extraction_node", entity_extraction_node)
workflow.add_node("summarization_node", summarization_node)
workflow.add_node("sentiment_analysis_node", sentiment_analysis_node)
workflow.add_node("keyword_extraction_node", keyword_extraction_node)
workflow.add_node("context_analysis_node", context_analysis_node)

# Define the edges and flow between the nodes
workflow.set_entry_point("classification_node")  # Start with classification
workflow.add_edge("classification_node", "entity_extraction_node")
workflow.add_edge("entity_extraction_node", "summarization_node")
workflow.add_edge("summarization_node", "sentiment_analysis_node")
workflow.add_edge("sentiment_analysis_node", "keyword_extraction_node")
workflow.add_edge("keyword_extraction_node", "context_analysis_node")
workflow.add_edge("context_analysis_node", END)  # End the workflow

# Compile the graph
app = workflow.compile()

# Streamlit UI for user input
st.title("Text Analysis Pipeline")
st.write("Provide a piece of text to analyze using this advanced text processing pipeline.")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze Text") and user_input:
    state_input = {"text": user_input}
    result = app.invoke(state_input)

    st.subheader("Analysis Results")
    st.write(f"**Classification:** {result['classification']}")
    st.write(f"**Entities:** {', '.join(result['entities'])}")
    st.write(f"**Summary:** {result['summary']}")
    st.write(f"**Sentiment:** {result['sentiment']}")
    st.write(f"**Keywords:** {', '.join(result['keywords'])}")
    st.write(f"**Context:** {result['context']}")

    st.success("Text analysis complete! Check out the details above.")
