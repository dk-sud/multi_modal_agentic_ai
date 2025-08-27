# 🧠 Multimodal Agent Systems (Agno AI Teams)

This README covers two advanced agent-based projects using the `agno` library — demonstrating **team coordination**, **agent routing**, and **tool-enhanced reasoning** in real-world e-commerce and customer support use cases.

---

## 📁 Projects Overview

### 1. 🤖 Coordinated E-Commerce Support Team
**File:** `multi_agent_agno.py`

- Composed of two specialized agents:
  - `faq_agent`: Handles web-based questions using Google Search
  - `inventory_agent`: Responds with stock availability via a custom inventory tool
- Uses `Team(mode="coordinate")` to create a collaborative assistant
- Supports multi-question prompts like:
  > *"Is iPhone 15 in stock?"* and *"Which is better for cybersecurity — ThinkPad or MacBook Pro M4?"*

---

### 2. ☎️ Multi-Agent Routing Call Center
**File:** `multi_routeing_agent.py`

- Implements a simulated call center with three agents:
  - `customer_support`: Handles tech issues (crashes, logins, freezing)
  - `sales_support`: Handles pricing, plans, and discounts
  - `faq_agent`: General business information (hours, location, contact)
- Uses `Team(mode="route")` to **intelligently route** user queries to the correct agent.
- Supports user input like:
  > *"I am unable to login"* → Routed to tech support agent.

---

## 🧠 Tech Stack

| Component        | Technology                      |
|------------------|----------------------------------|
| Agent Framework  | [`agno`](https://pypi.org/project/agno/) |
| LLM Models       | OpenAI GPT (via `OpenAIChat`)    |
| Team Modes       | `coordinate`, `route`            |
| Tooling          | GoogleSearch, Custom Python classes |
| Env Management   | `python-dotenv`                  |

---

## ⚙️ Setup Instructions

1. **Install requirements**

```bash
pip install agno python-dotenv
```

2. **Set API Key in `.env`**

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your-openai-api-key
OPEN_API_KEY=your-openai-api-key
```

> ⚠️ Both variables may be required due to naming differences across files.

---

## ▶️ Run the Projects

### For Coordinated Agents:

```bash
python multi_agent_agno.py
```

### For Routed Agents:

```bash
python multi_routeing_agent.py
```

---

## 💡 Use Cases

- AI-powered **customer support system** simulation
- Prototype for **multi-skill LLM assistants**
- Extension point for full **AI contact center** or **eCommerce copilot**

---

## 🧪 Example Questions

- *"Is the AirPods Pro in stock?"*
- *"What discounts are available this week?"*
- *"The app is crashing on launch."*

These will be answered by appropriate agents in real time.

---

## 📝 Future Enhancements

- Stream outputs into chat interfaces (Streamlit, React, etc.)
- Plug into real eCommerce APIs
- Add memory/history per user session
- Track tool usage metrics for agents

---

## 📜 License

MIT License

---

## 🙋‍♂️ Contributing

Feel free to fork and enhance agent logic, routing, or integration patterns. Contributions welcome!
