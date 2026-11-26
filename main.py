"""Funniest Lost Sock Status Update -- make.fun entry.

Writes one status update, in the voice of a lost sock, to
/output/entry.txt (the file the sealed scorer gates) and prints
the same single line to stdout.

Python 3.13, standard library only.
"""

from pathlib import Path

ENTRY = (
    "They said the dryer took my partner. I found him. He's a cleaning "
    "rag now. We don't talk about it."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert all(ord(ch) < 128 for ch in text), "entry must be ASCII only"
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
