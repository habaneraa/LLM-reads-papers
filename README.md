# LLM Reads Papers :robot::page_facing_up:

Inspired by [ChatGPT-Paper-Reader](https://github.com/talkingwallace/ChatGPT-Paper-Reader), this project aims to explore how can LLMs help us read research papers. For now, I have rewritten the core parts of ChatGPT-Paper-Reader with [LangChain](https://python.langchain.com/en/latest/index.html) library to make the project more extensible. 

Ideas and contributions are welcomed.

## Features

- Identifying section titles of the paper by regex matching and using a special prompt
- Context length control: it splits the paper based on paper sections and `TextSplitter` from `LangChain`
- Summarization with focusing on a set of user-defined key points

## Roadmap

- Split the paper with more accurate content recognition (excludes references, extract abstract, etc.)
- Recursive summarization to make the output to the desired length.
  - summary < 500 words → read the abstract!
  - summary > 3000 words → read the introduction & conclusion!
  - summary ~ 1000 words → LLM might help. :thinking:
- Answer specific questions when reading
