import os
import sys
import subprocess
import json
import datetime
import csv
import ssl
import streamlit as st
import random

# Function to install required packages
def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            st.warning(f"Installing missing package: {package}")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            st.success(f"Installed {package} successfully!")

# List of required packages
required_packages = [
    "nltk", "textblob", "sklearn", "streamlit"
]

# Install missing packages
install_packages(required_packages)

# Importing dependencies after installation
import nltk
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL workaround for NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download("punkt")

# Load intents
file_path = os.path.abspath("intends.json")
with open(file_path, 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Train the chatbot model
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=100000)

tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent["tag"])
        patterns.append(pattern)

X = vectorizer.fit_transform(patterns)
Y = tags
clf.fit(X, Y)

def correct_spelling(text):
    return str(TextBlob(text).correct())

def chatbot(input_text):
    corrected_text = correct_spelling(input_text)
    input_text = vectorizer.transform([corrected_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
    return "I'm sorry, I didn't understand that. Can you rephrase?"

counter = 0

def main():
    global counter
    st.title("Intents-based Chatbot using NLP")

    menu = ["Home", "Conversation History", "About", "Contact", "Settings", "FAQ"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome to the chatbot. Please ask your queries and press enter after that.")

        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        if user_input:
            user_input_str = str(user_input)
            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye', 'take care']:
                st.write("Thank you for chatting with me! Have a great day!")
                st.stop()
    
    elif choice == "Conversation History":
        st.header("Conversation History")
        try:
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Chatbot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown('--------------')
        except FileNotFoundError:
            st.warning("No chat history found.")

    elif choice == "About":
        st.write("This project demonstrates an NLP-based chatbot using Logistic Regression and Streamlit.")

    elif choice == "Contact":
        st.header("Contact Information")
        st.write("""
                  **Developer:** Sushant Telrandhe  
                  **Email:** worksushanttelrandhe@gmail.com  
                  **GitHub:** [GitHub Profile](https://github.com/0jokerkiller0)  
                  **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/sushant-telrandhe-1917b0236)
                  """)

    elif choice == "Settings":
        st.header("Settings")
        if st.button("Clear Chat History"):
            if os.path.exists('chat_log.csv'):
                os.remove('chat_log.csv')
                st.success("Chat history cleared!")
            else:
                st.warning("No chat history found to clear.")

    elif choice == "FAQ":
        st.header("Frequently Asked Questions")
        st.write("""
                  **Q1: How does this chatbot work?**  
                  A: This chatbot uses NLP techniques and Logistic Regression to understand user queries and respond appropriately.
                  
                  **Q2: Can I contribute to this project?**  
                  A: Yes! You can contribute via GitHub. Feel free to submit pull requests or issues.
                  
                  **Q3: How do I clear chat history?**  
                  A: Go to the 'Settings' menu and click on 'Clear Chat History.'
                  """)

if __name__ == '__main__':
    main()
