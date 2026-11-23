#!/usr/bin/env python3
# Make the Judge Smile (one line, 102 chars, pure stdlib): writes the line to /output/entry.txt.
import os

LINE = "A stranger handed me her umbrella at the bus stop this morning, then walked off into the rain humming."

def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200
    assert text.endswith(".")
    assert text.count(".") == 1
    assert "?" not in text and "!" not in text
    assert ". " not in text
    assert "\n" not in text and "\t" not in text
    assert text == LINE.strip()
    assert text == text.strip()  # no leading/trailing whitespace
    assert "  " not in text  # no double spaces
    assert text[0].isupper()  # starts as a proper sentence
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
