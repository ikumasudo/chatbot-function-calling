# Chatbot with OpenAI API Function Calling

## Setup

```bash
git clone https://github.com/be4rr/chatbot-function-calling.git
cd chatbot-function-calling
```

```bash
echo 'OPENAI_API_KEY=<API KEY>' > .env
```

```bash
python -m venv venv
source venv/bin/activate
pip install langchain streamlit openai python-dotenv
streamlit run main.py
```
