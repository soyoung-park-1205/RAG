from click import prompt
from langchain.prompts import PromptTemplate


def build_context_prompt():
    return PromptTemplate.from_template(
        """
    당신은 뉴스 기사를 참고하여 사용자의 질문에 답변하는 AI입니다.

    다음은 최근의 '{keyword}' 관련 뉴스 기사 내용입니다:
    
    {context}
    
    질문: {question}

    아래 조건을 반드시 지켜서 답변해 주세요.
    
    - 답변은 반드시 위의 기사 내용 만을 활용할 것. (기사에 언급된 명사 만을 활용하여 답변)
    - "~니다."와 같은 친절한 격식체를 사용하여 한국어로 간결하게 답변할 것.
    - "내가 대답한다면, ", "이렇게 답변해보세요." 등의 표현은 절대 사용하지 말 것.
    - 기사에 없는 내용을 절대 만들어 내지 말 것.
    
    """
    )
