# 🧠 Private AI Research & Retrieval Stack

A modular, self-hosted AI stack for intelligent document retrieval, natural language processing, code generation, and live research — entirely on your own hardware.

---

## 🏗️ Project Overview

This stack is designed to provide an alternative to hosted AI services like ChatGPT, with full local control over your data, documents, and model choices. It supports:

- **Retrieval-Augmented Generation (RAG)**: Ask questions and get answers grounded in your private data.
- **Multi-model support**: Swap between general-purpose and code-optimized models.
- **Internet-connected agents**: Perform live lookups using APIs (weather, Wikipedia, Wayback Machine, etc.).
- **User-friendly web interface**: Built on Open WebUI with persistent chat, file uploads, and agent triggering.
- **Ingestion from common formats**: Markdown, PDFs, Apple Notes, emails, and more.
- **Agent extensibility**: Easily add new tools like Brave Search, ArchiveBox, or Filesystem Scanners.

---

## 🧝‍ Core Components

- [**Kotaemon**](https://github.com/kota-ai/kotaemon) — Local LLM orchestration platform.
- [**Open WebUI**](https://github.com/open-webui/open-webui) — Friendly front-end interface.
- [**Qdrant Vector Database**](https://github.com/qdrant/qdrant) — Fast semantic search backend.
- [**WireGuard VPN (Optional)**](https://www.wireguard.com/) — For outbound agent privacy.

---

## 🧠 Supported Models

### 🔮 General-Purpose Chat
- `llama-3-8b-lexi-uncensored.Q4_K_M.gguf`
- `llama-3-8b-lexi-uncensored.Q2_K.gguf`

### 💻 Code Generation
- `deepseek-coder-1.3b-instruct.Q4_K_M.gguf`
- `deepseek-coder-6.7b-instruct.Q4_K_M.gguf`

All models are run with `llama.cpp` (GGUF format) and swappable in the UI.

---

## 🔎 Embedding Backend

- `nomic-embed-text-v1.5` — Fast, high-quality local embedding model from Nomic AI.

---

## 📆 Ingestion Pipelines (Local Data)

| Type | Description |
|------|-------------|
| 📂 Filesystem Scanner | Crawl specified directories for `.pdf`, `.txt`, `.md`, `.docx`, etc. |
| 📝 Apple Notes | Ingest `.txt` or `.html` exports from Apple Notes |
| 📓 Obsidian Vault | Use `.md` files from your knowledge base |
| 📧 Email Agent | Parse `.eml`, `.mbox`, or `.txt` email exports |
| 📅 Calendar Agent | Ingest `.ics` or `.csv` calendar data |
| 💳 Financial Data | Load `.csv` or `.pdf` statements for spending analysis |
| 🗃️ ArchiveBox | Search your self-hosted web archive (HTML, PDFs, screenshots, full-text) |

---

## 🌐 Internet-Connected Agents

| Agent | Purpose |
|-------|---------|
| 🛙 Brave Search | Privacy-respecting search API |
| 🌐 Wikipedia | Fetch structured Wikipedia content |
| ⌛ Wayback Machine | Look up old/deleted URLs |
| 🗓️ Calendar | Query local calendar data |
| 💸 Finance | Parse and analyze spending data |
| 📨 Email | Search messages, invoices, etc. |
| ⛅ Weather | Live weather via OpenWeather API |
| 📊 Stock Market | Market data from Yahoo or Alpha Vantage |
| 📐 Google Search | Fallback to general search |
| 🛍️ Google Maps | Places, directions, business info |
| 🌍 OpenStreetMap | Open geographic data |

---

## 🔒 Privacy & Networking

- All model inference and embedding occurs **100% locally**.
- All document indexing is done on your machine or LAN.
- Internet access is **only used by agents**, and can be disabled.
- Optional VPN routing supported via **WireGuard** using **Gluetun** container.

You can enable container-level VPN by uncommenting the `gluetun` section in `docker-compose.yml`.

---

## 📌 Use Case Examples

| Prompt | Example Agents Triggered |
|--------|---------------------------|
| “Search for news on AI regulation in the EU.” | Brave Search, Google Search |
| “What’s the forecast for Seattle this weekend?” | Weather Agent |
| “What’s on my calendar for Tuesday?” | Calendar Agent |
| “Summarize my Obsidian vault on stoicism.” | Obsidian Ingestor + RAG |
| “Find emails from Comcast with attachments.” | Email Agent |
| “What was AAPL’s stock price last month?” | Stock Market Agent |
| “Find archived version of this broken link.” | Wayback Machine |
| “Give me restaurants near my hotel in Paris.” | Google Maps, OpenStreetMap |
| “Tell me what I spent on subscriptions last quarter.” | Finance Agent |
| “Search my ArchiveBox for past research on AI ethics.” | ArchiveBox Ingestor + RAG |

---

## 🛠️ Hardware Requirements

| Resource | Minimum |
|----------|---------|
| CPU | Quad-core with AVX2 (or better) |
| RAM | 8 GB (16 GB+ recommended) |
| Storage | 100 GB SSD minimum |
| GPU | Optional (Metal/CUDA for faster inference) |

> ✅ Model and vector DB directories can be mounted over NFS or SMB if preferred.

---

## 📁 Project Structure





```
repo-root/
│
├── docker-compose.yml
├── .env
├── settings.yaml
│
├── models/               # Pre-downloaded GGUF models
├── qdrant_data/          # Persistent vector DB storage
├── archivebox_data/
├── email_exports/
├── obsidian/
├── notes_ingest/
├── financial_data/
├── calendar/
│
└── syncthing_data/       # Optional file sync
```


---

## 🥐 Setup Instructions

Coming soon...

Includes:

- Mount instructions (for NAS-backed folders)
- `.env` config walkthrough
- VPN toggle instructions
- How to run and update containers
