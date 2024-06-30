from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
import openai
from chat.config import opeai_env

# OpenAI API 키 설정
openai.api_key = opeai_env["OPENAI_API_KEY"]

# # LLM 및 프롬프트 템플릿 설정
llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-3.5-turbo',
    openai_api_key=opeai_env["OPENAI_API_KEY"]
)

prompt = PromptTemplate(
    input_variables=["query"],
    template="{query}",
)

# # LLM 체인 생성
chain = LLMChain(llm=llm, prompt=prompt)

def get_query(query: str) -> str:
    try:
        response = chain.run({"query": query})
        return response
    except openai.error.RateLimitError as e:
        return f"Rate limit exceeded: {e}"
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
