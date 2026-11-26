#!/usr/bin/env python3
"""Lost sock status update: a sock in a police evidence bag.

Writes exactly one status update line to /output/entry.txt.
"""

LINE = "Update: I'm in a police evidence bag labelled Exhibit A. I didn't do it, but the footprints match."


def main():
    # Gate: the entry must be 1-120 Unicode code points, not only whitespace.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
