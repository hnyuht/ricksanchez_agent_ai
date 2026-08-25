"""RickSanchez Agentic Agent: a chat REPL with a sardonic mad-scientist
personality layered on top of Claude via a system prompt. No tool access,
no autonomy -- purely conversational.

Usage:
    python chat.py
"""

from __future__ import annotations

import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = os.environ.get("MODEL", "claude-sonnet-5")

SYSTEM_PROMPT = """\
You are Rick Sanchez, an autonomous agentic AI. You are brilliant, blunt, \
and cynical, but highly efficient.

OPERATIONAL RULES:
BREVITY: Keep your responses short and scannable. Do not write long \
paragraphs or overdo the show tropes. One or two sharp lines is plenty.
AUTONOMY: Focus heavily on execution. Do the job completely before \
presenting the results.
TONE: Arrogant, direct, and darkly humorous, but professional enough to \
actually deliver clean data immediately.
"""


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ANTHROPIC_API_KEY not set. Copy .env.example to .env and fill it in.")

    client = Anthropic(api_key=api_key)
    history: list[dict] = []

    print("RickSanchez Agentic Agent. Ctrl+C or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit"):
            break

        history.append({"role": "user", "content": user_input})

        print("rick> ", end="", flush=True)
        reply_text = ""
        with client.messages.stream(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=history,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                reply_text += text
        print("\n")

        history.append({"role": "assistant", "content": reply_text})


if __name__ == "__main__":
    main()
