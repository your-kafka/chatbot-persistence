# LangGraph Chatbot

A lightweight conversational chatbot built with LangGraph, LangChain, Groq, and Streamlit. The project demonstrates how to create a simple stateful chat agent with in-memory conversation tracking and a browser-based UI.

## Author

- Name: Ramkrishna Rathore
- Email: luckyrathore70495@kgpian.iitkgp.ac.in

## Features

- Stateful chat flow using LangGraph
- In-memory conversation checkpointing
- Groq-powered language model responses
- Streamlit chat interface for quick local demos
- Streaming UI mode for real-time token display
- Compact responses optimized for short, crisp answers

## Tech Stack

- Python 3.12
- LangGraph
- LangChain
- Groq
- Streamlit
- Python-dotenv

## Project Structure

```text
langgraph-chatbot/
├── .env                        # Local environment variables (not committed)
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── pyproject.toml              # Python project metadata
├── requirements.txt            # Python dependencies
├── src/
│   └── langgraph_chatbot/
│       ├── __init__.py
│       ├── backend.py          # LangGraph chatbot logic
│       ├── frontend.py         # Standard Streamlit chat UI
│       └── frontend_streaming.py  # Streaming Streamlit UI
└── .venv/                      # Local virtual environment (ignored by Git)
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd langgraph-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root and add the following:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get an API key from the Groq platform and paste it into the environment file before running the app.

## Run the Application

### Standard chat UI

```bash
streamlit run src/langgraph_chatbot/frontend.py
```

### Streaming chat UI

```bash
streamlit run src/langgraph_chatbot/frontend_streaming.py
```

Then open the local Streamlit URL shown in the terminal, typically:

```text
http://localhost:8501
```

## How It Works

The backend uses a LangGraph `StateGraph` with a single node that:

- receives the latest user message,
- appends it to the message history,
- and sends the conversation context to a Groq model.

The app uses `InMemorySaver` to maintain a simple conversation checkpoint for the current thread, and the Streamlit frontends render the user/assistant messages in a chat UI.

## Example Flow

```python
response = chatbot.invoke({
    'messages': [HumanMessage(content='Hello!')]
}, config=config1)
```

This returns the model's response and stores the interaction in the in-memory graph state.

## Notes

- `frontend.py` is the standard chat application.
- `frontend_streaming.py` streams responses chunk by chunk for a more interactive user experience.
- The current project is designed for local development and demonstration purposes.

## Contact

For questions or collaboration, please contact:

- Ramkrishna Rathore
- luckyrathore70495@kgpian.iitkgp.ac.in
