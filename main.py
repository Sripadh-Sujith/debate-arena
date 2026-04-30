from connections import graph
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from time import sleep

usr = input('Enter the topic:')
maxround = int(input('Enter maximum rounds:'))

result = graph.invoke({
    "topic": usr,
    "history": [],
    "round": 1,
    "max_rounds": maxround,
    "turn": "",
    "winner": ""
})

console = Console()


def typewriter_panel(role, content):
    colors = {
        "moderator": "cyan",
        "pro": "green",
        "con": "red",
        "judge": "magenta"
    }
    text = Text()
    with Live(Panel(text, title=role.upper(), border_style=colors.get(role, "white")), refresh_per_second=30) as live:
        for char in content:
            text.append(char)
            sleep(0.005)
            live.update(Panel(text, title=role.upper(), border_style=colors.get(role, "white")))


for msg in result["history"]:
    typewriter_panel(msg["role"], msg["content"])
    sleep(0.5)

console.print(Panel(f"Winner: {result['winner']}", style="bold yellow"))