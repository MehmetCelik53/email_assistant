# Email Assistant

This repository contains a LangGraph-powered Email Assistant agent. It can triage, respond, and manage email workflows using LLMs and custom tools. The main logic is in a Jupyter notebook, with supporting Python modules for prompts, schemas, and utilities.

## Files
- app.ipynb: Main notebook with agent logic and workflow demos
- prompt_templates.py: Templates for prompts used in the agent
- prompts.py: Prompt strings and configuration
- schemas.py: Pydantic schemas for agent state and input
- utils.py: Utility functions for parsing and formatting emails

## Usage
Open `app.ipynb` in Jupyter or VS Code and run the cells to simulate email triage and response scenarios. The agent can:
- Classify emails as IGNORE, NOTIFY, or RESPOND
- Use tools to draft emails, schedule meetings, check calendar availability, and ask follow-up questions
- Handle human-in-the-loop (HITL) interruptions for review and feedback

## Features
- Modular workflow using LangGraph and LangChain
- Custom tools for email and calendar management
- HITL support for safe and accurate automation
- Example scenarios for real-world email handling

## License
MIT

---

### Türkçe Özet
Bu depo, LangGraph ve LangChain ile geliştirilmiş bir Email Assistant (E-posta Asistanı) içerir. E-postaları sınıflandırır, yanıtlar ve takvim işlemlerini otomatikleştirir. Ana mantık Jupyter defterinde, yardımcı Python dosyaları ise istemci ve araç mantığını içerir. Notebook'u çalıştırarak e-posta iş akışlarını test edebilirsiniz.