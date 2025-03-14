# Implementation of Chatbot using NLP

## Overview
This project is an **AI-powered chatbot** that utilizes **Natural Language Processing (NLP)** to understand and respond to user queries. The chatbot employs **scikit-learn** for intent classification and **Streamlit** for an interactive web interface.

## Features
- ✅ **NLP-based text processing** using NLTK  
- ✅ **Intent recognition** with Machine Learning  
- ✅ **Predefined responses** for different intents  
- ✅ **Interactive Web Interface using Streamlit**  
- ✅ **Conversation History Logging**  
- ✅ **Easily customizable intents and responses**  

## Technologies Used
- **Python** 🐍  
- **NLTK (Natural Language Toolkit)**  
- **Scikit-learn** (TF-IDF Vectorizer & Logistic Regression)  
- **Streamlit** for UI  
- **TextBlob** for spelling correction  
- **JSON for training data**  

## How It Works
1. **Data Preparation**: The chatbot is trained on a dataset containing various **intents, patterns, and responses** (stored in `intents.json`).  
2. **Text Preprocessing**: The input text is **tokenized, vectorized**, and corrected using **TextBlob**.  
3. **Model Training**: A **Logistic Regression model** is trained to classify user input into different intents.  
4. **Response Generation**: Based on the classified intent, the chatbot provides a **predefined response**.  
5. **User Interface**: The chatbot runs as a **Streamlit web app** for an interactive experience.  
6. **Chat Logging**: Conversations are logged in a `chat_log.csv` file.

## Installation
Clone the repository and install dependencies:
```bash
# Clone the repository
git clone https://github.com/0jokerkiller0/Implementation-of-Chatbot-by-using-NLP.git

# Navigate to the project directory
cd Implementation-of-Chatbot-by-using-NLP

# Create and activate a virtual environment
python -m venv chatbot_env
source chatbot_env/bin/activate  # On Windows use: chatbot_env\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

## Usage
To run the chatbot, use the following command:
```bash
streamlit run chatbot_script.py
```
After running the command, the chatbot UI will be accessible in your browser at:
- **Local URL**: [http://localhost:8501](http://localhost:8501)
- **Network URL**: Your machine's local network IP (shown in the terminal output)

## Customization
You can modify `intents.json` to add new **intents, patterns, and responses** to improve the chatbot's functionality.

## Future Enhancements
- 🔹 **Speech-to-Text (STT) and Text-to-Speech (TTS) integration**  
- 🔹 **Deploy as a web app using Flask or FastAPI**  
- 🔹 **Train with Deep Learning (LSTM/RNN) for better accuracy**  
- 🔹 **Real-time API integration (e.g., Weather API, News API)**  

## Contributing
Feel free to **fork**, **modify**, and **contribute** to enhance this chatbot! 🚀

