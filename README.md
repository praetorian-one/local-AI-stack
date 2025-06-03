# 🧠 Private AI Research & Retrieval Stack

A modular, self-hosted AI stack for intelligent document retrieval, natural language processing, code generation, and live research — entirely on your own hardware.

## 🏗️ Project Overview

This stack is designed to provide an alternative to hosted AI services like ChatGPT, with full local control over your data, documents, and model choices. It supports:

- **Retrieval-Augmented Generation (RAG)**: Ask questions and get answers grounded in your private data.
- **Multi-model support**: Swap between general-purpose and code-optimized models.
- **Internet-connected agents**: Perform live lookups using APIs (weather, Wikipedia, Wayback Machine, etc.).
- **User-friendly web interface**: Built on Open WebUI with persistent chat, file uploads, and agent triggering.
- **Ingestion from common formats**: Markdown, PDFs, Apple Notes, emails, and more.
- **Agent extensibility**: Easily add new tools like Brave Search, ArchiveBox, or Filesystem Scanners.

## 🧍‍ Core Components

- [**Kotaemon**](https://github.com/kota-ai/kotaemon) — A local LLM orchestration platform, chosen for its flexibility, modularity, and ability to support multiple models and agents.

- [**Open WebUI**](https://github.com/open-webui/open-webui) — A browser-based front-end that offers a clean, extensible chat interface with integrated RAG (Retrieval-Augmented Generation) capabilities. It supports document loading, `#command` queries, and direct internet lookups.

- [**Qdrant Vector Database**](https://github.com/qdrant/qdrant) — A high-performance vector search engine chosen for its scalability, rich feature set, and ease of integration with our LLM stack. It stores document embeddings enabling fast semantic retrieval.

- [**WireGuard VPN (Optional)**](https://www.wireguard.com/) — A modern, high-performance VPN protocol. This stack supports optional outbound routing of all service traffic through a WireGuard VPN container such as [**Gluetun**](https://github.com/qdm12/gluetun). Disabled by default. Useful for privacy, location shifting, or routing outbound agent requests through a VPN.

## 🧠 Supported Models

Pre-downloaded models are mounted into the stack. You may switch them by editing a single variable or dropdown in Open WebUI:

### 🔮 General-Purpose Chat
- [`llama-3-8b-lexi-uncensored.Q4_K_M.gguf`](https://huggingface.co/TheBloke/llama-3-8B-Lexi-Uncensored-GGUF)
- [`llama-3-8b-lexi-uncensored.Q2_K.gguf`](https://huggingface.co/TheBloke/llama-3-8B-Lexi-Uncensored-GGUF)

### 💻 Code Generation
- [`deepseek-coder-1.3b-instruct.Q4_K_M.gguf`](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct)
- [`deepseek-coder-6.7b-instruct.Q4_K_M.gguf`](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)

All models are served using [llama.cpp](https://github.com/ggerganov/llama.cpp) with GGUF quantization for efficient CPU/GPU inference.

## 🔎 Embedding Backend

- [**nomic-embed-text-v1.5**](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) — Fast, high-accuracy sentence embeddings used to index and semantically search all private documents. Backed by the Nomic team (creators of GPT4All embeddings).

## 📆 Ingestion Pipelines

These components populate the Qdrant vector DB and can be queried by the assistant:

- ✅ **Filesystem Scanner Agent** — Crawls user-defined directories for `.pdf`, `.txt`, `.md`, `.docx`, and others.
- ✅ **Apple Notes Ingestor** — Converts exported `.txt` or `.html` Apple Notes into searchable content.
- ✅ **Obsidian Vault Support** — Direct `.md` file parsing for knowledge bases and Zettelkasten setups.
- ✅ **Email Export Agent** — Ingests `.eml`, `.mbox`, or `.txt`-formatted email exports.
- ✅ **Calendar Agent** — Parses `.ics` and `.csv` calendar exports to contextualize queries.
- ✅ **Financial Data Agent** — Upload `.csv` or `.pdf` bank statements for local analysis.
- ✅ **Apple Notes Ingestion** — Ingests exported Apple Notes in `.txt` or `.html` format for semantic retrieval.
- ✅ **Obsidian Vaults** — Parses `.md` files in structured vaults for rich semantic queries.

## 🌐 Internet-Connected Agents

These optional tools allow your AI to access the internet live:

| Agent | Description | Use Cases |
|-------|-------------|-----------|
| 🛍️ **Brave Search Agent** | Uses [Brave Search API](https://api.search.brave.com/) for privacy-first web results. | Research topics, recent events. |
| 🌐 **Wikipedia Agent** | Queries Wikipedia API for general knowledge. | Definitions, timelines, bios. |
| ⌛ **Wayback Machine Agent** | Retrieves historical snapshots via [archive.org](https://archive.org). | View deleted pages, historical prices. |
| 📚 **ArchiveBox Agent** | Searches your own local [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) snapshot repo. | Internal link search and backup access. |
| 📅 **Calendar Agent** | Checks availability and schedules. | “What’s on my calendar Friday?” |
| 💸 **Finance Agent** | Summarizes local CSVs or PDF statements. | “How much did I spend on food in April?” |
| 📨 **Email Agent** | Searches email bodies and attachments. | “Find the invoice from Comcast.” |
| ⛅ **Weather Agent** | Fetches current and forecast data via OpenWeather API. | “Is it raining in Seattle right now?” |
| 📊 **Stock Market Agent** | Pulls real-time and historical data via [Yahoo Finance API](https://www.yahoofinanceapi.com/) or [Alpha Vantage](https://www.alphavantage.co/). | “What was TSLA's closing price last Friday?”, “Compare AAPL and MSFT year-to-date.” |

## 🛠️ Hardware Requirements

Minimum for smooth operation:
- **CPU**: Quad-core (AVX2 or AVX512 strongly recommended)
- **RAM**: 8 GB (16+ GB recommended for multiple models or larger context windows)
- **Disk**: 100+ GB SSD (fast access for models and vector DB)
- **GPU (optional)**: CUDA or Metal support for GPU acceleration in `llama.cpp`

> ✅ NAS-backed storage (NFS or SMB) is supported for `models/` and `qdrant/` storage. Mount these via the host OS before launching Docker.

## 💪 Deployment Strategy

The full stack is containerized using Docker Compose. It includes:

- Open WebUI front-end
- Kotaemon agent runtime
- Qdrant vector DB
- Optional VPN via WireGuard container
- Optional document sync via Syncthing
- Ingestion pipelines and config files

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

## 🥐 Setup Instructions

Will be added after all files are finalized, including:

- System prerequisites
- Mounting network shares (if used)
- Model download script
- `.env` and `settings.yaml` customization
- VPN setup (optional)
- Launching the stack
