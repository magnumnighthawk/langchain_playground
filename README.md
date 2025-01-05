# LangChain Food Tips Generator

A simple Python application that generates food tips using LangChain and OpenAI's GPT-3.5 model or HuggingFace models.

## Description

This project demonstrates the basic usage of LangChain to create a chain that generates customized food tips based on sentiment and keyword inputs. It supports both OpenAI's GPT-3.5-turbo-instruct model and HuggingFace models to generate human-like responses.

## Prerequisites

- Python 3.7+
- OpenAI API key (if using OpenAI)
- HuggingFace API token (if using HuggingFace)

## Installation

1. Clone this repository:

2. Install required packages:
```bash
# For OpenAI
pip install langchain langchain-community openai

# For HuggingFace
pip install langchain langchain-community langchain-huggingface
```

3. Set up your API credentials:
   
   For OpenAI:
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
   ```

   For HuggingFace:
   ```bash
   export HUGGINGFACEHUB_API_TOKEN='your-huggingface-api-token'
   ```

## Usage

Run the script using Python:

```bash
python chain.py
```

You can modify the model settings in the code:

```python
# For OpenAI
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)

# For HuggingFace
llm = HuggingFaceHub(repo_id="google/flan-t5-base",
                     model_kwargs={"temperature": 0.9})
```

## Example Output

The program will generate tips based on the provided sentiment and keyword. For example:
```
"Here's a great food tip: Always try to eat a rainbow of colors on your plate for maximum nutritional benefits!"
```

## Features

- Customizable prompt template
- Adjustable temperature for response creativity
- Simple and easy to modify for different use cases


## Contributing

Feel free to submit issues and pull requests.


Here's the README.md content as a string within quotes:

