import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
import openai

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = api_key

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

# 체인 실행 및 오류 처리
try:
    response = chain.run({"country": "대한민국"})
    print(response)
except openai.RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
except openai.OpenAIError as e:
    print(f"An error occurred: {e}")
