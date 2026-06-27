# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

This project implements an AI-powered customer support automation system for **ABC Technologies**, a SaaS company that provides cloud-based business management software.

The system automates customer support by identifying customer intent, routing queries to the appropriate department, retrieving relevant information from company documents using Retrieval-Augmented Generation (RAG), maintaining conversation history using SQLite memory, handling human approval for high-risk requests, and generating professional responses through a supervisor agent.

The project is built using **LangGraph**, **LangChain**, **Groq LLM**, **ChromaDB**, and **SQLite**.

---

# Features

* Intent Classification
* Department-wise Agent Routing
* Sales Support Agent
* Technical Support Agent
* Billing Support Agent
* Account Support Agent
* Retrieval-Augmented Generation (RAG)
* Chroma Vector Database
* SQLite Conversation Memory
* Human-in-the-Loop Approval
* Supervisor Agent
* Professional Customer Response Generation

---

# Technologies Used

* Python 3.12
* LangGraph
* LangChain
* LangChain Groq
* ChromaDB
* HuggingFace Embeddings
* SQLite
* PyPDF
* SQLAlchemy
* Python Dotenv

---

# Project Structure

```
CustomerSupportAI/
│
├── agents/
│   ├── classifier.py
│   ├── sales_agent.py
│   ├── technical_agent.py
│   ├── billing_agent.py
│   ├── account_agent.py
│   ├── supervisor.py
│   └── human_approval.py
│
├── documents/
│   ├── company_policy.pdf
│   ├── pricing_guide.pdf
│   ├── technical_manual.pdf
│   └── faq.pdf
│
├── memory/
│   ├── database.py
│   ├── memory.py
│   └── memory_node.py
│
├── rag/
│   ├── loader.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── rag.py
│
├── app.py
├── graph.py
├── router.py
├── state.py
├── init_db.py
├── memory.db
├── requirements.txt
├── README.md
└── .env
```

---

# Workflow

```
Customer Query
        │
        ▼
Intent Classification
        │
        ▼
Department Routing
        │
 ┌──────┼──────────────┐
 │      │      │       │
 ▼      ▼      ▼       ▼
Sales Technical Billing Account
 │      │      │       │
 └──────┼──────┼───────┘
        ▼
Human Approval (if required)
        │
        ▼
Supervisor Agent
        │
        ▼
SQLite Memory
        │
        ▼
Final Customer Response
```

---

# Knowledge Base Documents

The RAG pipeline retrieves information from the following documents:

* Company Policy
* Pricing Guide
* Technical Manual
* FAQ Document

---

# Human-in-the-Loop Requests

The following requests require manual approval before responding:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

# Memory

Conversation history is stored using SQLite.

Example:

Customer:

```
My name is David.
```

Customer:

```
I have a billing issue.
```

Customer:

```
What was my previous support issue?
```

Response:

```
Your previous support issue was:
I have a billing issue.
```

---

# Setup Instructions

## 1. Clone the repository

```
git clone <repository-url>
cd CustomerSupportAI
```

---

## 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 3. Configure environment variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 4. Initialize SQLite database

```
python init_db.py
```

---

## 5. Run the application

```
python app.py
```

---

# Sample Queries

### Sales

```
What are the pricing plans available for your software?
```

---

### Account

```
I forgot my account password.
```

---

### Technical Support

```
My application crashes whenever I upload a file.
```

---

### Billing

```
I need a refund for my annual subscription.
```

---

### Memory

```
What was my previous support issue?
```

---

