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

## App Use

### First Stage: Prompt Entry
At the opening page of the app, you have the ability to write your prompt which the LLM will later answer.
<p align="center">
  <img src="images/enter_prompt.png" alt="Enter Prompt">
</p>

### Second Stage: Prompt Enhancement
There are seven ways in which you can enhance your prompt, or you can skip ahead by clicking the Finish button.
<p align="center">
  <img src="images/enter_purpose.png" alt="Enter Purpose">
</p>

### End Stage & Beyond: Model Output
At this stage, the model responds to your enhanced prompt. This may take a few minutes to run based on your computer's speed. At the bottom of the page is an option to run another prompt.
<p align="center">
  <img src="images/model_output.png" alt="Model Output">
</p>

## App Setup
### Overview
The interface of the tool is within a Docker image, which we'll make into a Docker container. The Llamafile is located outside the Docker container. The Docker container and Llamafile will be setup to communicate with each other. The result will be a locally hosted app which you can interact with through your web browser.

### Docker Image
#### Download the Docker Image
Using a bash terminal, pull the image from DockerHub (ensure that Docker Desktop is running)
- `docker pull jaredbaileyduke/local-prompt-enhancer:latest`

#### Create a Running Container
Using the downloaded image, create a running container which can communicate with both the your web browser and the Llamafile.
- `docker run -d -p 8501:8501 jaredbaileyduke/local-prompt-enhancer`

### Llamafile
#### Download a Llamafile
Executible LLMs can be found at the following GitHub repostitory:
<p>
  <a href="https://github.com/Mozilla-Ocho/llamafile">
  https://github.com/Mozilla-Ocho/llamafile
  </a>
</p>

I recommend choosing a smaller LLM in order to ensure the best speed performance. For personal use, I've selected TinyLlama from Meta.

#### Run the Llamafile (Windows)
You can run the Llamafile file two different ways

Using Bash, start the executible:
- `./path-to-model/model.llamafile --server --nobrowser -ngl 999`

Or in the GUI:
1) Rename the Llamafile. The new name should end in .exe
  - For example, TinyLlama-1.1B-Chat-v1.0.F16.llamafile should now be TinyLlama-1.1B-Chat-v1.0.F16.llamafile.exe
2) Run the Llamafile by double clicking on the Llamafile to run the executible


#### Run the Llamafile (Mac and Linux)
1) Make the Llamafile executible
  - `chmod +x path-to-model/model.llamafile`
2) Start the executible
  - `./path-to-model/model.llamafile --server --nobrowser -ngl 999`

### Putting it all Together
Go to web browser and enter the url:
`localhost:8501`

The app is now ready for your use.

## Tool Architecture
The architecture was kept sleak and simple. 
- The users interacts with the Streamlit frontend
- The frontend calls an API
- The API call interacts with the LLM, and relays output back to the frontend

<p align="center">
  <img src="images/architecture.png" alt="Architecture Diagram">
</p>


