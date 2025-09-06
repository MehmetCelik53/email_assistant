from typing import List, Any
import json
import html2text

def parse_email(email_input: dict) -> dict:
    """Parse an email input dictionary.

    Args:
        email_input (dict): Dictionary containing email fields:
            - author: Sender's name and email
            - to: Recipient's name and email
            - subject: Email subject line
            - email_thread: Full email content

    Returns:
        tuple[str, str, str, str]: Tuple containing:
            - author: Sender's name and email
            - to: Recipient's name and email
            - subject: Email subject line
            - email_thread: Full email content
    """
    return (
        email_input["author"],
        email_input["to"],
        email_input["subject"],
        email_input["email_thread"],
    )


def format_for_display(tool_call):
    """Format content for display in Agent Inbox

    Args:
        tool_call: The tool call to format
    """
    # Initialize empty display
    display = ""

    # Add tool call information
    if tool_call["name"] == "write_email":
        display += f"""# Email Draft

     **To**: {tool_call["args"].get("to")}
     **Subject**: {tool_call["args"].get("subject")}
     
     {tool_call["args"].get("content")}
     """
    elif tool_call["name"] == "schedule_meeting":
        display += f"""# Calendar Invite
     
     **Meeting**: {tool_call["args"].get("subject")}
     **Attendees**: {', '.join(tool_call["args"].get("attendees"))}
     **Duration**: {tool_call["args"].get("duration_minutes")} minutes
     **Day**: {tool_call["args"].get("preferred_day")}
     """
    elif tool_call["name"] == "Question":
        # Special formatting for questions to make them clear
        display += f"""# Question for User
        
        {tool_call["args"].get("content")}
        """
    else:
        # Generic format for other tools
        display += f"""# Tool Call: {tool_call["name"]}

        Arguments:"""

        # Check if args is a dictionary or string
        if isinstance(tool_call["args"], dict):
            display += f"\n{json.dumps(tool_call['args'], indent=2)}\n"
        else:
            display += f"\n{tool_call['args']}\n"
    return display


def format_email_markdown(subject, author, to, email_thread, email_id=None):
    """Format email details into a nicely formatted markdown string for display

    Args:
        subject: Email subject
        author: Email sender
        to: Email recipient
        email_thread: Email content
        email_id: Optional email ID (for Gmail API)
    """
    id_section = f"\n**ID**: {email_id}" if email_id else ""

    return f"""

**Subject**: {subject}
**From**: {author}
**To**: {to}{id_section}

{email_thread}

---
"""


def show_graph(graph, xray=False):
    """Display a LangGraph mermaid diagram with fallback rendering.

    Handles timeout errors from mermaid.ink by falling back to pyppeteer.

    Args:
        graph: The LangGraph object that has a get_graph() method
    """
    from IPython.display import Image

    try:
        # Try the default renderer first
        return Image(graph.get_graph(xray=xray).draw_mermaid_png())
    except Exception as e:
        # Fall back to pyppeteer if the default renderer fails
        import nest_asyncio

        nest_asyncio.apply()
        from langchain_core.runnables.graph import MermaidDrawMethod

        return Image(
            graph.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.PYPPETEER)
        )
