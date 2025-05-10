from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate


def get_response_format():
    response_schemas = [
        ResponseSchema(name="answer", description="질문에 대한 답변"),
    ]

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    return output_parser.get_format_instructions()

def get_search_check_format():
    response_schemas = [
        ResponseSchema(name="fit_condition", description="조건 만족"),
    ]

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

    return output_parser.get_format_instructions()


def build_context_prompt():
    return PromptTemplate.from_template(
        """
    이전 대화 내용:
    {messages}
    
    당신은 뉴스 기사를 참고하여 사용자의 질문에 답변하는 AI입니다.

    다음은 최근의 '{keyword}' 관련 뉴스 기사 내용입니다:

    {context}

    질문: {question}

    아래 조건을 반드시 지켜서 답변해 주세요. 필요한 경우 이전 대화 내용을 참고하세요.

    - 답변은 반드시 위의 기사 내용 만을 활용할 것. (기사에 언급된 명사 만을 활용하여 답변)
    - "~니다."와 같은 친절한 격식체를 사용하여 한국어로 간결하게 답변할 것.
    - "내가 대답한다면, ", "이렇게 답변해보세요." 등의 표현은 절대 사용하지 말 것.
    - 기사에 없는 내용을 절대 만들어 내지 말 것.
    
    {format_instructions}
    """,
        partial_variables =  {"format_instructions": get_response_format()}
    )


def build_question_prompt():
    return PromptTemplate.from_template(
        """
    이전 대화 내용:
    {messages}
    질문: {question}
    
    당신은 챗봇 AI입니다. 아래 질문에 대해 답변해주세요. 이전 대화 내용은 질문과 관련이 있는 경우에만 활용해주세요.
    
    아래 조건을 반드시 지켜서 답변해 주세요.
    
    - "~니다."와 같은 친절한 격식체를 사용하여 한국어로 간결하게 답변할 것.
    - "내가 대답한다면, ", "이렇게 답변해보세요.", "기사 내용에 따르면" 등과 같은 표현은 절대 사용하지 말 것.

    {format_instructions}
    """,
        partial_variables = {"format_instructions": get_response_format()}
    )


def build_search_decision_prompt():
    return PromptTemplate.from_template(
        """

    최신성 체크 혹은 추가 검색이 필요한 질문은 1, 그렇지 않은 단순 대화 패턴일 경우 0을 리턴해주세요.
    
    [최신성 체크가 필요한 질문 예시]
    1. 현재 미국 대통령은 누구야?
    2. 오늘 날씨 알려줘.
    3. 2025년 5월 미국 달러 환율 알려줘.
    
    [단순 대화 패턴 예시]
    1. 안녕하세요
    2. 나는 소영이야
    3. 내 문서 요약해줘
    
    질문: {question}

    {format_instructions}
    """,
        partial_variables = {"format_instructions": get_search_check_format()}
    )