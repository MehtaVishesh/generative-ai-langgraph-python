# LangGraph Agent Workflows

A collection of stateful AI workflows built with **LangGraph, LangChain, and Python**. This repository explores graph-based orchestration, conditional routing, checkpointing, retrieval-augmented generation, and human-in-the-loop interactions.

## Projects

### 1. Stateful CLI Chatbot

A command-line chatbot that maintains conversation state across interactions.

- Define workflow state and graph execution.
- Manage conversation threads.
- Use checkpointing to retain state between graph invocations.

### 2. Intent-Routed Multi-Agent Workflow

A graph-based workflow that directs incoming questions to specialised handlers.

- Use structured output to classify user intent.
- Route coding, weather, and web-search requests through conditional edges.
- Integrate external tools for search and weather information.
- Manage workflow execution through a LangGraph state graph.

**Technologies:** Python, LangGraph, LangChain, Pydantic, OpenWeatherMap, Google Serper.

### 3. PDF Retrieval-Augmented Generation

A document question-answering workflow that retrieves relevant information from PDF files.

- Load and split document content.
- Generate embeddings and index document chunks.
- Retrieve relevant context for incoming questions.
- Integrate retrieval into a graph-based workflow.

### 4. Human-in-the-Loop Email Workflow

An email-drafting workflow that incorporates human review and feedback.

- Generate an initial email draft.
- Pause workflow execution for human review.
- Process feedback and revise the draft.
- Use conditional routing to continue or revise the workflow.

## Key concepts

- Graph state, nodes, and edges.
- Conditional routing and specialised agent workflows.
- State persistence through checkpointing.
- Human review, interrupts, and workflow resumption.
- Retrieval-augmented generation and external tool integration.

## Prerequisites

- Python version compatible with the project dependencies.
- Git.
- Jupyter Notebook or JupyterLab for notebook-based examples.
- API keys for the model and external services used by each workflow.

## Installation

Clone the repository:

```bash
git clone https://github.com/MehtaVishesh/generative-ai-langgraph-python.git
cd generative-ai-langgraph-python
```

Create and activate a virtual environment.

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Create a `.env` file with the credentials required by the workflow you want to run.

```dotenv
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
```

Use the variable names expected by the selected notebook or application. Replace the placeholders with valid credentials.

## Run the examples

Launch JupyterLab:

```bash
jupyter lab
```

Open the relevant notebook and execute its cells in order. Review its configuration section before running model calls or external API requests.

## Suggested reading order

1. Stateful CLI chatbot — understand graph state and checkpointing.
2. Intent-routed workflow — explore structured output and conditional edges.
3. PDF RAG workflow — connect retrieval to graph execution.
4. Human-in-the-loop email workflow — examine interrupts, feedback, and workflow resumption.

## Author

**Vishesh Mehta** — AI Engineer, Melbourne, Australia.

[GitHub](https://github.com/MehtaVishesh) · [LinkedIn](https://www.linkedin.com/in/vishesh-mehta-516427217/)
