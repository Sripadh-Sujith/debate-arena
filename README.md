# 🎙️ AI Debate Arena

An AI-powered multi-agent debate simulator built with **LangGraph** and **Gemma 4 via OpenRouter**. Two AI agents argue opposing sides of any topic across multiple rounds, moderated and judged by dedicated AI agents — all rendered in a live typewriter-style terminal UI.

---

## 🚀 Why AI Debate Arena?

Most AI apps give a **single answer**.

AI Debate Arena creates a **battle of ideas** using multiple AI agents so users can explore arguments, challenge assumptions, and think critically before making decisions.

Perfect for:

* Students
* Researchers
* Founders
* Writers
* Curious thinkers
* Anyone comparing viewpoints

---

## 📁 Project Structure

```bash
debate-arena/
├── main.py
├── agents.py
├── connections.py
└── prompts.py
```

---

## 🧠 How It Works

The debate runs as a **LangGraph multi-agent state machine** with 4 agents:

| Agent     | Role                                                          |
| --------- | ------------------------------------------------------------- |
| Moderator | Introduces topic, explains rules, randomly selects who starts |
| Pro       | Defends the topic                                             |
| Con       | Challenges the topic                                          |
| Judge     | Evaluates and declares a winner                               |

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/Sripadh-Sujith/debate-arena.git
cd debate-arena
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add OpenRouter API Key

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Configure Gemma 4

```python
from langchain_openrouter import ChatOpenRouter
import os

llm = ChatOpenRouter(
    model="google/gemma-4-27b-it",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 📄 License

MIT License.

---

## 🙌 Author

Built by **Sripadh Sujith**
