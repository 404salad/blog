#!/usr/bin/env python3
import re
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"

FILLERS = [
    "very", "really", "just", "actually", "basically", "quite",
    "extremely", "totally", "literally", "maybe", "perhaps",
    "somewhat", "rather"
]

# regex
_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+|\n+')
_WORD_RE = re.compile(r"\w+['-]?\w*|\w+")
_BE_VERB = r"(?:am|is|are|was|were|be|been|being)"
_PASSIVE_SIMPLE_RE = re.compile(rf'\b{_BE_VERB}\b\s+\w+(?:ed|en|n)\b', re.IGNORECASE)
_PASSIVE_BY_RE = re.compile(
    rf'\b{_BE_VERB}\b\s+\w+(?:ed|en|n)\s+by\b',
    re.IGNORECASE
)

def split_sentences(text: str):
    return [p.strip() for p in _SENTENCE_SPLIT_RE.split(text) if p.strip()]

def word_count(s: str) -> int:
    return len(_WORD_RE.findall(s))

def find_fillers(sentence: str):
    found = []
    for filler in FILLERS:
        for m in re.finditer(r'\b' + re.escape(filler) + r'\b', sentence, re.IGNORECASE):
            found.append((m.group(0), m.start(), m.end()))
    return found

def find_passive(sentence: str):
    spans = []
    for m in _PASSIVE_BY_RE.finditer(sentence):
        spans.append((m.start(), m.end(), m.group(0)))
    for m in _PASSIVE_SIMPLE_RE.finditer(sentence):
        spans.append((m.start(), m.end(), m.group(0)))
    return spans

def analyze(text: str, max_words: int = 20):
    sentences = split_sentences(text)
    for i, s in enumerate(sentences, start=1):
        issues = []
        fillers = find_fillers(s)
        passives = find_passive(s)
        long = word_count(s) > max_words
        complex_ = s.count(',') >= 3 or ';' in s

        if not (fillers or passives or long or complex_):
            continue  # skip clean sentences

        print(f"line {i}: {s}")

        if fillers:
            marked = s
            for _, start, end in sorted(fillers, key=lambda t: t[1], reverse=True):
                marked = marked[:start] + MAGENTA + marked[start:end] + RESET + marked[end:]
            print("  Filler:", marked)

        if passives:
            for start, end, phrase in passives:
                print("  Passive:", s[:start] + MAGENTA + phrase + RESET + s[end:])

        if long:
            print(RED + f"  Long sentence ({word_count(s)} words)" + RESET)
        if complex_:
            print(RED + "  Complex sentence (many commas/clauses)" + RESET)

        print()

def main():
    text = sys.stdin.read()
    if not text.strip():
        print("Provide text on stdin.")
        return
    analyze(text)

if __name__ == "__main__":
    main()

