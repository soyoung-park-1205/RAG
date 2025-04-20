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


def build_judge_prompt():
    return PromptTemplate.from_template(
    """
    아래는 사용자의 질문에 대한 AI의 답변입니다.
    
    질문: {question}
    답변: {answer}
    
    [참고 기사 내용 (reference)]
    {context}
    
    아래 두 항목에 대해 점수 기준을 반드시 반영하여 엄격하게 답변을 평가해 주세요:
    
    1. 질문에 적절한 내용을 포함하고 있나요? (relevance)
    점수 기준:
    - 1~3:  질문을 회피하거나, 추가 정보를 요구만 하고 답변을 하지 않 (제공할 수 없습니다, 모릅니다 등)
    - 4~6: 질문의 핵심에 대해 답변하지 못함
    - 7~8: 질문에 대해 일부 답변함
    - 9~10: 질문의 핵심 내용에 대해 명확히 답변함
    
    2. reference 내용에 기반하고 있나요? 다른 일반적 지식이 아닌 reference 내용만 참고하여 평가해 주세요. (faithfulness) 
    점수 기준:
    - 1~3: reference에 있는 주요 정보 전혀 반영 안 함
    - 4~6: 잘못된 정보, 수치를 포함함
    - 7~8: 대부분 맞지만 핵심 정보 누락
    - 9~10: reference에 있는 내용의 핵심을 포함
        
    각 항목에 대해 1~10점 사이로 평가하여 부연 설명없이 아래와 같은 JSON 포맷으로 만 정확히 리턴해 주세요:
    {{
      "relevance": 점수,
      "faithfulness": 점수
    }}
    
    """
    )