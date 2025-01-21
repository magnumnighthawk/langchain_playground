# LangChain Food Tips Generator

A simple Python application that generates food tips using LangChain and OpenAI's GPT-3.5 model or HuggingFace models. The application also integrates tools for searching YouTube for relevant recipe videos.

## Description

This project demonstrates the basic usage of LangChain to create a chain that generates customized food tips based on sentiment and keyword inputs. It supports both OpenAI's GPT-3.5-turbo-instruct model and HuggingFace models to generate human-like responses. Additionally, it includes tools for searching YouTube for relevant recipe videos and provides a chatbot interface for user interaction.

## Prerequisites

- Python 3.7+
- OpenAI API key (if using OpenAI)
- HuggingFace API token (if using HuggingFace)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

   This command tells `pip` to read the `requirements.txt` file and install all the packages specified in it. Make sure you run this command in the directory where your `requirements.txt` file is located.

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
python chatbot.py
```

You can modify the model settings in the code:

```python
# For OpenAI
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)

# For HuggingFace
llm = HuggingFaceHub(repo_id="google/flan-t5-base",
                     model_kwargs={"temperature": 0.9})
```

### Running in Jupyter Notebook

To run the program in a Jupyter Notebook:

1. Install Jupyter Notebook:

   ```bash
   pip install notebook
   ```

2. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Create a new Python notebook and copy the relevant code from `langgraphing.py` into the notebook cells.

4. Run the notebook cells to execute the program and interact with the chatbot.

## Example Output

The program will generate tips based on the provided sentiment and keyword. For example:
```
"Here's a great food tip: Always try to eat a rainbow of colors on your plate for maximum nutritional benefits!"
```

## Features

- Customizable prompt template
- Adjustable temperature for response creativity
- Integration with YouTube for recipe video suggestions
- Functionality to serialize messages for easier handling
- Interactive chatbot interface for user queries

## New Features

- Added a new feature for generating recipe suggestions based on user preferences.
- Integrated YouTube search for relevant recipe videos.
- Instructions for running the program in Jupyter Notebook.

## Contributing

Feel free to submit issues and pull requests.