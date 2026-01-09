# Digital You

This repository serves as the foundation for building a personalized **Digital Twin** using **Large Language Models (LLMs)**.

The goal of this project is to ingest professional artifacts—such as resumes, LinkedIn profiles, and portfolios—and expose them through a conversational AI interface that accurately represents an individual’s professional persona.

## Technical Setup

### 1. Clone the repository and navigate to project root.

### 2. Environment Synchronization (Requires `uv`)

Ensure `uv` is installed, then run:

```bash
uv sync
```

### 3. Credential Management

Create a `.env` file in the project root directory to securely store your credentials:

```env
OPENAI_API_KEY=your_production_key_here
```

> ⚠️ Never commit your `.env` file to version control.

### 4. Data Ingestion

Populate the `/data` directory with your professional documents.

**Supported file formats:**

- `.txt`
- `.md`
- `.pdf`

These files will be read, parsed, and combined to construct the AI’s contextual knowledge base.

## Implementation Tasks

### 1. Client Initialization

- Establish a secure connection to the OpenAI API.

### 2. Data Pipeline

- Implement a robust file ingestion system.

### 3. Persona Grounding

- Engineer a system prompt using ingested professional data.

### 4. Inference Execution

- Connect to the OpenAI Chat Completions endpoint.

### 5. Deployment

- Initialize and deploy the Gradio UI.

## Running the Application

```bash
uv run app.py
```

This launches the Gradio interface locally.
