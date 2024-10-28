import google.generativeai as genai
import os
from typing import Dict, List
import re

class IndianContextChatbot:
    def __init__(self, api_key: str):
        """Initialize the chatbot with Gemini API key."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        
        # Basic greeting patterns
        self.greeting_patterns = {
            r'\b(hi|hello|hey|namaste)\b': [
                "Namaste! How can I assist you today?",
                "Hello! I'm your  AI assistant.",
                "Hi there! Looking forward to have a conversation with you."
            ]
        }

    def generate_indian_context_prompt(self, user_input: str) -> str:
        """Generate a prompt that enforces Indian context."""
        # Check if the input is asking about specific topics
        topics_to_contextualize = {
            r'\b(cricket.*player|player.*cricket)\b': 'Please only mention Indian cricket players in your response.',
            r'\b(food|dish|cuisine)\b': 'Please only mention Indian foods and dishes in your response.',
            r'\b(movie|film|cinema)\b': 'Please only discuss Indian movies and cinema in your response.',
            r'\b(music|song|singer)\b': 'Please only discuss Indian music, songs, and singers in your response.',
        }
        
        context = "Please provide information specifically in the Indian context. "
        for pattern, instruction in topics_to_contextualize.items():
            if re.search(pattern, user_input.lower()):
                context += instruction
        
        return f"{context}\nUser query: {user_input}"

    def get_response(self, user_input: str) -> str:
        """Get response from the chatbot."""
        # Check for basic greetings first
        for pattern, responses in self.greeting_patterns.items():
            if re.search(pattern, user_input.lower()):
                from random import choice
                return choice(responses)
        
        try:
            # Generate India-specific context prompt
            prompt = self.generate_indian_context_prompt(user_input)
            
            # Get response from Gemini
            response = self.chat.send_message(prompt)
            return response.text
            
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again."

    def reset_chat(self):
        """Reset the chat history."""
        self.chat = self.model.start_chat(history=[])

def main():
    # Replace with your Gemini API key
    GEMINI_API_KEY = "your api key"
    
    # Initialize chatbot
    chatbot = IndianContextChatbot(GEMINI_API_KEY)
    
    print("Namaste! I'm your  AI assistant. Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Thank you for chatting! Namaste! 🙏")
            break
            
        response = chatbot.get_response(user_input)
        print(f"\nAssistant: {response}")

if __name__ == "__main__":
    main()