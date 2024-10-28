# AI--Chatbot
This AI chatbot filters all responses to be specific to India. For example, if a user asks about famous singers or cricketers, it will only return Indian names. It uses the Gemini API to generate responses based on user queries and adds context to ensure the answers remain focused on India.
Features
Filters all user queries and provides responses in the Indian context.
Recognizes and responds to greetings like "hi," "hello," and "namaste."
Supports queries related to Indian cricket players, food, movies, and music.
# Requirements
1.Python 3.x
2.The following Python libraries:
google.generativeai

# Installation
1. Install the required dependencies: pip install -r requirements.txt
2. Set up your Gemini API key in the code (replace with your own key):GEMINI_API_KEY = "your-gemini-api-key"
3. Run the chatbot:python chatbot.py
   
# Usage
Upon starting the chatbot, you can ask questions like "Who are some famous singers?" and it will only return Indian singers.

The chatbot also responds to greetings like "hello," "hi," and "namaste."

Example usage:
You: Who are some famous singers?
Assistant: Some famous Indian singers include Lata Mangeshkar, Arijit Singh, and Kishore Kumar.





