# AI Research Agent

A smart chatbot that helps you explore the world of **AI**, **Machine Learning**, and **cutting-edge research** using real-time tools like **arXiv**, **Wikipedia**, and the **Web** — all packed into a simple Streamlit app.

---

## What is This?

This project is an AI-powered research assistant built using:

- **LangGraph** to manage the chatbot flow
- **Groq’s Qwen 32B LLM** to understand and answer your questions
- **Tools** like:
  - `arXiv` for research papers
  - `Wikipedia` for summarized info
  - `Tavily` for real-time web search
- **Streamlit** for the user interface

You ask a question — it finds the answer from real sources!

---

## ⚙️ How to Set It Up

### 1. Clone this Project

```bash
git clone https://github.com/your-username/ai-research-agent.git
cd ai-research-agent
````

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the Needed Libraries

```bash
pip install -r requirements.txt
```

### 4. Set Your API Keys

Make a `.env` file and add your keys like this:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the App

```bash
streamlit run app.py
```

Then go to the link it shows (usually [http://localhost:8501](http://localhost:8501)) to use the chatbot!

---

## 💬 How to Use

Just type your research question into the input box.
Example:

```
What’s the latest research on AI agents?
```

The chatbot will search academic papers, Wikipedia, and the web, then give you a helpful answer.

---

## What’s Inside

* **Streamlit**: Simple web app interface
* **LangGraph**: Controls how the chatbot thinks
* **LangChain**: Tool and LLM integration
* **Groq LLM**: Fast and smart AI model
* **Tools**:

  * Arxiv
  * Wikipedia
  * Tavily Search

---

## Features

* Answers your questions using real sources
* Combines multiple tools with a large AI model
* Easy to use with a clean web UI
* Open-source and easy to customize

---

## 🙌 Want to Help?

Feel free to fork this repo, improve the chatbot, or add new tools.
PRs are welcome!

---


## 📚 Credits

Thanks to:

* [LangChain](https://github.com/langchain-ai/langchain)
* [LangGraph](https://github.com/langchain-ai/langgraph)
* [Groq](https://groq.com/)
* [Tavily](https://www.tavily.com/)
* [arXiv](https://arxiv.org/)
* [Wikipedia](https://www.wikipedia.org/)

