PRO_PROMPT = """
You are arguing FOR: {topic}

Debate so far:
{history}

Give a strong argument. Avoid repetition.
"""

CON_PROMPT = """
You are arguing AGAINST: {topic}

Debate so far:
{history}

Rebut previous argument and add counterpoints.
"""

MODERATOR_PROMPT = """
Introduce the debate topic: {topic}
Set rules briefly and announce who starts: {starter}
"""

JUDGE_PROMPT = """
Debate Topic: {topic}

Full Debate:
{history}

Decide winner (pro or con) and explain why and do not mention the loser in the response.
"""