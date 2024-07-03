import json
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
import openai
from chat.config import opeai_env

# OpenAI API 키 설정
openai.api_key = opeai_env["OPENAI_API_KEY"]

# ChatOpenAI 설정
llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-4o',
    openai_api_key=opeai_env["OPENAI_API_KEY"]
)

# 이전 대화 데이터를 템플릿에 맞춰 변환하는 함수
def format_messages(messages):
    formatted_messages = []
    for msg in messages:
        if msg.role == 'user':
            formatted_messages.append(f"User: {msg.content}")
        elif msg.role == 'assistant':
            formatted_messages.append(f"Assistant: {msg.content}")
        elif msg.role == 'system':
            formatted_messages.append(f"System: {msg.content}")
    return "\n".join(formatted_messages)

# PromptTemplate 설정
prompt = PromptTemplate(
    input_variables=["messages"],
    template="{messages}\nUser:"
)

# LLMChain 생성
chain = LLMChain(llm=llm, prompt=prompt)

# 사용자 질문 처리 함수
def get_query(messages: list) -> str:
    try:
        formatted_messages = format_messages(messages)
        response = chain.run({"messages": formatted_messages})
        return response
    except openai.error.RateLimitError as e:
        return f"Rate limit exceeded: {e}"
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
