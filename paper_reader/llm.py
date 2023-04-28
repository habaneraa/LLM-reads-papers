"""init LangChain chat model"""
from langchain.chat_models import ChatOpenAI

chatgpt = ChatOpenAI(
    # openai_api_key='fake',
    model_name='gpt-3.5-turbo',
    temperature=0.0,
)
