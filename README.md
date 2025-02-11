LangGraph and Groq-Based Text Analysis Pipeline

This project is a text analysis pipeline built using LangGraph and Groq, featuring a Streamlit web interface for seamless user interaction. It allows users to classify text, extract entities, generate summaries, analyze sentiment, and more through a modular workflow.

🚀 Overview

Key Features

LangGraph Workflow: Implements a graph-based workflow for structured text analysis.

Groq AI Integration: Leverages Groq language models for NLP tasks.

Streamlit UI: Provides an intuitive web-based interface for user interaction.

Comprehensive Text Analysis: Performs classification, entity recognition, summarization, sentiment analysis, keyword extraction, and context detection.

#How It Works

Text Classification: Categorizes text into types like News, Blog, Research, Technology, etc.

Entity Extraction: Identifies key entities (persons, organizations, locations).

Text Summarization: Generates a concise summary of the input text.

Sentiment Analysis: Analyzes whether the text is positive, negative, or neutral.

Keyword Extraction: Extracts important keywords from the text.

Context Analysis: Determines the broader theme (e.g., Business, Health, Entertainment).

#📌 Prerequisites

Python 3.8+

Groq API key (stored in a .env file)

#🔧 Installation

Clone the Repository:

git clone https://github.com/yourusername/Text-Analysis-Pipeline.git
cd Text-Analysis-Pipeline

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

Run the Application:

streamlit run Text_Analysis_Pipeline.py

#📂 Project Structure

├── Text_Analysis_Pipeline.py  # Main application with LangGraph workflow
├── requirements.txt           # Dependencies
├── .env                       # API Key storage (not to be committed)
├── README.md                  # Documentation

#🎯 Usage

Open the Streamlit web interface.

Enter a piece of text in the input box.

Click Analyze Text to process it through the pipeline.

View the results including classification, extracted entities, and summary.

##🛠 Technologies Used

Python: Core programming language.

LangGraph: For workflow management.

Groq AI: NLP processing.

Streamlit: Web interface.

##🚀 Future Enhancements

Add more NLP features like topic modeling.

Enable file upload for bulk text processing.

Implement user authentication for secure access.

#🤝 Contributing

Contributions are welcome! Feel free to submit a pull request with improvements.

###📝 License

This project is open-source and available under the MIT License.

🔹 Developed by Muhammad Shahzaib Shahid
