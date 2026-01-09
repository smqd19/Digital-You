import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment-specific configurations
load_dotenv()

# --- TODO 1: Service Initialization ---
# Initialize the OpenAI client using your API credentials.
# Ensure you handle the case where the API key might be missing.
client = None

def ingest_professional_data():
    """
    TODO 2: Multi-Source Data Ingestion
    Implement logic to scan the /data directory for relevant files (e.g., .txt, .md, or .pdf).
    
    For PDF parsing, you may need to add 'pypdf' to your pyproject.toml and sync. (uv add pypdf)
    """
    context = ""
    # Placeholder: Implement your custom ingestion logic here.
    return "Expert Full Stack Developer with 2+ years of experience."

def digital_twin_orchestrator(message, history):
    """
    Handles the orchestration between user input and LLM inference.
    """
    
    # Retrieve injected context
    context = ingest_professional_data()

    # --- TODO 3: Prompt Engineering ---
    # Define the system persona. Use the 'context' variable to ground the AI's knowledge in your professional history.
    system_instructions = f"Act as a professional digital twin. Context: {context}"

    # --- TODO 4: Inference Call ---
    # Implement the Chat Completions API call. 
    # Consider experimenting with temperature and model (e.g., 'gpt-4o-mini').
    
    # --- ENHANCEMENT SUGGESTION: Conversation Memory ---
    # Currently, this function is stateless. To make it remember previous 
    # exchanges, you must iterate through the 'history' list and append 
    # those messages to your 'messages' array before the final user message.
    
    # Simulated response - Replace with actual API call logic
    return "Logic not yet implemented. Please complete TODO 4."

# --- TODO 5: Interface Provisioning ---
# Expose the orchestrator via Gradio's ChatInterface.
app = gr.ChatInterface(
    fn=digital_twin_orchestrator,
    type="messages", # Modern Gradio message format
)

# --- ENHANCEMENT SUGGESTION: UI/UX Customization ---
# You can enhance the professional look of your application by adding:
# 1. A custom 'title' and 'description' to gr.ChatInterface.
# 2. 'examples' to guide the user on what to ask your digital twin.
# 3. Custom CSS or a specific 'theme' (e.g., gr.themes.Soft()).

if __name__ == "__main__":
    app.launch()