
# AI-Powered Website Generator

An AI-powered web application that generates complete, responsive websites from natural-language prompts.  
Users describe their requirements (e.g., *“Create a portfolio website for a photographer”*), and the system automatically generates a functional website with layout, styling, and content, which can be previewed and downloaded instantly.

---

## 🚀 Features

- **Natural Language Input**
  - Users provide website requirements using plain English.

- **AI-Powered Website Generation**
  - Uses an open-source Large Language Model (LLaMA 2) to generate complete HTML websites.

- **Live Preview**
  - Generated websites are rendered instantly in the browser using an iframe.

- **Export Functionality**
  - Users can download the generated website as an HTML file.

- **Robust Output Handling**
  - Server-side sanitization ensures clean HTML output with no model explanations or invalid assets.
  - Automatic replacement of broken image sources with online placeholders.

- **Responsive Design**
  - Generated websites are mobile-friendly and use modern CSS techniques.

---

## 🏗️ System Architecture

---

## 🧰 Tech Stack

### Frontend
- HTML
- CSS
- Vanilla JavaScript
- iframe for live preview

### Backend
- Python
- FastAPI
- Uvicorn

### AI / ML
- **LLaMA 2 (Open-Source LLM)**
- Ollama (local model runtime)

---

## 🤖 Why LLaMA 2 + Ollama?

- Completely **free and open-source**
- No API quotas or billing requirements
- Runs locally for full control and privacy
- Suitable for internship-level and academic projects
- Demonstrates practical GenAI engineering decisions

---

## ⚙️ How It Works

1. User enters a website requirement in the frontend UI.
2. Frontend sends a POST request to the FastAPI backend.
3. Backend constructs a structured prompt and sends it to the LLaMA 2 model via Ollama.
4. The model generates a complete HTML website.
5. Backend sanitizes the output to:
   - Remove explanations (LLM leakage)
   - Ensure valid HTML
   - Fix broken image URLs using online placeholders
6. Clean HTML is returned to the frontend.
7. Website is rendered live in an iframe and can be downloaded.

---

## ▶️ How to Run Locally (Full AI Mode)

### Prerequisites
- Python 3.10+
- Ollama installed
- LLaMA 2 model pulled via Ollama

### 1. Install Ollama and Pull Model
```bash
ollama pull llama2
