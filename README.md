# GenAI & Agentic AI Showcase

Showcasing various GenAI and agentic AI capabilities using LangChain, LangGraph, and LLM models. This project demonstrates the evolution from basic LLM chains to complex agents with reasoning, tool usage, and human-in-the-loop interactions.

## Description

This project highlights AI capabilities from simple text generation to complex agentic systems that use tools, search the web, and interact with humans. It integrates models like OpenAI's GPT series and HuggingFace models with frameworks like LangChain and LangGraph to create sophisticated AI systems.

## Prerequisites

- Python 3.7+
- OpenAI API key (for OpenAI models)
- HuggingFace API token (for HuggingFace models)
- Tavily API key (for search capabilities)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API credentials:

   For OpenAI:
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```

   For HuggingFace:
   ```bash
   export HUGGINGFACEHUB_API_TOKEN='your-huggingface-api-token'
   ```

   For Tavily Search:
   ```bash
   export TAVILY_API_KEY='your-tavily-api-key'
   ```

## Usage

Each Python file demonstrates different GenAI capabilities and can be run individually:

```bash
python simple-chain.py
python sequential-chain.py
python chatbot.py
python langgraphing.py
python human-in-the-loop.py
python agents.py
```

For Jupyter notebooks:

```bash
jupyter notebook
# Then open vector-db-demo.ipynb or langgraph_chatbot_human-in-the-loop.ipynb
```

## Project Files and Capabilities

### Foundation: Basic LLM Interaction
- **simple-chain.py**: Demonstrates a basic LLM chain for generating food tips using a simple prompt template.
- **sequential-chain.py**: Shows how to chain multiple LLM calls in sequence to generate a recipe, calculate cooking time, and analyze nutritional value.

### Conversation and Memory
- **chatbot.py**: Implements a basic chatbot using LangGraph for message management and conversation state.

### Advanced Agents and Tool Use
- **langgraphing.py**: Creates an agent with web search capabilities using LangGraph and the Tavily search tool.
- **agents.py**: Demonstrates ReAct (Reasoning and Acting) agents that can search YouTube and the web to answer complex questions.

### Human-AI Collaboration
- **human-in-the-loop.py**: Implements human approval for agent actions, allowing users to approve or reject tool executions before they happen.
- **langgraph_chatbot_human-in-the-loop.ipynb**: Jupyter notebook showing a chatbot with human escalation capabilities.

### Vector Databases and Embeddings
- **vector-db-demo.ipynb**: Demonstrates embedding generation, storage, and similarity search using OpenAI embeddings and FAISS.

## Features

- **Multi-model support**: Works with OpenAI GPT models and HuggingFace models
- **Prompt engineering**: Examples of effective prompt templates and chaining
- **Tool integration**: Integration with YouTube search and web search tools
- **Human-in-the-loop**: Workflows that include human approval and interaction
- **Vector embeddings**: Storage and retrieval of semantically similar content
- **Agent frameworks**: Both LangChain agents and LangGraph for complex agent behavior
- **Memory systems**: Conversation memory handling in agents and chatbots

## Contributing

Feel free to submit issues and pull requests.