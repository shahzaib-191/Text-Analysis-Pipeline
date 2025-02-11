# LangGraph and Groq-Based Text Analysis Pipeline

This project demonstrates a text analysis pipeline built using LangGraph and Groq, integrated with a Streamlit web interface. It allows users to classify text, extract entities, and generate summaries through a modular workflow.

## Overview

### Key Features
- **LangGraph**: Manages graph-based workflows for complex data processing.
- **Groq Integration**: Uses Groq AI for powerful language model processing.
- **Streamlit Interface**: A user-friendly web interface to interact with the pipeline.
- **Text Analysis**: Classifies input text, extracts entities, and generates summaries.

### How It Works
- **Text Classification**: Categorize text into News, Blog, Research, or Other.
- **Entity Extraction**: Identify key entities like persons, organizations, and locations.
- **Text Summarization**: Generate a concise summary of the text.
- **Sentiment Analysis**: Analyze the tone of the text (Positive, Negative, Neutral).
- **Keyword Extraction**: Extract important keywords or phrases.
- **Context Analysis**: Understand the broader context or theme (Business, Technology, etc.).

## Prerequisites
- Python 3.8+
- Groq API key (Add this to a `.env` file in the root directory)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/maryamsafdar/Text-Analysis-Pipeline-Project/tree/main
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your Groq API key:
    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Project Structure

- `app.py`: The main application file that contains the Streamlit app and LangGraph workflow.
- `.env`: Holds environment variables like the Groq API key.
- `requirements.txt`: Lists all required Python packages.
- `README.md`: Documentation for setting up and understanding the project.

## Usage
1. Start the app by running the Streamlit command.
2. Input a sample text into the web interface.
3. Click on the provided buttons to see the classification, extracted entities, and summary.
4. View the graph-based workflow visualization.

## Technologies Used
- **LangGraph**: For creating and managing the workflow.
- **Groq**: Provides AI-powered responses for classification, entity extraction, and summarization.
- **Streamlit**: To create an interactive and easy-to-use web interface.
- **Python**: Core programming language used for development.

## Future Improvements
- Extend the workflow to include more stages like sentiment analysis or topic modeling.
- Add user authentication to secure access.
- Allow users to upload text files directly for processing.

