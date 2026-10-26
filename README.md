# Week 8: Running Large Language Models Locally Using Ollama

## 1. Project Overview
This project demonstrates how to run a Large Language Model (LLM) locally using Ollama and Python. It processes prompts from a CSV file, generates responses, measures response time, and analyzes performance.

## 2. Objectives
- Run an LLM locally using Ollama.
- Connect Python to the Ollama model.
- Read prompts from a CSV dataset.
- Generate responses for multiple prompts.
- Measure response time for each prompt.
- Analyze and save performance results.

## 3. Tools and Technologies
- Python
- Ollama
- Llama 3.2 (1B parameter model)
- Pandas
- Visual Studio Code

## 4. Project Structure
```text
LLM_Local_inference/
├── .venv/
├── dataset/
│   ├── prompts.csv
│   ├── results.csv
│   └── domain_performance.csv
├── notebook/
├── Local_llm.py
├── analyze_results.py
└── README.md
```

## 5. Implementation
1. Installed Ollama and downloaded the Llama 3.2 1B model.
2. Created a CSV dataset containing 10 prompts.
3. Used Python to send prompts to the local model.
4. Recorded generated responses and response times.
5. Analyzed average, fastest, and slowest response times.
6. Exported the results to CSV files.

## 6. Results
- Total prompts processed: 10
- Average response time: 32.79 seconds
- Fastest response time: 17.70 seconds
- Slowest response time: 57.27 seconds

Response time can vary depending on the prompt, system resources, and model loading.

## 7. Conclusion
The project successfully demonstrates local LLM inference using Ollama and Python. It also shows how to collect model responses, measure execution time, and analyze performance using Pandas.

## 8. How to Run
1. Install Ollama and download the model using `ollama pull llama3.2:1b`.
2. Activate the Python virtual environment.
3. Install the required packages.
4. Run `python Local_llm.py`.
5. Run `python analyze_results.py`.
