# Chatbot with OpenAI API Function Calling

## Setup

```bash
git clone https://github.com/be4rr/chatbot-function-calling.git
cd chatbot-function-calling
```

Rename `.env.example` to `.env` and fill in the API key.

```bash
python -m venv venv
source venv/bin/activate
pip install langchain streamlit openai python-dotenv
streamlit run main.py
```