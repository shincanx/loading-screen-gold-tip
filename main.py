#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (a single line, at most 200 characters) for
stressed developers and AI coding agents to /output/entry.txt and prints it.
No network, no dependencies, fully deterministic.
"""

import os

TIP = "Tip: You and the agent both swear the code works. One of you is lying. The build is loading the truth."


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} characters"
    assert TIP == TIP.strip() and "\n" not in TIP, "tip must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)
    print(TIP)


if __name__ == "__main__":
    main()
