[![Format and Lint](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/format_and_lint.yml/badge.svg)](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/format_and_lint.yml)
[![Python Tests](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/python-tests_and_%20docker.yml/badge.svg)](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/python-tests_and_%20docker.yml)
[![Docker Build and Deploy](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/docker-build-deploy.yml/badge.svg)](https://github.com/JaredBaileyDuke/prompt-enhancer-with-local-llm/actions/workflows/docker-build-deploy.yml)

# Prompt Enhancer with a Local LLM
A systematic prompt enhancer with a local LLM (using llamafile) for increased security and portability.

After years of bad press from hacks and data leaks, corporate employees are facing increased pressure to keep their company's information safe. Many corporations have even taken the stance that employees must not use online LLMs, such as ChatGPT, for fear of what the employees may share (trade secrets, strategy, upcoming plans, etc.). Some employees looking to use the latest AI tools find themselves unable to convince their security and legal teams to accept the risk.

This tool allows users to interact with an LLM in a safe and secure manner. In addition, this tool is designed for prompt enhancements specific to your purpose and industry. Through answering 7 short questions, users can seek the best outputs from the LLM. This is especially helpful for those less accustomed to LLMs.

## Why This Product?
- 100% local, 100% private, can be run without an internet connection
- For Windows, Mac, and Linux machines
- For use on both:
  - CPU only machine
  - GPU machine (Can detect and use your GPU, whether it is from Apple, NVIDIA, or AMD)
- Open Source
- Free
- Prompt enhancement naturally built into 7 step process

## How To Videos
### Windows
### Mac
### Linux

## Tool Architecture
The architecture was ekpt sleak and simple. 
- The users interacts with the Streamlit frontend
- The frontend calls an API
- The API call interacts with the LLM, and relays output back to the frontend

<p align="center">
  <img src="images/architecture.png" alt="Architecture Diagram">
</p>


