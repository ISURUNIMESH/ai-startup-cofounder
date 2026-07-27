#  AI Startup Co-Founder

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.54-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-blueviolet?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-RAG-00A67E?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-orange?style=for-the-badge)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM_API-6C47FF?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-High_Speed-black?style=for-the-badge)

</p>

<p align="center">
<b>An AI-powered Startup Validation Platform built using Multi-Agent AI, Retrieval-Augmented Generation (RAG), LangGraph, and Streamlit.</b>
</p>

---

## Project Description

**AI Startup Co-Founder** is an intelligent startup validation platform designed to assist entrepreneurs in evaluating and refining their startup ideas. Instead of relying on a single AI response, the system orchestrates multiple specialized AI agents, each responsible for a different stage of startup analysis.

The application follows a sequential multi-agent workflow where every agent contributes domain-specific knowledge, including idea validation, market research, business model generation, marketing strategy development, risk assessment, and final business evaluation. The workflow is managed using **LangGraph**, enabling structured agent communication and state management.

To improve the quality and relevance of AI responses, the system incorporates **Retrieval-Augmented Generation (RAG)** with **ChromaDB**, allowing the agents to retrieve contextual knowledge before generating outputs.

The platform integrates **OpenRouter** and **Groq** through a configurable model router, enabling flexible model selection based on speed, reasoning capability, and cost.

The final output is presented through a modern **Streamlit dashboard**, providing entrepreneurs with a structured startup validation report that supports informed decision-making. 

## Problem Statement

Many aspiring entrepreneurs have innovative startup ideas but struggle to evaluate their feasibility, market potential, business strategy, and associated risks before investing significant time and resources. Traditional validation methods often require extensive research, expert consultation, and market analysis, making the process time-consuming and costly.

While Large Language Models (LLMs) can provide useful insights, a single AI response often lacks structured analysis and domain-specific reasoning across different business aspects. This creates a need for an intelligent system that can perform comprehensive startup validation using specialized AI agents supported by external knowledge.

---

## Project Objectives

The primary objectives of this project are:

- Develop a multi-agent AI system for startup idea validation.
- Analyze startup ideas from multiple business perspectives.
- Integrate Retrieval-Augmented Generation (RAG) to provide context-aware responses.
- Orchestrate AI agents using LangGraph for structured workflows.
- Support multiple LLM providers through a configurable model router.
- Present startup evaluation results through an interactive Streamlit dashboard.

---

## Key Features

- Multi-Agent AI architecture
- LangGraph-based agent orchestration
- Retrieval-Augmented Generation (RAG) using ChromaDB
- Context-aware startup analysis
- Market research and competitor analysis
- Business model generation
- Marketing strategy recommendations
- Risk identification and mitigation suggestions
- Final startup evaluation and scoring
- Interactive Streamlit user interface
- Support for multiple LLM providers (OpenRouter and Groq)
- Structured JSON outputs for reliable agent communication 

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.11+ |
| Frontend | Streamlit |
| AI Framework | LangChain |
| Agent Orchestration | LangGraph |
| Vector Database | ChromaDB |
| LLM Providers | OpenRouter, Groq |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Environment Management | python-dotenv |
| Version Control | Git & GitHub |

---

## Model Choice Comparison

The application supports multiple Large Language Models (LLMs) through a configurable model router. Different models can be selected depending on the requirements of each AI agent.

| Sub-task | Model (Provider) | Latency | Cost per Token | Context Window | Reasoning Quality | Why Chosen |
|----------|------------------|---------|----------------|----------------|-------------------|------------|
| Primary Multi-Agent Analysis | Gemini 2.5 Flash Lite (OpenRouter) | Very Low | Low | Large | Good | Provides fast response generation, reliable structured JSON output, and cost-effective performance for sequential multi-agent workflows. |
| Advanced Reasoning (Optional) | DeepSeek R1 (OpenRouter) | Medium | Medium | Large | Excellent | Used for complex reasoning tasks where stronger reasoning quality is required. |
| Alternative Provider | Llama 3.3 70B (Groq) | Very Low | Low | Large | Very Good | Provides high-speed inference and serves as a reliable alternative provider when required. |

## Model Selection Strategy

The system is designed to support multiple LLM providers rather than relying on a single model. This approach allows each agent to use the most appropriate model based on its task requirements while balancing response quality, reasoning capability, execution speed, and operational cost. The model router enables easy configuration and future expansion without modifying the overall application architecture.


## Agentic AI Design Patterns

The AI Startup Co-Founder application implements multiple agentic AI design patterns to improve modularity, scalability, and reasoning quality throughout the startup evaluation workflow.

### 1. Orchestrator–Worker Pattern

The application uses **LangGraph** as the workflow orchestrator. LangGraph controls the execution order of all specialized AI agents. Each agent performs a dedicated task and updates the shared workflow state before passing it to the next agent.

**Implementation:**
- `graph/workflow.py`
- `graph/nodes.py`

---

### 2. Tool-Use Pattern

Each AI agent retrieves relevant contextual information from the **Retrieval-Augmented Generation (RAG)** pipeline before generating responses. The retrieved knowledge from the ChromaDB vector database enables the agents to produce more accurate and context-aware startup recommendations.

**Implementation:**
- `rag/retriever.py`
- `rag/vector_store.py`
- `rag/embeddings.py`

---

### 3. Router Pattern

The application includes a configurable **Model Router** that dynamically selects the appropriate Large Language Model (LLM) provider based on the application configuration. This allows the system to support both **OpenRouter** and **Groq** without changing the agent implementation.

**Implementation:**
- `utils/model_router.py`
- `config.py`


## System Architecture

The AI Startup Co-Founder application follows a modular multi-agent architecture. The user interacts with a Streamlit web interface, which sends the startup idea to a LangGraph workflow. Each AI agent performs a specialized task and passes its output to the next agent. The agents retrieve relevant knowledge from the ChromaDB vector database through a Retrieval-Augmented Generation (RAG) pipeline before generating responses using Large Language Models (LLMs). The final evaluation is displayed in the Streamlit dashboard.

### System Architecture Diagram

<p align="center">
  <img src="images/image 7.png" width="900">
</p>

## Agent Communication

The application follows a sequential multi-agent workflow orchestrated by LangGraph. Each agent is responsible for a specific stage of startup evaluation and passes its structured output to the next agent. This modular design ensures that every aspect of the startup idea is analyzed independently before producing the final evaluation.

### Agent Communication Mechanism

The application uses LangGraph's shared `StartupState` object for agent-to-agent communication. Each agent reads structured outputs generated by previous agents, performs its own specialised analysis, updates the shared state, and passes it to the next stage of the workflow. This approach enables structured communication between agents without direct messaging and ensures a consistent flow of information throughout the startup evaluation process.

### Agent Communication Diagram

<p align="center">
  <img src="images/image 8.png" width="200">
</p>

### Agent Responsibilities

| Agent | Responsibility |
|-------|----------------|
| Idea Agent | Evaluates the feasibility, uniqueness, and clarity of the startup idea. |
| Market Agent | Analyzes the target market, customer segments, competitors, and market opportunities. |
| Business Agent | Generates an appropriate business model and revenue strategy. |
| Marketing Agent | Recommends marketing channels, customer acquisition strategies, and branding approaches. |
| Risk Agent | Identifies potential technical, financial, operational, and market risks. |
| Reviewer Agent | Reviews the outputs of all previous agents and produces the final startup evaluation and overall score. |

## Retrieval-Augmented Generation (RAG) Pipeline

The AI Startup Co-Founder application uses a Retrieval-Augmented Generation (RAG) pipeline to improve the quality and relevance of AI-generated responses. Instead of relying only on the knowledge stored in Large Language Models (LLMs), the system retrieves relevant information from a local knowledge base before generating a response.

The knowledge base is created by processing startup-related documents, converting them into vector embeddings, and storing them in ChromaDB. When a user submits a startup idea, the system retrieves the most relevant document chunks and provides them as additional context to the AI agents. This enables the agents to generate more accurate, context-aware, and consistent recommendations.

### RAG Pipeline Diagram

<p align="center">
  <img src="images/image 9.png" width="300">
</p>

### RAG Workflow

1. Startup-related documents are collected and processed.
2. The documents are divided into smaller text chunks.
3. Each chunk is converted into vector embeddings.
4. The embeddings are stored in the ChromaDB vector database.
5. When a startup idea is submitted, a similarity search retrieves the most relevant document chunks.
6. The retrieved context is combined with the agent prompt.
7. The LLM generates a context-aware response using both the user input and the retrieved knowledge.


## Retrieval Evaluation

The retrieval pipeline was evaluated using five representative startup-related queries to verify the relevance of the retrieved context.

| Query | Retrieved Context | Result |
|-------|-------------------|--------|
| AI-powered Healthcare Assistant | Startup validation and healthcare business documents | Relevant |
| Smart Farming Platform | Agriculture and agritech startup documents | Relevant |
| Online Learning Platform | EdTech startup and business model documents | Relevant |
| Food Delivery Startup | Logistics and business strategy documents | Relevant |
| AI Recruitment System | HR technology and recruitment startup documents | Relevant |

The retrieved documents were relevant to each query and provided useful contextual information that improved the quality and consistency of the AI-generated responses.


## Chunking Strategy

The knowledge base is processed using LangChain's **RecursiveCharacterTextSplitter** before generating vector embeddings.

| Configuration | Value |
|--------------|-------|
| Chunk Size | 1000 characters |
| Chunk Overlap | 200 characters |
| Text Splitter | RecursiveCharacterTextSplitter |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |

This chunking strategy preserves contextual information while improving semantic retrieval accuracy.


## Project Structure

```text
AI-Startup-CoFounder/
│
├── agents/                  # AI agent implementations
├── graph/                   # LangGraph workflow
├── images/                  # Application screenshots and diagrams
├── rag/                     # RAG components
├── utils/                   # Utility functions
├── vector_db/               # ChromaDB vector database
├── .env                     # Environment variables
├── app.py                   # Streamlit application
├── config.py                # Application configuration
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── test_api.py
├── test_graph.py
├── test_loader.py
└── ...
```

---

## Setup Instructions

### Prerequisites

Before running the application, ensure the following software is installed:

- Python 3.11 or later
- Git
- A valid OpenRouter API Key
- (Optional) A Groq API Key

---

### Clone the Repository

```bash
git clone https://github.com/ISURUNIMESH/ai-startup-cofounder.git
cd ai-startup-cofound
```
---

### Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root and add your API credentials.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
GROQ_API_KEY=your_groq_api_key

FAST_MODEL=google/gemini-2.5-flash-lite
REASONING_MODEL=deepseek/deepseek-r1
```

---

### Run the Application

```bash
streamlit run app.py
```

After the application starts, open the local URL displayed in the terminal (typically `http://localhost:8501`) in your web browser.

## Application Workflow

The AI Startup Co-Founder application follows a structured workflow to evaluate startup ideas. Each AI agent performs a dedicated task and passes its output to the next stage, ensuring a comprehensive analysis.

### Workflow Steps

1. The user enters a startup idea through the Streamlit interface.
2. The Idea Agent evaluates the feasibility, clarity, and innovation of the idea.
3. The Market Agent analyzes the target market, competitors, and potential opportunities.
4. The Business Agent generates an appropriate business model and revenue strategy.
5. The Marketing Agent recommends customer acquisition and marketing strategies.
6. The Risk Agent identifies potential business, technical, financial, and operational risks.
7. The Reviewer Agent combines the outputs of all previous agents and generates the final startup evaluation.
8. The results are presented in the Streamlit dashboard.

---



## Application Screenshots

### Home Page

<p align="center">
  <img src="images/image 1.png" width="900">
</p>

*Figure 1. Home page of the AI Startup Co-Founder application.*

---

### Startup Idea Input

<p align="center">
  <img src="images/image 2.png" width="900">
</p>

*Figure 2. Startup idea submission interface.*

---

### Market Analysis

<p align="center">
  <img src="images/image 3.png" width="900">
</p>

*Figure 3. Market analysis generated by the AI agents.*

---

### Business Model

<p align="center">
  <img src="images/image 4.png" width="900">
</p>

*Figure 4. Business model recommendations.*

---

### Risk Analysis

<p align="center">
  <img src="images/image 5.png" width="900">
</p>

*Figure 5. Risk assessment generated by the Risk Agent.*

---

### Final Startup Evaluation

<p align="center">
  <img src="images/image 6.png" width="900">
</p>

*Figure 6. Final startup evaluation dashboard.*



## Live Demo

The application can be accessed through the following Streamlit deployment:

**Live Demo:**(https://startup-cofounder.streamlit.app/)


---

## Known Limitations

The current implementation has the following limitations:

- The quality of generated responses depends on the selected LLM.
- Internet connectivity is required to access external LLM providers.
- The knowledge base is limited to the documents indexed in the ChromaDB vector store.
- The system currently supports English-language startup analysis only.
- API rate limits or temporary service interruptions may affect response generation.
- Startup recommendations should be considered as decision-support suggestions rather than professional business advice.

---

## Future Improvements

The following enhancements are planned for future versions:

- Support for additional LLM providers.
- User authentication and personalized workspaces.
- Startup report export in PDF format.
- Multi-language support.
- Integration with external market intelligence APIs.
- Real-time collaboration for multiple users.
- Advanced analytics and visualization dashboard.
- Continuous knowledge base updates.

---

## Contributors

| Name | Role |
|------|------|
| K G I Nimesh : ITBIN-2313-0071 | Project Developer |

---

### License

This project is developed for academic purposes as part of the Agentic AI Application Development assignment.

Copyright © 2026. All rights reserved.
