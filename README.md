# RickSanchez Agentic Agent

A chat REPL with a sardonic mad-scientist personality layered on top of
Claude, via `chat.py`'s system prompt. Purely conversational — no tool
access, no autonomy, no memory beyond the current session.

## Setup

```
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
cp .env.example .env        # then fill in ANTHROPIC_API_KEY
```

## Run

```
python chat.py
```

Type `exit` or Ctrl+C to quit.

## Notes

- Personality lives entirely in `SYSTEM_PROMPT` in `chat.py` — tune it there.
- History is in-memory only; nothing is persisted between runs.
- `MODEL` in `.env` defaults to `claude-sonnet-5` if unset.
