# 🎙️ AI Debate Arena

An AI-powered multi-agent debate simulator built with **LangGraph** and **Groq**. Two AI agents argue opposing sides of any topic across multiple rounds, moderated and judged by dedicated AI agents — all rendered in a live typewriter-style terminal UI.

---

## 📁 Project Structure

```
debate-arena/
├── main.py           # Entry point: user input, graph invocation, terminal display
├── agents.py         # State definition, LLM setup, all agent functions
├── connections.py    # Graph nodes, edges, routing logic, compiled graph
└── prompts.py        # All prompt templates
```

---

## 🧠 How It Works

The debate runs as a **LangGraph state machine** with 4 agents:

| Agent | Role |
|---|---|
| **Moderator** | Introduces the topic, sets rules, randomly picks who argues first |
| **Pro** | Argues in favour of the topic each round |
| **Con** | Rebuts and argues against the topic each round |
| **Judge** | Evaluates the full debate and declares a winner |

### Flow

```
START → Moderator → [Pro ↔ Con] × N rounds → Judge → END
```

- The moderator randomly picks the starting side (`pro` or `con`)
- Pro and Con alternate until `max_rounds` is reached
- The judge then reviews the full debate history and picks a winner

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sripadh-Sujith/debate-arena.git
cd debate-arena
```

### 2. Install dependencies

```bash
pip install langgraph langchain-groq rich
```

### 3. Set your Groq API key

In `agents.py`, replace the `api_key` value with your own key from [console.groq.com](https://console.groq.com):

```python
llm = ChatGroq(
    model='llama-3.1-8b-instant',
    api_key='your_groq_api_key_here'
)
```

> **Tip:** Use an environment variable instead for security:
> ```python
> import os
> api_key=os.environ.get("GROQ_API_KEY")
> ```

---

## ▶️ Usage

```bash
python main.py
```

You will be prompted for:

```
Enter the topic: AI will replace software engineers
Enter maximum rounds: 3
```

Each agent's response then streams to the terminal with a typewriter effect in colour-coded panels.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `langgraph` | State machine / agent orchestration |
| `langchain-groq` | Groq LLM integration via LangChain |
| `rich` | Terminal UI (panels, live typewriter rendering) |

---

## 🗂️ Module Details

### `prompts.py`
Stores all 4 prompt templates as plain strings with `{placeholder}` variables for topic, history, and starter side.

### `agents.py`
- Defines the `State` TypedDict shared across all graph nodes
- Initialises the `ChatGroq` LLM instance
- Implements `moderator`, `pro_agent`, `con_agent`, and `judge` functions

### `connections.py`
- Defines routing functions `next_turn` and `should_continue`
- Builds and compiles the `StateGraph` with all nodes and edges

### `main.py`
- Collects user input
- Invokes the compiled graph
- Renders each message from history using the `typewriter_panel` function

---

## 🔮 Possible Improvements

- Move the API key to a `.env` file using `python-dotenv`
- Add support for saving debate transcripts to a file
- Allow the user to choose the LLM model at runtime
- Add a web UI using Flask or Streamlit
- Support more than 2 debaters

---

## 📄 License

MIT License. Free to use and modify.