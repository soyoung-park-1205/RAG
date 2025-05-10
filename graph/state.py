from typing_extensions import TypedDict


class MyState(TypedDict):
    question: str
    messages: list
    keyword: str
    context: str
    response: str
    thread_id: str
    model_nm: str
    origin: bool