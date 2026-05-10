import random
from langchain_openrouter import ChatOpenRouter
from typing_extensions import TypedDict, List, Dict
from prompts import PRO_PROMPT, CON_PROMPT, MODERATOR_PROMPT, JUDGE_PROMPT
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenRouter(
    model="google/gemma-4-26b-a4b-it",
    api_key=os.getenv('API_KEY')
)

class State(TypedDict):
    topic: str | None
    turn: str | None
    history: List[Dict]
    round: int
    max_rounds: int
    winner: str | None


def moderator(state: State):
    starter = random.choice(['pro', 'con'])

    response = llm.invoke(MODERATOR_PROMPT.format(
        topic=state['topic'],
        starter=starter
    ))

    print(response.content)

    state['history'].append(
        {'role': 'moderator', 'content': response.content}
    )

    state['turn'] = starter

    return state


def pro_agent(state: State):
    response = llm.invoke(PRO_PROMPT.format(
        topic=state['topic'],
        history=state['history']
    ))

    state['history'].append(
        {'role': 'pro', 'content': response.content}
    )

    state['turn'] = 'con'
    state['round'] += 1

    return state


def con_agent(state: State):
    response = llm.invoke(CON_PROMPT.format(
        topic=state['topic'],
        history=state['history']
    ))

    state['history'].append(
        {'role': 'con', 'content': response.content}
    )

    state['turn'] = 'pro'
    state['round'] += 1

    return state


def judge(state: State):
    response = llm.invoke(JUDGE_PROMPT.format(
        topic=state["topic"],
        history=state["history"]
    ))

    state["history"].append({
        "role": "judge",
        "content": response.content
    })

    if 'pro' in response.content:
        state['winner'] = 'pro'
    else:
        state['winner'] = 'con'

    return state
