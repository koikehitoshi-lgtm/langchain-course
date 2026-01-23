"""
Quick example: prints the installed langchain-openai module version.

Run:
  cd ~/Desktop/langchain-course
  source .venv/bin/activate
  python examples/langchain_openai_example.py

This example does not call the OpenAI API — set `OPENAI_API_KEY`
and extend the file if you want to make requests.
"""

import importlib


def main():
    m = importlib.import_module("langchain_openai")
    print("langchain_openai version:", getattr(m, "__version__", "unknown"))


if __name__ == "__main__":
    main()
