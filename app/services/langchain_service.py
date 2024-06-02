from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
import openai
from app.core.config import settings

# OpenAI Chat 모델 설정
llm = ChatOpenAI(
    temperature=0,  # 창의성 0으로 설정
    model_name='gpt-3.5-turbo',  # 모델명
)

# 프롬프트 템플릿 생성
prompt = PromptTemplate(
    input_variables=["country"],
    template="{country}의 수도는 어디야?",
)

# LLM 체인 생성
chain = LLMChain(llm=llm, prompt=prompt)

def get_capital(country: str) -> str:
    try:
        response = chain.run({"country": country})
        return response
    except openai.RateLimitError as e:
        return f"Rate limit exceeded: {e}"
    except openai.OpenAIError as e:
        return f"An error occurred: {e}"
