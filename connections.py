from langgraph.graph import START, StateGraph, END
from agents import State, moderator, pro_agent, con_agent, judge


def next_turn(state):
    return state["turn"]


def should_continue(state):
    if state["round"] >= state["max_rounds"]:
        return "judge"
    return "continue"


graph_builder = StateGraph(State)

graph_builder.add_node("moderator", moderator)
graph_builder.add_node("pro", pro_agent)
graph_builder.add_node("con", con_agent)
graph_builder.add_node("judge", judge)

graph_builder.add_edge(START, "moderator")
graph_builder.add_conditional_edges('moderator', next_turn,
                                    {
                                        'pro': 'pro',
                                        'con': 'con'
                                    }
                                    )

graph_builder.add_edge('pro', 'con')

graph_builder.add_conditional_edges('con', should_continue, {
    'judge': 'judge',
    'continue': 'pro'
})

graph_builder.add_edge('judge', END)

graph = graph_builder.compile()