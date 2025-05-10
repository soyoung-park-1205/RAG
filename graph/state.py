from typing import Annotated

from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class MyState(TypedDict):
    question: str
    messages: Annotated[list, add_messages]
    keyword: str
    context: str
    response: str
    thread_id: str
    model_nm: str
    origin: bool