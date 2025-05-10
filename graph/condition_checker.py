from graph.state import MyState


def has_keyword(state: MyState):
    return state["keyword"] != ""

def is_origin(state: MyState):
    return state["origin"] == True
