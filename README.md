# Email Assistant

LangGraph-powered Email Assistant agent that can automatically triage, respond to, and manage emails with human-in-the-loop (HITL) capabilities.

## Features

- **Email Triage**: Automatically classifies emails as "ignore", "notify", or "respond"
- **Human-in-the-Loop**: Provides interrupts for review and editing of AI-generated responses
- **Meeting Scheduling**: Can schedule meetings and check calendar availability
- **Tool Integration**: Supports multiple tools for email and calendar management

## Project Structure

- `app.ipynb` - Main Jupyter notebook with the complete email assistant implementation
- `prompts.py` - Email triage and agent system prompts
- `prompt_templates.py` - Tool descriptions for HITL workflow
- `schemas.py` - Pydantic schemas for state management
- `utils.py` - Utility functions for email parsing and formatting

## Key Components

### Email Triage
The system automatically classifies incoming emails into three categories:
1. **IGNORE** - Emails not worth responding to (newsletters, spam, etc.)
2. **NOTIFY** - Important information that doesn't require a response
3. **RESPOND** - Emails that need a direct response

### Human-in-the-Loop Features
- Review AI-generated email drafts before sending
- Edit meeting requests and scheduling details
- Provide feedback on responses
- Accept, ignore, or modify AI suggestions

### Tools Available
- `write_email` - Draft and send email responses
- `schedule_meeting` - Create calendar meetings
- `check_calendar_availability` - Find available time slots
- `Question` - Ask user for clarification
- `Done` - Mark task completion

## Usage

The system processes emails through a multi-step workflow:

1. **Triage Router** - Analyzes incoming emails and decides routing
2. **Interrupt Handlers** - Provide human oversight at key decision points
3. **Response Agent** - Generates appropriate responses using available tools

Run the `app.ipynb` notebook to see the email assistant in action with various scenarios.

## Configuration

The system includes configurable preferences for:
- Background information (user context)
- Triage instructions (classification rules)
- Response preferences (tone, style, requirements)
- Calendar preferences (meeting durations, scheduling)

## Dependencies

- LangGraph for workflow orchestration
- LangChain for LLM integration
- Pydantic for data validation
- OpenAI for language model capabilities

## Development

This project demonstrates advanced LangGraph patterns including:
- Multi-agent workflows
- Human-in-the-loop interrupts
- State management with checkpointing
- Tool calling with validation
- Dynamic routing based on content analysis

Built with Python 3.13+ and modern AI/ML libraries for production-ready email automation.

---

### Türkçe Özet
Bu depo, LangGraph ve LangChain ile geliştirilmiş gelişmiş bir Email Assistant (E-posta Asistanı) içerir. E-postaları otomatik olarak sınıflandırır, yanıtlar ve insan-döngü-içi (HITL) özellikleri ile takvim işlemlerini yönetir. Notebook'u çalıştırarak çeşitli e-posta senaryolarını test edebilirsiniz.