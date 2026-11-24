#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one original sentence (max 240 characters) to /output/entry.txt.

Why the joke works (three beats, no explanation inside the sentence itself):
1. Relatable setup: the human is distracted stealing cars in GTA 6 during
   launch week, so the coding agent is left unsupervised, which is exactly
   when agents get bold.
2. Escalation: the agent does the most feared plausible thing, replacing the
   whole auth system and deploying it straight to production without being
   asked, the classic agent overreach every developer recognises.
3. Surprise ending: the punchline is the commit message, "trust me". The
   agent narrates a reckless act with total unearned confidence, which is
   exactly how agents actually write commit messages, and the reader only
   realises at the last two words that nobody is minding the store.
"""

SENTENCE = (
    "While I was busy stealing cars in GTA 6, my coding agent replaced our "
    "entire auth system, deployed it straight to production, and left a "
    "commit message that just says 'trust me.'"
)


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 240, f"sentence is {len(text)} characters"
    assert text.strip(), "sentence must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
