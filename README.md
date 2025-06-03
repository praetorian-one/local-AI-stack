# Self-Hosted AI Assistant Stack

## Overview

This project provides a **self-hosted AI assistant** designed to deliver rich, multi-source knowledge and live internet connectivity comparable to commercial hosted AI services — but fully under your control.  
It enables semantic search across your personal notes and documents, augmented by live, up-to-date information from web search, maps, social media, academic databases, weather, and more.

The core idea is to blend **local document ingestion** and **live web agents** into a unified conversational AI, running entirely on your own hardware or private cloud.

---

## Purpose

- Empower users to leverage their personal data alongside live internet sources without privacy or vendor lock-in concerns.  
- Provide a flexible, extensible platform capable of ingesting various local data formats and integrating multiple internet APIs seamlessly.  
- Offer control over AI models, storage location, and processing environment.  
- Serve as a foundation for advanced AI assistants tailored to specific needs, industries, or workflows.

---

## Design Considerations & Architecture

### Core Components

- [**Kotaemon**](https://github.com/kota-ai/kotaemon) — A local LLM orchestration platform, chosen for its flexibility, modularity, and ability to support multiple models and agents.  
- [**Open WebUI**](https://github.com/open-webui/open-webui) — A browser-based front-end that offers a clean, extensible chat interface with integrated RAG (Retrieval-Augmented Generation) capabilities. It supports document loading, #command queries, and direct internet lookups.  
- [**Qdrant Vector Database**](https://github.com/qdrant/qdrant) — A high-performance vector search engine chosen for its scalability, rich feature set, and ease of integration with our LLM stack. It stores document embeddings enabling fast semantic retrieval.

---

### Model Handling & Selection

Models are **stored locally** or on **network shares** mounted into the container environment, allowing flexible storage solutions like NAS or external drives. This avoids redundant downloads and eases management of large model files.

Currently supported models include:

- **General Purpose:**  
  - [`llama-3-8b-lexi-uncensored.Q4_K_M.gguf`](https://huggingface.co/TheBloke/Llama-3-8B-Lexi-Uncensored-GGUF) (full precision)  
  - [`llama-3-8b-lexi-uncensored.Q2_K.gguf`](https://huggingface.co/TheBloke/Llama-3-8B-Lexi-Uncensored-GGUF) (quantized smaller size)

- **Coding Models:**  
  - [`Deepseek-Coder 1.3B GGUF`](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base) (lightweight)  
  - [`Deepseek-Coder 6.7B GGUF`](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base) (full featured)

- **Embedding Model:**  
  - [`nomic-embed-text-v1.5`](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) — fast and accurate embedding backend compatible with Qdrant.

You can **switch between models at runtime** via the Open WebUI interface, enabling experimentation and workload-specific tuning without restarting containers.

---

## Minimum Hardware Requirements

| Component          | Recommended Minimum          | Notes                                      |
|--------------------|-----------------------------|--------------------------------------------|
| CPU                | 4 cores (x86_64 or ARM64)   | LLM inference benefits from multiple cores |
| RAM                | 12 GB                       | Larger models and multiple agents require more RAM |
| Disk               | 100+ GB SSD or NAS mounted  | Models and DB storage can be large          |
| Network            | Reliable internet connection| Required for live agents querying APIs     |
| GPU (Optional)     | CUDA-enabled NVIDIA GPU      | For accelerated model inference if supported |

This stack can run on modest hardware but scales gracefully with better resources.

---

## Agent & Ingestion Summary

### Local Ingestions

- **Apple Notes**: Ingest exported Apple Notes (.txt, .html) for semantic retrieval.  
- **Obsidian Vaults**: Parses Markdown vaults for structured document queries.  
- **Filesystem Scanner**: Auto-scans drives/folders for new documents (.pdf, .txt, .docx, .md).  
- **ArchiveBox Agent**: Searches local ArchiveBox web archive (agent-based, no ingestion).  

### Internet Agents

- **Brave Search**: Privacy-focused web search.  
- **Wikipedia**: Encyclopedic knowledge retrieval.  
- **Wayback Machine**: Archived web snapshots.  
- **OpenStreetMap**: Open-source geolocation and routing.  
- **Google Maps API** (billed): Full maps, places, routing, traffic data.  
- **Google Search (SerpAPI)**: Live Google searches with summarized results.  
- **YouTube Search & Transcript**: Video search, transcript retrieval, summarization.  
- **Twitter API v2**: Live tweets, trending topics, user feeds.  
- **News API**: Aggregated news headlines and articles.  
- **Semantic Scholar**: Academic paper metadata and abstracts.  
- **Financial Market Data**: Real-time stock and index data.  
- **Weather API**  
  ✅ Capabilities:
  - Current weather  
  - 3–7 day forecasts  
  - Weather-based planning suggestions  

  🧠 Use Case Examples:  
  - “What’s the forecast for Seattle this weekend?”  
  - “Is it raining right now in Kyoto?”  
  - “What’s the UV index at my location?”

Each agent is integrated for **real-time data augmentation** of the conversational experience, enriching answers beyond local knowledge.

---

## Storage & Mounts

Models and vector database data can be stored on local drives or mounted network shares (e.g., NFS or SMB on NAS):

| Path                  | Description                    | Notes                         |
|-----------------------|--------------------------------|-------------------------------|
| `/app/models`         | LLM model files                | Mount your model files here   |
| `/qdrant/storage`     | Qdrant vector DB               | Database persistence storage  |
| `/data/apple_notes`   | Apple Notes ingestion folder   | Mount exported notes here     |
| `/data/obsidian_vault`| Obsidian vault folder          | Mount your Obsidian vault here|
| `/data/scanner_watch` | Filesystem Scanner watch path  | Folders to auto-scan for docs |

---

## Next Steps

- Configuration via `.env` and `settings.yaml` files to customize API keys, model selections, and agent parameters.  
- Docker Compose for seamless container orchestration, enabling easy deployment and upgrades.  
- Expand agents and ingestion types as needed to tailor the assistant to your specific domain or interests.  

---

Feel free to open issues or pull requests to suggest enhancements or report bugs.  
This project aims to provide a powerful, open foundation for self-hosted AI assistants that respect privacy and empower users.

---

*Happy self-hosting!*
